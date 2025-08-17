import datetime
import json
import random
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List


@dataclass
class Question:
    id: str
    question: str
    options: List[str]
    correct_index: int
    difficulty: str


def load_question_bank(path: str = "rbi_questions.json") -> List[Question]:
    """Load pre-generated RBI quiz questions from a JSON file."""

    with open(Path(path), "r", encoding="utf-8") as f:
        data = json.load(f)
    return [Question(**q) for q in data]


QUESTIONS: List[Question] = load_question_bank()


def generate_quiz(num_questions: int = 10) -> List[Question]:
    random.seed(datetime.date.today().isoformat())
    sample = random.sample(QUESTIONS, k=min(num_questions, len(QUESTIONS)))
    return sample


def main() -> None:
    quiz = generate_quiz()
    data = [asdict(q) for q in quiz]
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
