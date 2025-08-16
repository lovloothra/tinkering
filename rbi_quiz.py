import datetime
import json
import random
from dataclasses import dataclass, asdict
from typing import List


@dataclass
class Question:
    id: str
    question: str
    options: List[str]
    correct_index: int
    difficulty: str


QUESTIONS: List[Question] = [
    Question(
        id="Q1",
        question="What is the current repo rate as per latest RBI monetary policy?",
        options=["6.5%", "7.0%", "6.25%", "6.75%"],
        correct_index=0,
        difficulty="Easy",
    ),
    Question(
        id="Q2",
        question="What is the minimum Net Worth requirement for Payment Aggregators?",
        options=["₹15 crore", "₹25 crore", "₹50 crore", "₹100 crore"],
        correct_index=0,
        difficulty="Medium",
    ),
    Question(
        id="Q3",
        question="Which committee is responsible for setting the policy repo rate in India?",
        options=[
            "Monetary Policy Committee",
            "Securities and Exchange Board",
            "Financial Stability and Development Council",
            "NITI Aayog",
        ],
        correct_index=0,
        difficulty="Easy",
    ),
    Question(
        id="Q4",
        question="What does CRR stand for in banking terminology?",
        options=[
            "Cash Reserve Ratio",
            "Credit Risk Rating",
            "Capital Requirement Ratio",
            "Current Repo Rate",
        ],
        correct_index=0,
        difficulty="Medium",
    ),
    Question(
        id="Q5",
        question="Which retail payment system is operated by NPCI?",
        options=["UPI", "NEFT", "RTGS", "SWIFT"],
        correct_index=0,
        difficulty="Medium",
    ),
    Question(
        id="Q6",
        question="What is the main purpose of the Standing Deposit Facility (SDF)?",
        options=[
            "To absorb excess liquidity without providing collateral",
            "To provide long-term loans to small industries",
            "To facilitate foreign exchange transactions",
            "To insure bank deposits",
        ],
        correct_index=0,
        difficulty="Hard",
    ),
]


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
