# README.md — Surgical Patch

Apply these edits to the uploaded root `README.md`.

## 1. Repository Structure

Insert this line between `12-monitoring-reporting-and-roadmap/` and `90-visuals/`:

```text
├── 80-operating-evidence/
```

## 2. Folder intent table

Insert this row between the `12-monitoring-reporting-and-roadmap` and `90-visuals` rows:

```markdown
| `80-operating-evidence` | Worked risk-to-control implementation, synthetic operating-evidence, control-testing, and assurance demonstrations |
```

## 3. Section 11 — Operational governance

Under `### Operational governance`, add:

```markdown
- worked operating-evidence package for AI-004 WingInspect Vision, including control implementation, synthetic execution records, human override examples, and control testing.
```

## 4. Section 13 — Evidence and Auditability

Immediately after:

> Where evidence is unavailable, the portfolio should state that explicitly rather than imply operating effectiveness.

insert:

```markdown
### 13.1 Worked operating-evidence example — AI-004 WingInspect Vision

Project W.I.N.G. now includes a worked implementation package showing how a material AI risk is translated into an operating control and an auditable evidence chain.

For **AI-004 — WingInspect Vision**, the package traces:

**AI-004-R01 material safety risk → CTRL-004-01 Mandatory Human Release Gate → accountable manufacturing owner → synthetic inspection execution records → human override evidence → control test → production-evidence gap**

The package demonstrates:

- control design and accountable ownership;
- an execution trigger before final product release;
- independent qualified-human accept/reject authority;
- documented cases in which a human inspector disagrees with the AI output;
- traceable decision and release records;
- a synthetic control test; and
- explicit separation between synthetic workflow evidence and real production operating-effectiveness evidence.

➡️ **[View the AI-004 WingInspect Operating Evidence Package](./80-operating-evidence/AI-004-winginspect/)**

> **Evidence boundary:** The WingInspect execution records and control test are synthetic portfolio artifacts. They demonstrate governance operating-model and assurance design; they do not establish actual WingInspect model performance, real manufacturing outcomes, or production control effectiveness.
```

## 5. Section 16 — Areas Still Under Development

Replace:

```markdown
- expanded evidence repository;
```

with:

```markdown
- expanded operating-evidence coverage beyond the current AI-004 worked example;
```

No other README content should be changed.
