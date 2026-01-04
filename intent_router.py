def detect_intent(query: str):
    q = query.lower()

    if any(x in q for x in ["study plan", "schedule", "prepare"]):
        return "STUDY_PLAN"

    if any(x in q for x in ["quiz", "test", "mcq", "questions"]):
        return "QUIZ"

    if any(x in q for x in ["what is", "explain", "define", "why", "how"]):
        return "CONCEPT"

    return "GENERAL"
