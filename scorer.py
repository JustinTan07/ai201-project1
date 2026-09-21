def judge(question: str, expects: str, answer: str, results) -> bool:
    """Pass if the expected phrase appears in the answer (case-insensitive)."""
    return expects.lower() in answer.lower()