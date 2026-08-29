# tscc regression-suite roadmap

This is a living production-gate roadmap coupled to tscc's compatibility roadmap.
Every compiler checkpoint reviews suite impact; every material corpus discovery
reviews compiler priorities and public support claims.

## Current priorities

1. Establish canonical ownership/synchronization with `tscc/regression` and add a
   cheap automated comparison.
2. Record the exact TypeScript and Node reference versions used for validated
   checkpoints.
3. Map current cases to an explicit feature/support matrix.
4. Identify features that parse but lack runtime, side-effect, scope, negative,
   or project/module evidence.
5. Prioritize incomplete semantic slices and historical bug families.
6. Expand real-world-derived and malformed/recovery cases.
7. Add differential/runtime evidence for each newly advertised feature.
8. Use the corpus under sanitized candidates and future fuzz/generated discovery.
9. Keep website support claims traceable to suite evidence.

CP32 records the first contextual callable-expression contract at 539 cases and
515/0/24. Future callable expansion should add standalone expression-statement,
inference, optional/rest contextual parameter, overload and generic evidence as
each bounded compiler slice becomes real.

After production, new language support expands the contract, TypeScript releases
trigger reference review, production defects become minimized cases, and
performance optimizations must pass semantic gates before acceptance.
