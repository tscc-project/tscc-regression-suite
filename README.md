# TS -> JS compiler regression suite

Compiler-agnostic regression corpus used to compare `tscc` with TypeScript's reference compiler.

This checkpoint contains **579 cases**, producing **555 pass / 0 fail / 24
deliberate semantic skips**. Runtime and syntax expectations are validated with
`tsc --noCheck`; semantic cases are additionally verified against normal
`tsc --module commonjs`. The explicit module mode prevents TypeScript release
changes to its default configuration from silently reclassifying the corpus.

Install and verify the pinned Node 22.22.1 / TypeScript 7.0.2 oracle environment,
then run against a compiler with:

```bash
npm ci
python3 check_oracles.py
python3 run.py --tscc /path/to/tscc --node tools/node --tsc tools/tsc
```
