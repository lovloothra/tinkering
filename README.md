# tinkering

Utilities for tinkering with AI and compliance-related experiments.

## RBI Circular Quiz

`rbi_quiz.py` scrapes the Reserve Bank of India circular index and
builds a daily multiple-choice quiz of ten questions. Each question asks
for the issue date of a circular and includes four options. The quiz is
seeded by the current date so all players see the same questions each
day.

### Requirements

```
pip install -r requirements.txt
```

### Usage

```
python rbi_quiz.py
```

This prints a JSON array of ten questions that can be consumed by a
front-end or another service.
