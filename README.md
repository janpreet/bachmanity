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

```
> be gilfoyle and fix the failing test

Fine. I'll look at your build. Lower your expectations to zero and I may
exceed them.
```

## What these will not do

- Quote the show verbatim. Each skill generates fresh material in the voice, so it holds up past the third response.
- Put persona text anywhere that outlives the conversation. Commit messages, code comments and file contents are written straight.
- Lie about results. Failures get spun, never hidden. Every skill has this rule at the top and it outranks the bit.
- Keep the bit going when things are actually on fire. They read the room and dial down.
- Profanity. The show is crude, these are not. The characters carry it without the language.

## Why

I wanted to see if persona skills could be funny without getting in the way of real work. Silicon Valley is the perfect test case: ten very different egos, all of whom occasionally deliver.

Not affiliated with HBO. Obviously.
