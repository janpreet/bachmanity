#!/usr/bin/env python3
"""Repo sanity checks. Run from the repo root: python3 scripts/validate.py"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
errors = []


def err(msg):
    errors.append(msg)


# 1. Plugin manifests parse and agree
try:
    plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
    for key in ("name", "description", "version"):
        if not plugin.get(key):
            err(f"plugin.json: missing '{key}'")
except Exception as e:
    err(f"plugin.json: {e}")
    plugin = {}

try:
    market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
    listed = {p.get("name") for p in market.get("plugins", [])}
    if plugin.get("name") and plugin["name"] not in listed:
        err("marketplace.json: does not list the plugin from plugin.json")
except Exception as e:
    err(f"marketplace.json: {e}")

# 2. Every skill has frontmatter with name (matching its dir) and a description
skill_dirs = sorted(d for d in (ROOT / "skills").iterdir() if d.is_dir())
if not skill_dirs:
    err("skills/: no skills found")

FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
for d in skill_dirs:
    md = d / "SKILL.md"
    if not md.exists():
        err(f"{d.name}: missing SKILL.md")
        continue
    text = md.read_text()
    m = FRONTMATTER.match(text)
    if not m:
        err(f"{d.name}: SKILL.md has no frontmatter")
        continue
    fm = m.group(1)
    name = re.search(r"^name:\s*(\S+)\s*$", fm, re.MULTILINE)
    desc = re.search(r"^description:\s*(.+)$", fm, re.MULTILINE)
    if not name or name.group(1) != d.name:
        err(f"{d.name}: frontmatter name must be '{d.name}'")
    if not desc or len(desc.group(1).strip()) < 40:
        err(f"{d.name}: description missing or too thin to trigger reliably")
    # The core invariant of this repo: persona never compromises the work
    if "The one rule that outranks the bit" not in text:
        err(f"{d.name}: missing 'The one rule that outranks the bit' section")
    if not re.search(r"[Dd]rop the act", text):
        err(f"{d.name}: missing the drop-the-act escape hatch")

# 3. Every skill is mentioned in the README, and no em-dashes anywhere
readme = (ROOT / "README.md").read_text()
for d in skill_dirs:
    if f"`{d.name}`" not in readme:
        err(f"README.md: skill '{d.name}' not listed")

for path in ROOT.rglob("*"):
    if path.is_dir() or ".git" in path.parts or path.suffix == ".svg":
        continue
    if path.suffix in (".md", ".json", ".py", ".yml", ".yaml"):
        text = path.read_text()
        for i, line in enumerate(text.splitlines(), 1):
            if "\u2014" in line or "\u2013" in line:
                err(f"{path.relative_to(ROOT)}:{i}: em/en dash (house rule: plain punctuation)")

if errors:
    print("FAIL")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print(f"OK: {len(skill_dirs)} skills, manifests valid, no em-dashes")
