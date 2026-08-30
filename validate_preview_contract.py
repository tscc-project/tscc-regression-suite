#!/usr/bin/env python3
import json
from pathlib import Path
root = Path(__file__).resolve().parent
repo = root.parent / "tscc"
contract = json.loads((repo / "docs/compiler-preview-contract.json").read_text())
assert contract["schema_version"] == 1
assert contract["production_dependencies"] == []
assert set(contract["module_modes"]) == {"preserve", "esnext", "commonjs"}
for key in ("positive_project", "negative_project"):
    assert (repo / contract[key]).is_file()
assert (repo / contract["jspp_intersection_source"]).is_file()
assert (repo / contract["candidate_evidence"]).is_file()
assert contract["status"] == "preview-candidate-qualified"
assert "package-node-modules-resolution" in contract["excluded"]
print("tscc compiler preview contract valid")
