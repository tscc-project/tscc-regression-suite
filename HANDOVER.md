# tscc regression-suite handover

This repository is the standalone compiler-agnostic black-box corpus for tscc.
It should answer whether an arbitrary candidate executable implements the
externally observable TypeScript-to-JavaScript behavior the project claims.

## Authority and current state

- Runner: `run.py --tscc /absolute/path/to/tscc`.
- Corpus: `cases.json`.
- Current retained checkpoint: 519 cases; 492 pass, zero fail, 27
  semantic-checker-only skips after bounded assignment and mutability checking.
- Oracles: TypeScript `tsc --noCheck`, full `tsc` for semantic-only
  classification, and Node for runtime cases.

Current files define suite behavior. tscc source owns implementation architecture.
The tscc product handover owns compatibility/product decisions. This repository
owns independent observable evidence.

## Test categories

- **runtime**: candidate output executes under Node and matches expected behavior.
- **emit**: generated output contains/omits required structure.
- **syntax-negative**: `tsc --noCheck` rejects and candidate must reject.
- **semantic-only**: no-check accepts but full `tsc` rejects; skipped until tscc
  has the relevant semantic checker.

Compile success alone is weak evidence. Prefer runtime and side-effect-sensitive
tests for transforms. Exact output snapshots are useful but do not prove semantics.

## Local/standalone relationship

An executable mirror exists at `tscc/regression`. This standalone repository is
the canonical external contract owner; the implementation repository provides
`make check-regression-sync` to compare `cases.json` and `run.py`. This
repository's `REGRESSION_NOTES.md` contains suite-owned checkpoint notes. Update
the standalone contract first and synchronize the mirror in the same checkpoint.

## Running and environment

```bash
python3 run.py --tscc /absolute/path/to/tscc
```

The suite also needs `tsc` and Node. Serious checkpoint reports should record
their versions because reference behavior/output can evolve. The runner controls
color environment for stable Node output and uses temporary directories/case
isolation.

## Adding a regression

```text
reproduce
→ ask reference behavior where compatibility applies
→ reduce to minimal deterministic case
→ choose runtime/emit/syntax-negative/semantic-only category
→ confirm candidate fails for intended reason
→ fix compiler separately
→ add sibling scope/side-effect/malformed variants
→ full corpus
```

Do not classify a `tsc --noCheck`-accepted/full-`tsc`-rejected restriction as a
parser bug. Do not modify tests merely to make a candidate green without deciding
whether compatibility changed.

## Checkpoints and production gate

A suite checkpoint may add runtime/differential evidence, better classification,
determinism, fixture clarity, or a new failure family without changing tscc.
Counts are checkpoint facts, not the objective.

The suite is a primary production gate: every advertised feature should have
appropriate external evidence; runtime semantics, scope, malformed behavior, and
known bug families should be covered; reference compatibility should be explicit.

## Public actions

Local suite work is normal. Do not commit, push, tag, publish, or redefine public
compiler compatibility without explicit direction.

## Maintaining this handover

This and linked documents are living infrastructure. Review them when corpus
ownership, runner/oracles, reference versions, categories, determinism, or
production responsibilities change. Consolidate durable lessons rather than
appending a diary. Every substantial checkpoint reviews handover and roadmap.

See `docs/handover/TESTING.md` and `docs/handover/ROADMAP.md`.
Detailed suite history lives at
`docs/handover/CONTRACT-HISTORY.md`, including runtime/differential
test philosophy, production-gate responsibilities, and the living roadmap.

CP2 adds `feature-matrix.json` as the machine-readable external evidence map.
Run `python3 validate_feature_matrix.py` to verify its schema, retained case
count, unique families, states, and every named case against the corpus.
