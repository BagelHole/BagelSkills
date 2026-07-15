#!/usr/bin/env python3
"""Validate BagelSkills structure and core Agent Skills specification rules."""
from pathlib import Path
import json, re, sys

ROOT=Path(__file__).resolve().parents[1]
SKILLS=ROOT/'skills'
NAME_RE=re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
EXPECTED={'grill-me-until-its-clear','anti-slop-frontend','ux-friction-hunter','failure-museum','scope-sniper','repo-archaeologist','launch-forensics','blast-radius','decision-tribunal','agent-proof-work'}
errors=[]

def err(path,msg): errors.append(f'{path.relative_to(ROOT)}: {msg}')

def parse_frontmatter(path):
    text=path.read_text(encoding='utf-8')
    if not text.startswith('---\n'):
        err(path,'must start with YAML frontmatter at byte 0'); return {},text
    end=text.find('\n---\n',4)
    if end<0:
        err(path,'frontmatter closing delimiter not found'); return {},text
    raw=text[4:end]
    data={}
    # Strict-enough parser for the scalar fields this collection requires.
    for line in raw.splitlines():
        if line.startswith((' ', '\t')) or ':' not in line: continue
        k,v=line.split(':',1); data[k]=v.strip().strip('"\'')
    return data,text[end+5:]

if not SKILLS.is_dir(): errors.append('skills/: missing')
found={p.name for p in SKILLS.iterdir() if p.is_dir()} if SKILLS.is_dir() else set()
if found != EXPECTED:
    errors.append(f'skills/: expected {sorted(EXPECTED)}, found {sorted(found)}')

for d in sorted(SKILLS.iterdir()) if SKILLS.is_dir() else []:
    if not d.is_dir(): continue
    skill=d/'SKILL.md'
    if not skill.exists(): err(d,'SKILL.md missing'); continue
    fm,body=parse_frontmatter(skill)
    name=fm.get('name','')
    desc=fm.get('description','')
    if name != d.name: err(skill,'frontmatter name must equal directory name')
    if not NAME_RE.fullmatch(name) or len(name)>64: err(skill,'name violates Agent Skills naming constraints')
    if not desc or len(desc)>1024: err(skill,'description must be 1..1024 characters')
    if 'when' not in desc.lower(): err(skill,'description must state when to use the skill')
    compat=fm.get('compatibility','')
    if len(compat)>500: err(skill,'compatibility exceeds 500 characters')
    if not body.strip(): err(skill,'body must be non-empty')
    if '**Complete when:**' not in body: err(skill,'workflow lacks completion criteria')
    for rel in ['references/playbook.md','assets/output-template.md','evals/evals.json','evals/trigger-evals.json']:
        if not (d/rel).is_file(): err(d,f'{rel} missing')
    for filename in ['evals/evals.json','evals/trigger-evals.json']:
        p=d/filename
        if p.exists():
            try: data=json.loads(p.read_text())
            except Exception as ex: err(p,f'invalid JSON: {ex}'); continue
            if filename.endswith('trigger-evals.json'):
                if not isinstance(data,list) or not any(x.get('should_trigger') is True for x in data) or not any(x.get('should_trigger') is False for x in data): err(p,'needs positive and negative trigger cases')
            else:
                cases=data.get('evals',[]) if isinstance(data,dict) else []
                if len(cases)<2 or any(not x.get('prompt') or not x.get('expected_output') for x in cases): err(p,'needs at least two complete output evals')

for p in SKILLS.glob('*/SKILL.md'):
    if p.stat().st_size>100_000: err(p,'SKILL.md exceeds 100 KB progressive-disclosure limit')

if errors:
    print(f'FAILED: {len(errors)} problem(s)')
    for e in errors: print(f'- {e}')
    sys.exit(1)
print(f'OK: validated {len(found)} Agent Skills, resources, and eval suites')
