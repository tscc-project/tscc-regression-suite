# tscc regression-suite handover

## CP3/TC1 coordination (2026-08-30)

The compiler now retains a durable per-file compilation unit through output
commit. This is an ownership-only checkpoint: the external 519-case contract and
its 492 pass / 0 fail / 27 intentional skip baseline are unchanged. The focused
lifecycle invariant lives in the compiler repository; this suite remains the
black-box behavior gate.

CP4/TC2 replaces tscc's duplicate production traversal with one `ProgramGraph`.
The independent 519-case behavior contract remains the parity gate.

CP5/TC3 adds durable syntax IDs, spans and recovery nodes without changing the
external contract. The 519-case corpus remains the behavior parity gate.

CP19/TC8A adds canonical object-shape infrastructure only. CP20/TC8B promotes
missing-required-property and readonly-write cases: the 525-case external
contract is now 501 pass / 0 fail / 24 intentional skips.

This repository is the standalone compiler-agnostic black-box corpus for tscc.
It should answer whether an arbitrary candidate executable implements the
externally observable TypeScript-to-JavaScript behavior the project claims.

## Authority and current state

- Runner: `run.py --tscc /absolute/path/to/tscc`.
- Corpus: `cases.json`.
- Current retained checkpoint: 533 cases; 509 pass, zero fail, 24
  semantic-checker-only skips after bounded object/property checking.
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

CP8/TC4 hardens internal malformed-input recovery and adds a focused deterministic
parser-budget test. The 519-case external compatibility contract and its
492/0/27 result remain unchanged; no new TypeScript support family is claimed.

CP9/INT0 adds `run_interop.py` and six separately classified fixtures. The runner
uses only the public tscc and JS++ CLIs, executes emitted JavaScript independently
under Node and JS++, and requires both to match an explicit expected completion
value. Its built-in anti-agreement self-test proves equal-but-wrong outputs fail.
These cases are test-only intersection evidence and do not change the 519-case
normal compatibility count.

CP10 changes internal declaration/scope ownership without changing the 519-case
external compatibility count. Its focused binder evidence covers arrows, flat
destructuring, class names and hoisted function identity.

CP13/TC6 expands the contract to 521 cases. Three function-signature cases now
exercise typed ordinary-function arguments, exact bounded arity and annotated
return expressions through tscc. Optional/rest parameters, overloads, generics,
function expressions and contextual typing remain outside this slice.

CP14/TC7A expands the contract to 523 cases and 497/0/26 by promoting literal
union and primitive union mismatch diagnostics. Flow narrowing remains separate.

CP17/TC7B expands the contract to 525 cases and 499/0/26 with guarded-branch
mismatch and post-branch restoration evidence.
## CP22 / TC8C (2026-08-30)

Four nested/excess-policy cases raise the corpus to 529 cases: 505 pass, zero
fail and 24 intentional skips.
## CP24 expression-identity checkpoint (2026-08-30)

The 529-case external contract remains 505/0/24. CP24 changes checker ownership:
expression spans and significant tokens are interned in the compilation unit.

## CP28 reusable object declarations (2026-08-30)

Four alias/interface cases raise the corpus to 533 cases: 509 pass, zero fail
and 24 skips. They cover nested aliases, compatible interface merging, named-path
mismatch diagnostics and readonly metadata across merged declarations.

## CP30–CP31 callable foundation (2026-08-30)

Expression typing now consumes retained nodes, and callable signatures are
canonical type identities. These are internal ownership/model checkpoints; the
533-case observable contract remains 509/0/24 until CP32 enables callable
variables and contextual function expressions.
