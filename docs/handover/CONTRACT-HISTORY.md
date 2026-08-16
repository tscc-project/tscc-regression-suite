# Contract history and institutional context

> This is a living historical companion to the repository's operational handover. The live repository remains authoritative. Maintain, correct, reorganize, or supersede this material as project evidence evolves while retaining durable rationale.

# tscc Regression Suite

## Independent Compiler Contract, Development, Testing and Production-Gate Handover

# 1. Identity

The standalone tscc regression suite should answer:

> Does this tscc executable implement the externally observable compiler behavior the project claims?

It should remain as implementation-independent as practical.

---

# 2. Why independence matters

An external suite can test:

```text
current compiler
old compiler
candidate compiler
alternate implementation
```

without caring about internal class layout.

That gives tscc freedom to refactor.

---

# 3. Relationship to internal suite

Codex identified both:

```text
tscc/tscc/regression
```

and:

```text
tscc-regression-suite
```

The canonical relationship needs to be established.

Possibilities:

```text
standalone canonical
embedded copy synchronized from it
```

or:

```text
local canonical
standalone distribution synchronized from local
```

or deliberate different responsibilities.

Do not guess.

---

# 4. If mirrored, automate checking

If they are intended to match, add a cheap verification mechanism.

Human memory is not sufficient long-term synchronization infrastructure.

---

# 5. Core test classes

The suite should eventually cover several distinct forms.

### Positive compilation

```text
valid supported program
→ success
```

### Negative compilation

```text
invalid program
→ controlled failure
```

### Emission

```text
input
→ expected emitted structure
```

### Runtime

```text
input
→ compile
→ execute
→ expected semantics
```

### Differential/reference

```text
tsc behavior
vs
tscc behavior
```

where compatibility is intended.

---

# 6. Runtime tests are exceptionally valuable

Compiler output can look plausible while being wrong.

Therefore runtime tests should be treated as first-class.

Example:

```text
compile
↓
run under Node
↓
assert stdout/state/exit status
```

---

# 7. Evaluation-order tests

For lowering features, use side effects.

Conceptually:

```ts
let calls = 0;

function f() {
    calls++;
    return value;
}
```

Then verify:

```text
result
AND
calls
```

This detects duplicate evaluation.

---

# 8. Scope matrix

Where relevant test:

```text
global
function
nested function
block
loop
class
module
shadowing
closure
```

Not every feature needs every dimension, but scope-sensitive features should not receive only top-level tests.

---

# 9. Feature matrices

A useful conceptual feature family is:

```text
basic
nested
parenthesized
combined with another expression
side-effect operand
scope variant
malformed
unexpected EOF
```

Select relevant dimensions.

Do not explode into meaningless Cartesian-product testing.

---

# 10. Error behavior

Malformed input should not:

```text
hang
crash
infinite-loop
silently emit nonsense
```

Timeout protection may be useful for parser regressions.

---

# 11. Differential testing

Where TypeScript compatibility is intended:

```text
tsc accepts?
tscc accepts?

tsc runtime?
tscc runtime?

diagnostic category?
```

can be compared.

Pin/reference tool versions sufficiently to avoid false regressions from upstream changes.

---

# 12. Snapshot limitations

Exact emitted-output snapshots are useful for:

```text
stable transform shape
debugging
unexpected codegen changes
```

but should not become the sole oracle.

Two different outputs can be semantically equivalent.

One plausible-looking output can be semantically wrong.

---

# 13. Test environment

Control:

```text
working directory
temp directories
module fixture paths
Node version
TypeScript version
environment variables
```

where they influence results.

---

# 14. Bug workflow

Preferred:

```text
reproduce
↓
compare reference if relevant
↓
reduce
↓
add failing external regression
↓
fix
↓
focused pass
↓
neighboring semantic variants
↓
full suite
```

---

# 15. Production role

The suite is a primary tscc production gate.

Production status should require evidence that:

```text
advertised language features are externally tested
runtime semantics are exercised
negative behavior is controlled
scope-sensitive behavior is covered
known historical bugs remain fixed
reference compatibility is tested where promised
real-world discovered bugs become regressions
```

---

# 16. Current production-roadmap role

**LIVING ROADMAP**

The suite's immediate roadmap should track the compiler roadmap:

```text
establish current supported-feature inventory
↓
map existing tests to features
↓
identify unsupported test dimensions
↓
prioritize incomplete semantic slices
↓
expand runtime tests
↓
expand negative/parser recovery tests
↓
add differential tests where appropriate
↓
add real-world bug regressions
↓
increase adversarial coverage
↓
production candidate full run
```

---

# 17. Coverage matrix

For tscc specifically, I would seriously consider maintaining a machine-readable or easily reviewed coverage matrix connecting:

```text
feature
→ tests
→ support status
```

without making it bureaucratic.

This could become valuable for both website and production planning.

---

# 18. Living roadmap rule

> Every compiler checkpoint should review regression-suite implications and every substantial regression discovery should review the compiler production roadmap. The two roadmaps are coupled. New evidence may reveal that a supposedly complete feature is not production-ready or that a previously high-priority gap is less important than an architectural failure family.

---

# 19. Post-production

After tscc reaches production status:

```text
new language feature
→ new contract tests

new TypeScript release
→ compatibility review

production bug
→ minimized regression

new platform
→ environment validation

performance optimization
→ semantic suite before benchmark acceptance
```

---

# 20. Do not accidentally

```text
test compile success only
treat snapshots as semantics
depend on moving tsc without version control
duplicate local/standalone suites indefinitely
ignore runtime
ignore malformed input
let website support claims outrun the suite
```

---

---

