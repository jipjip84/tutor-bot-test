# Harvest Ledger

A farm-themed study companion for *Principles of Management* (LibreTexts).

- **8 weeks, 2 chapters a week.** Mon–Tue cover the first chapter, Wed–Thu the second, and Friday mixes both. Saturday is a Market Day quiz and Sunday is a fallow (rest) day.
- **160 seed-packet flash cards.** Each card has an illustration, the textbook definition with its section number, and an "On the farm" example. Browse back and forth and flip as often as you like; the Card barn tab lets you flip through every card, filtered by week or shuffled.
- **You decide when a day is done, and you can work ahead.** Press "Mark lesson complete" to log a lesson, then "Keep going" to jump to the next unfinished one.
- **Milestones.** Each finished week (all five lessons, plus 80% or better on Market Day) builds something on your farm: a barn, hens, a tractor, a silo, cows, beehives, an orchard, and finally the farmhouse. You also earn ribbons for streaks, cards harvested, perfect quizzes and greenhouse reviews.

- **Sound, video and interactive extras.**
  - Farm sound effects, with a Sound on/off switch.
  - "Read aloud" on every card.
  - "Watch it grow" animated diagrams for 11 key models (P-O-L-C, the control process, Lewin, Tuckman, Maslow, the five forces and more).
  - "Find a video" links to YouTube searches.
  - An AI "farm tutor" for follow-up questions, which uses Claude when the page is opened as a claude.ai artifact.
  - A Field games tab: chapter sorting, P-O-L-C sorting, type-the-term and farm scenario questions.

## Files

- `src/course.py`: all course content (weeks, days, cards). Edit this to change cards.
- `src/app.html`: the app (layout, illustrations, logic).
- `build.py`: inlines the course into the app and writes `tutorbot.html`.

```sh
python3 build.py
```

Open `tutorbot.html` in a browser. Progress saves in the browser, or to your account when it's opened as a claude.ai artifact.
