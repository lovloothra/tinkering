# tinkering

Utilities for tinkering with AI and compliance-related experiments.

## RBI Circular Quiz

`rbi_quiz.py` now contains a curated set of multiple-choice questions on topics from the Reserve Bank of India. A deterministic shuffle based on the current date selects a daily quiz for all players.

### Requirements

```
pip install -r requirements.txt
```

### Usage

```
python rbi_quiz.py
```

This prints a JSON array of quiz questions that can be consumed by a front-end or another service.

### Web Interface

A minimal Flask app serves a simple quiz UI with progress tracking and shareable results.

```
python app.py
```

Visit `http://localhost:8000` in your browser to play.
