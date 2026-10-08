import re


def analyze_code(code, error_message=""):
    issues = []
    suggestions = []

    if not code.strip():
        return {
            "status": "No code provided",
            "issues": [],
            "suggestions": []
        }

    # Detect common Python issues
    if re.search(r"print\s+[^(]", code):
        issues.append("Possible Python print syntax issue.")
        suggestions.append("Use print() with parentheses.")

    if "==" not in code and "=" in code:
        suggestions.append(
            "Check whether you are using = for assignment "
            "where == comparison is required."
        )

    if error_message:
        error_lower = error_message.lower()

        if "syntaxerror" in error_lower:
            issues.append("Python syntax error detected.")
            suggestions.append(
                "Check brackets, colons, indentation, and syntax."
            )

        if "nameerror" in error_lower:
            issues.append("A variable or function may be undefined.")
            suggestions.append(
                "Check spelling and make sure the variable or function "
                "is defined before use."
            )

        if "typeerror" in error_lower:
            issues.append("There may be an incompatible data type.")
            suggestions.append(
                "Check the types of the values used in the operation."
            )

        if "indexerror" in error_lower:
            issues.append("A list or sequence index may be out of range.")
            suggestions.append(
                "Check the list length and the index being accessed."
            )

        if "indentationerror" in error_lower:
            issues.append("Python indentation problem detected.")
            suggestions.append(
                "Check spaces and indentation levels."
            )

    if not issues:
        issues.append("No obvious common issue detected.")
        suggestions.append(
            "Review the error message and test the code step by step."
        )

    return {
        "status": "Analysis completed",
        "issues": issues,
        "suggestions": suggestions
    }
