def grade_bump(gradebook: dict[str, str], student: str) -> None:
    if gradebook[student] == "A":
        gradebook[student] = "A+"
    else:
        gradebook[student] = "A"


grades: dict[str, str] = {"alyssa": "A", "luke": "B"}
