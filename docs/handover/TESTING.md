# tscc external-contract testing

## Evidence model

The suite deliberately separates:

```text
accept/reject
emitted structure
runtime semantics
reference compatibility
semantic-checker-only behavior
```

Not every case needs every dimension. Select the strongest oracle for the feature.
For runtime-bearing transforms, execute output and use side effects. For syntax
validity, `tsc --noCheck` is the current authority. Full `tsc` separates semantic
restrictions from parser behavior.

## Feature-family dimensions

Choose relevant cases from basic, nested, parenthesized, combined transform,
function/block/loop/class/module context, shadowing/closure, side-effect operands,
malformed grammar, unexpected EOF, project/module behavior, and diagnostics.

Avoid one happy-path fixture per feature. Avoid meaningless Cartesian explosion.
Ask which interaction can invalidate semantics.

## Evaluation order and scope

Counters, calls, getters, computed properties, update/compound assignment,
destructuring defaults, and short-circuit operands expose duplicate or reordered
evaluation. Assert both result and call count/order.

Scope-sensitive features should consider global, function, nested function,
block, loop, catch, class, module, parameter/rest/default/destructuring, closure,
and imported-binding contexts. Distinguish syntax-owned names/property keys/labels
from runtime references.

## Modules and transforms

Exercise imports, exports, defaults, aliases, re-exports, `export *`, namespaces,
cycles, live updates, type-only forms, CommonJS lowering, dynamic import/import
meta preservation, TSX, and import attributes only within current promised scope.
Multi-file runtime differential fixtures are especially valuable.

## Error behavior

Malformed input must fail controllably: no crash, hang, unbounded loop, corrupted
output, or consumption of unrelated following source. Use timeout protection where
appropriate. Test ambiguous prefixes, comments/newlines, missing delimiters, and
EOF.

## Environment and determinism

Record/pin TypeScript and Node versions for reproducible checkpoints. Control
working/temp paths, module options, colors, environment, and concurrency where
they affect output. Case names and failure output should identify the smallest
useful failure.

### Reconciled oracle checkpoint (2026-08-16)

Against `/home/nick/Repositories/nift/tscc/tscc/tscc`, Node v22.22.1 and
TypeScript 7.0.2, the runner reported 483 pass, one fail, and 27 skip across 511
classifications. The single failure was `semantic-import-meta-commonjs`, whose
expected semantic-only category has changed under this unpinned TypeScript
version. It is reference-classification drift, not an observed tscc runtime or
emit mismatch. The inherited checkpoint with an earlier reference compiler was
483 pass, zero fail, and 28 skip.

The top-level README still says 265 cases and is therefore stale. Prefer deriving
or reporting current totals rather than maintaining a timeless manual count. The
runner currently resolves `tsc` from `PATH`, so exact reproduction requires
pinning it externally until the suite gains an explicit version policy.

## Synchronization

Compare local and standalone suites mechanically. Decide canonical source and
allowed documentation differences. An exact-copy invariant belongs in automation,
not prose alone.

At this reconciliation point, `README.md`, `TSCC_BUG_LOG.md`, `cases.json`, and
`run.py` are byte-identical to the implementation repository's `regression/`
copies. Only `REGRESSION_NOTES.md` differs.

## Bug-family workflow

When one shape fails, inspect siblings under nesting, scope, side effects,
malformed input, and adjacent transforms. Retain minimized production/corpus bugs.
Document methodology here; individual cases belong in `cases.json` and detailed
history in notes/Git.
