#!/usr/bin/env python3
import json
from pathlib import Path

root = Path(__file__).resolve().parent
matrix = json.loads((root / "feature-matrix.json").read_text())
cases = json.loads((root / "cases.json").read_text())
names = {case["name"] for case in cases}
assert matrix["schema_version"] == 1
assert matrix["case_count"] == len(cases)
assert matrix["dimensions"] == ["accept", "emit", "runtime", "diagnostic", "project"]
ids = set()
for family in matrix["families"]:
    assert family["id"] not in ids
    ids.add(family["id"])
    assert family["state"] in {"covered", "partial", "planned"}
    assert family["cases"]
    missing = set(family["cases"]) - names
    assert not missing, f"{family['id']}: unknown cases {sorted(missing)}"
print(f"tscc external feature matrix valid: {len(ids)} families, {len(cases)} cases")
