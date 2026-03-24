# Copilot Workspace Instructions for GildedRose-Refactoring-Kata

## Project purpose

This repository is a multi-language refactoring kata (Gilded Rose) with lots of language-specific starter implementations and tests. The usual goal is: keep behavior unchanged, add/adjust tests, refactor for clarity and design quality, then validate across one or more language directories.

## What an agent should know first

- The authoritative behavior is in `GildedRoseRequirements.md` (plus translations).
- The classic code smell is the old `GildedRose::update_quality` loop with string-based item names.
- The default failing test in many languages is the `"fixme" != "foo"` starter test.
- The scheme for this kata is: avoid full rewrite, do small refactor/test cycles, preserve semantics.

## Useful files

- `README.md` (general kata description, history, instructions).
- `CONTRIBUTING.md` (rules for translations and tests).
- language subdirs under root (`python/`, `Java/`, `c99/`, `ruby/`, etc.).
- `texttests/README.md` (approval test fixture details and TextTest setup).

## Build/test command pattern

There is no single top-level build system; each language folder may have its own. Agents should inspect the target language folder first.

Examples:

- Java: `cd Java && ./gradlew -q text` (and `./gradlew -q text --args 10` for days).
- C (c99): `cd c99 && make test`.
- C (cmocka): `cd c_cmocka && mkdir -p build && cd build && cmake .. && make && ctest`.
- Python: likely `cd python && pytest` (or `python -m pytest`).
- Ruby: `cd ruby && bundle exec rspec` or `bundle exec ruby <fixture>`.

When uncertain, refer to each `README.md` in language subdirs.

## Agent behavior guidelines

1. Ask the user to pick a language/target folder (unless explicit). If user just says "refactor logic", clarify their preferred language variant.
2. Always run tests before and after patches.
3. Keep change size small. The kata prioritizes incremental refactoring.
4. Preserve core requirements (quality decreases in normal items, `Aged Brie` increases, `Sulfuras` constant, `Backstage passes` rules, conjured optional extension).
5. When writing code, include a focused regression test in the same language conventions.

## Prompts worth suggesting

- "Help me refactor the Java Gilded Rose implementation; keep behavior stable and clean up updateQuality." 
- "In Python, add a unit test for Backstage passes 10 days or less and refactor the main loop." 
- "Find and fix any behavior drift in `c99` version after removing duplicated conditions." 

## Next customization ideas

- `/create-agent gildedrose-engineering` for the kata-specific agent with language templates and metamorphic test patterns.
- `/create-instruction gildedrose-testing` describing common test strategies and approval test workflow.
- `/create-prompt gildedrose-improve` with step-by-step refactor tasks.

---

> Note: follow the workspace-level rule from `CONTRIBUTING.md`: do not provide completed kata solutions as PRs to avoid spoiling exercise for others.
