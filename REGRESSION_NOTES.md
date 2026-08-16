# Regression notes

The corpus grew from 216 to **265 cases** in the v0.6.0 checkpoint. The added families cover mapped/conditional/template-literal/indexed/variadic types, const type parameters, destructured parameters, class static/accessor syntax, type-only module forms, ambient enums/classes/functions, namespace merging and dotted namespaces, instantiation expressions, generic expression references, and additional malformed advanced-type grammar.

Current result: **246 pass / 0 fail / 19 semantic-only skips**.

# Regression hardening notes

The corpus grew from 78 to **216 cases** during the v0.5.0 checkpoint. Two adversarial expansion batches attacked richer type grammar, generics, assertions, overloads, classes, ambient declarations, namespaces, enums and malformed recovery.

The expansion repeatedly caught tempting but incorrect test assumptions. In particular, empty generic parameter/argument lists, rest-parameter placement, empty `implements` lists and some parameter-property forms are accepted by `tsc --noCheck` and rejected later by normal `tsc`; they therefore remain semantic-checker cases rather than parser bugs. String-named enum members without explicit initializers are valid TypeScript and were converted into a runtime regression instead of a negative case.

The reference harness was rewritten to batch `tsc --noCheck` and ordinary `tsc` validation. This reduced the 216-case reference pass from hundreds of TypeScript process startups to a handful of invocations while preserving per-file classification.

Current result: **198 pass / 0 fail / 18 deliberate semantic-only skips**. No confirmed TypeScript compiler correctness bug was found in this checkpoint.

## Checkpoint 14 — 454 cases

Expanded from 431 to 454 cases with CommonJS loop/destructuring shadowing, generic object methods, template/property counter-cases, dynamic import/import.meta preservation and stricter malformed module clauses. Current tscc v0.13.0 result: **427 pass / 0 fail / 27 semantic-only skips**.

## Checkpoint 15 — 481 cases

Expanded from 454 to **481 cases** with CommonJS live-import update/compound assignment, computed-property and destructuring-default contexts, parameter/rest/destructured shadowing, destructured exports, namespace/default re-exports and malformed module grammar. Current intermediate result: **454 pass / 0 fail / 27 semantic-only skips**. Fixes included control-flow parentheses no longer being mistaken for parameter scopes, label targets protected from live-import rewriting, destructured parameter shadowing and stricter namespace/default import/export validation.

## Checkpoint 16 — 511 cases

Expanded again to **511 cases** with TSX generic arrows nested inside JSX expressions, string/computed enums, nested/dotted namespaces, parameter-property variants, `satisfies`/`as const`, mapped/conditional/template-literal types, import attributes and malformed counterparts. Current tscc v0.15.0 result: **483 pass / 0 fail / 28 semantic-only skips**. This checkpoint fixed TSX generic arrows with `extends` inside JSX expression context and import-attribute objects being confused with named import specifiers.

## Checkpoint 17 — first binder-backed production transform

Added `cjs-import-function-var-shadow` after the bounded binder exposed a gap in
the legacy CommonJS live-import shadow-range heuristic: a function-local `var`
reference was rewritten as an imported live binding. The binder now protects the
ordinary identifier subset while legacy handling remains for unsupported binding
forms. Current result: **485 pass / 0 fail / 27 semantic-only skips** across 512
cases.

## Checkpoint 18 — bound primitive checking

Promoted two semantic contracts for annotated primitive types flowing through a
bound identifier: one initializer mismatch and one direct assignment mismatch.
Both are shadow-aware through symbol identity. Current result: **487 pass / 0
fail / 27 semantic-only skips** across 514 cases.
