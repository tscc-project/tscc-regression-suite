#!/usr/bin/env python3
import argparse,json,subprocess,sys,tempfile
from pathlib import Path

def agreement(node,js,expected):
    if node!=expected:return False,"Node oracle disagrees with fixture"
    if js!=expected:return False,"JS++ candidate disagrees with Node/fixture"
    return True,""

def self_test():
    checks=[
        agreement("42","42","42")[0],
        not agreement("41","41","42")[0],
        not agreement("42","41","42")[0],
        not agreement("41","42","42")[0],
    ]
    if not all(checks):raise AssertionError("anti-agreement classification failed")

def run(command,timeout=5):
    try:return subprocess.run(command,capture_output=True,text=True,timeout=timeout)
    except subprocess.TimeoutExpired:return None

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--tscc");parser.add_argument("--js");parser.add_argument("--node",default="node");parser.add_argument("--self-test",action="store_true");args=parser.parse_args();self_test()
    if args.self_test and not args.tscc and not args.js:print("interop anti-agreement self-test passed");return 0
    if not args.tscc or not args.js:parser.error("--tscc and --js are required")
    for candidate,prefix in ((args.tscc,"tscc"),(args.js,"JS++")):
        version=run([candidate,"--version"])
        if not version or version.returncode or not version.stdout.startswith(prefix):print(f"{prefix} candidate identity check failed",file=sys.stderr);return 2
    root=Path(__file__).resolve().parent;cases=json.loads((root/"interop/cases.json").read_text())["cases"];passed=failed=0
    node_driver="const fs=require('fs');const v=(0,eval)(fs.readFileSync(process.argv[1],'utf8'));console.log(typeof v==='function'?'[function]':String(v));"
    for case in cases:
        with tempfile.TemporaryDirectory(prefix="tscc-jspp-") as td:
            td=Path(td);source=td/"case.ts";output=td/"out";source.write_text(case["source"]);output.mkdir()
            compiled=run([args.tscc,"--pretty","false","--noResolve","--outDir",str(output),str(source)])
            emitted=output/"case.js"
            if not compiled or compiled.returncode or not emitted.exists():failed+=1;print(f"FAIL {case['id']}: tscc compile failed",file=sys.stderr);continue
            node=run([args.node,"-e",node_driver,str(emitted)]);js=run([args.js,str(emitted)])
            if not node or not js:failed+=1;print(f"FAIL {case['id']}: runtime timeout",file=sys.stderr);continue
            if node.returncode or js.returncode:failed+=1;print(f"FAIL {case['id']}: Node rc={node.returncode}, JS++ rc={js.returncode}\n{node.stderr}{js.stderr}",file=sys.stderr);continue
            ok,detail=agreement(node.stdout.strip(),js.stdout.strip(),case["expect"])
            if ok:passed+=1
            else:failed+=1;print(f"FAIL {case['id']}: {detail}; Node={node.stdout.strip()!r}, JS++={js.stdout.strip()!r}",file=sys.stderr)
    print(json.dumps({"pass":passed,"fail":failed,"eligible":len(cases),"classification":"test-only intersection"}));return 1 if failed else 0
if __name__=="__main__":sys.exit(main())
