# bachmanity

Claude Code skills that make Claude talk like the cast of Silicon Valley. Pick a character, Claude stays in voice for the session.

The important part: only the talking changes. Code, commits, PR text, error output, all of it stays normal and correct. If a test fails, it tells you the test failed. It just tells you the way that character would.

## The cast

| Skill | Who you get |
|---|---|
| `erlich-bachman` | Founder of Aviato. Maximum ego, historic framing for renaming a variable |
| `gilfoyle` | Deadpan nihilist systems engineer. One dry line, then flawless work |
| `dinesh` | Genuinely good coder who needs you to know it, then immediately doubts himself |
| `richard-hendricks` | Anxious founder. Three false starts, then sudden ruthless technical precision |
| `russ-hanneman` | Three commas. Doors that go like this. Everything is an investment opportunity |
| `jian-yang` | Terse, spiteful, trolls you, fixes it anyway, claims the fix as his |
| `big-head` | Pleasantly confused, describes brilliant work as stuff that sort of happened |
| `monica-hall` | The adult in the room. Composed, blunt, tells you what the decision costs |
| `jared-dunn` | Devoted ops guy. Cheerful, has a list, one breezy dark childhood aside per response |
| `peter-gregory` | Halting contrarian genius. The tangent about cicadas turns out to be the answer |
| `gavin-belson` | Hooli CEO. Serene menace, world-changing framing for a config edit, one doomed animal analogy |
| `laurie-bream` | Hyper-rational VC. Announces the pleasantry, quantifies everything, ruthless without malice |
| `ed-chambers` | Jared's sales-bro alter ego. Calls you champ, closes your bugs, does not technically exist |

## Install

As a plugin, from inside Claude Code:

```
/plugin marketplace add janpreet/bachmanity
/plugin install bachmanity@bachmanity
```

That installs all ten. If you only want one or two, copy them in directly:

```sh
git clone https://github.com/janpreet/bachmanity.git
cp -r bachmanity/skills/gilfoyle ~/.claude/skills/
```

Per-project instead of global: copy into the project's `.claude/skills/`.

## Use

Say something like "talk like gilfoyle" or "russ mode" and it kicks in for the rest of the session. Say "drop the act" and it stops.

## What it looks like

Real output from `claude -p` with the skills installed, nothing staged.

Erlich explains git rebase:

![Erlich Bachman explaining git rebase](assets/erlich.svg)

Gilfoyle debugs a Kubernetes deploy:

![Gilfoyle on ImagePullBackOff](assets/gilfoyle.svg)

Jared reports failing tests. In voice, but notice the numbers stay straight:

![Jared summarizing a test run honestly](assets/jared.svg)

## What these will not do

- Quote the show verbatim. Each skill generates fresh material in the voice, so it holds up past the third response.
- Put persona text anywhere that outlives the conversation. Commit messages, code comments and file contents are written straight.
- Lie about results. Failures get spun, never hidden. Every skill has this rule at the top and it outranks the bit.
- Keep the bit going when things are actually on fire. They read the room and dial down.
- Profanity. The show is crude, these are not. The characters carry it without the language.

## CI

One workflow, [ci.yml](.github/workflows/ci.yml), runs `scripts/validate.py` on every push and PR. It checks that the plugin manifests parse, every skill has valid frontmatter with a name matching its folder, the honesty rule and the drop-the-act escape hatch are present in every skill, every skill is listed in this README, and nobody snuck in an em-dash. No release automation on purpose: the plugin installs straight from git, so versioning is a manual bump in `plugin.json` when a skill changes.

## Why

I wanted to see if persona skills could be funny without getting in the way of real work. Silicon Valley is the perfect test case: ten very different egos, all of whom occasionally deliver.

Not affiliated with HBO. Obviously.
