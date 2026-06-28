def classify_document(text):

    text = text.lower()

    if any(word in text for word in [
        "incident",
        "incident report",
        "root cause",
        "corrective action"
    ]):
        return "incident_report"

    elif any(word in text for word in [
        "failure",
        "failure analysis",
        "breakdown"
    ]):
        return "failure_report"

    elif any(word in text for word in [
        "audit",
        "non-conformance",
        "compliance",
        "inspection finding"
    ]):
        return "audit_report"

    elif any(word in text for word in [
        "maintenance",
        "lubrication",
        "inspection schedule",
        "preventive maintenance"
    ]):
        return "maintenance"

    elif any(word in text for word in [
        "standard operating procedure",
        "sop",
        "procedure"
    ]):
        return "sop"

    elif any(word in text for word in [
        "manual",
        "installation",
        "operating instructions"
    ]):
        return "manual"

    return "other"