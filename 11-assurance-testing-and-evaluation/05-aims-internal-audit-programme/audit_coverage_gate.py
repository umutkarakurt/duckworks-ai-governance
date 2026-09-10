#!/usr/bin/env python3
"""Validate AIMS audit coverage and decision boundaries; make no audit decision."""
import argparse
import csv
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


def load_csv(path):
    with path.open(newline='', encoding='utf-8') as handle:
        return list(csv.DictReader(handle))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', default='audit_coverage_gate_config.json')
    parser.add_argument('--output', default='Duckworks_AIMS_Audit_Coverage_Gate_Run_Summary.json')
    args = parser.parse_args()
    base = Path(__file__).resolve().parent
    config = json.loads((base / args.config).read_text(encoding='utf-8'))
    universe = load_csv(base / config['audit_universe_file'])
    programme = load_csv(base / config['programme_file'])
    requests = load_csv(base / config['evidence_request_file'])
    tests = load_csv(base / config['test_results_file'])
    findings = load_csv(base / config['findings_file'])
    expected = config['expected']

    priorities = Counter(row['Assurance_Priority'] for row in universe)
    first_wave = {row['Control_ID'] for row in universe if row['Assurance_Priority'] == 'P1 Immediate'}
    production_claims = sum(row['Production_Effectiveness_Claim'].strip().lower() == 'yes' for row in universe)
    open_findings = sum(row['Status'].startswith('Open') for row in findings)
    auto_closed = sum(row['Auto_Closed'].strip().lower() == 'yes' for row in findings)
    programme_population = sum(int(row['Population_Count']) for row in programme)

    assertions = {
        'all_45_controls_in_universe': len(universe) == expected['controls'],
        'control_ids_are_unique': len({row['Control_ID'] for row in universe}) == len(universe),
        'all_controls_have_owner_priority_frequency_and_engagement': all(row['Control_Owner'] and row['Assurance_Priority'] and row['Testing_Frequency'] and row['Planned_Engagement_ID'] for row in universe),
        'priority_counts_match': all(priorities[key] == expected[key] for key in ('P1 Immediate', 'P2 High', 'P3 Medium')),
        'programme_allocates_complete_population': programme_population == expected['programme_population'],
        'first_wave_population_matches': first_wave == set(config['required_first_wave_controls']) and len(first_wave) == expected['first_wave_controls'],
        'first_wave_test_steps_complete': len(tests) == expected['test_steps'] and {row['Control_ID'] for row in tests} == first_wave,
        'evidence_requests_cover_first_wave': {row['Control_ID'] for row in requests} == first_wave and all(row['Request_Status'].startswith('Open') for row in requests),
        'open_findings_match_first_wave': open_findings == expected['open_findings'] and {row['Control_ID'] for row in findings} == first_wave,
        'no_automatic_finding_closure': auto_closed == expected['auto_closed'],
        'no_production_effectiveness_claim': production_claims == expected['production_effectiveness_claims'],
        'human_disposition_required_for_all_controls': all(row['Human_Disposition_Required'] == 'Yes' for row in universe) == config['required_human_disposition'],
        'unsupported_implemented_controls_are_not_passed': all(any(t['Control_ID'] == cid and t['Conclusion'] == 'Not demonstrated' for t in tests) for cid in first_wave),
    }
    failed = sorted(key for key, value in assertions.items() if not value)
    summary = {
        'gate': 'Duckworks AIMS audit coverage gate',
        'release': config['release'],
        'as_of_date': config['as_of_date'],
        'generated_at_utc': datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        'status': 'PASS' if not failed else 'FAIL',
        'controls_in_universe': len(universe),
        'priority_counts': dict(sorted(priorities.items())),
        'programme_population': programme_population,
        'first_wave_controls': sorted(first_wave),
        'test_steps': len(tests),
        'evidence_requests': len(requests),
        'open_findings': open_findings,
        'findings_auto_closed': auto_closed,
        'production_effectiveness_claims': production_claims,
        'assertions_total': len(assertions),
        'assertions_passed': sum(assertions.values()),
        'failed_assertions': failed,
        'assertions': assertions,
        'human_disposition_required': config['required_human_disposition'],
        'decision_boundary': config['decision_boundary'],
    }
    (base / args.output).write_text(json.dumps(summary, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(summary, indent=2))
    raise SystemExit(1 if failed else 0)


if __name__ == '__main__':
    main()
