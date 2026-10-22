"""Verdict normalization and recovery, shared by the report writer and the release redactor.

Kept in its own module so `redact_release.py` can replay the recovery step without
importing the plotting stack that `report.py` pulls in.
"""
import json
import re


def normalize_bool_verdict(value):
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        lowered = value.strip().lower()
        if lowered == "true":
            return True
        if lowered == "false":
            return False
    return None


def recover_verdict_from_raw_response(raw_response):
    """
    Recover is_correct from JSON-like verifier responses that failed strict parsing,
    commonly because LaTeX backslashes such as \\( or \\kappa are invalid JSON escapes.
    """
    if not raw_response:
        return None

    text = str(raw_response).strip()

    try:
        parsed = json.loads(text)
        return normalize_bool_verdict(parsed.get("is_correct"))
    except Exception:
        pass

    matches = re.findall(
        r'["\']?is_correct["\']?\s*[:=]\s*["\']?(true|false)["\']?',
        text,
        flags=re.IGNORECASE,
    )

    if not matches:
        return None

    unique = {match.lower() for match in matches}
    if len(unique) > 1:
        return None

    return matches[-1].lower() == "true"
