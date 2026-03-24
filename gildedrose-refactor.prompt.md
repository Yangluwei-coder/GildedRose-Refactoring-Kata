# Gilded Rose Refactor Prompt

## Summary
Use this prompt when you want an AI assistant to help you implement a small, behavior-preserving refactor in one of the languages in `GildedRose-Refactoring-Kata`, with a focused regression test and pass/fail verification.

## Instructions for the assistant

You are a coding assistant for the Gilded Rose kata.

1. Ask the user to pick a target language folder (e.g., `Java`, `python`, `c99`, `ruby`) if they haven't specified it yet.
2. Discover the current failing test in that folder (usually the starter test with `fixme` or equivalent).
3. Run the existing test suite (or suggested command by language README) and capture baseline results.
4. Identify the current implementation of the core behavior (`update_quality`, `updateQuality`, or equivalent) and the matching unit test file.
5. Apply a small refactor (few lines, structural clarity) while preserving behavior. Do not rewrite from scratch.
6. Add or update a focused regression test for one of these cases:
   - Normal item: quality decreases by 1 before sell date, by 2 after.
   - `Aged Brie`: quality increases.
   - `Sulfuras`: no change.
   - `Backstage passes`: +2 at 10 days or less, +3 at 5 days or less, drops to 0 after.
7. Run tests again and verify pass.
8. Provide a concise before/after summary and new regression assertion.

## Usage example

Prompt: 
"Use `gildedrose-refactor.prompt.md` to refactor Java code so `updateQuality` no longer uses a nested `if` chain, while preserving behavior. Add a test for backstage passes within 10 days."

## Notes

- Reference `GildedRoseRequirements.md` for acceptance rules.
- Follow repository guidance from `CONTRIBUTING.md`: don't produce an overall kata solution in one go.
- Keep final code change minimal and easy to review.
