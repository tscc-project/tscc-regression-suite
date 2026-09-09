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
interop = json.loads((root / "interop/cases.json").read_text())
interop_ids = [case["id"] for case in interop["cases"]]
assert interop["schema_version"] == 1
assert len(interop_ids) == len(set(interop_ids)) and interop_ids
for case in interop["cases"]:
    assert "expect" in case
    sources = [key for key in ("source", "source_file") if case.get(key)]
    assert len(sources) == 1, f"{case['id']}: expected exactly one source or source_file"
    if sources[0] == "source_file":
        source_path = (root / case["source_file"]).resolve()
        assert source_path.is_file(), f"{case['id']}: missing source_file {source_path}"
print(f"tscc external feature matrix valid: {len(ids)} families, {len(cases)} cases, {len(interop_ids)} interop cases")
