#!/usr/bin/env python3
import argparse
import re
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("--node", default="tools/node")
parser.add_argument("--tsc", default="tools/tsc")
args = parser.parse_args()

node = subprocess.run([args.node, "--version"], capture_output=True, text=True, check=True).stdout.strip()
tsc = subprocess.run([args.tsc, "--version"], capture_output=True, text=True, check=True).stdout.strip()

if node != "v22.22.1":
    raise SystemExit(f"unsupported Node oracle {node!r}; expected v22.22.1")
if tsc != "Version 7.0.2":
    raise SystemExit(f"unsupported TypeScript oracle {tsc!r}; expected Version 7.0.2")

print(f"tscc test oracles valid: Node {node[1:]}, TypeScript {tsc.removeprefix('Version ')}")
