def normalize_status(indicator: str) -> str:
    indicator = indicator.lower()

    if indicator in ["none", "operational"]:
        return "OPERATIONAL"
    if indicator in ["minor", "degraded"]:
        return "DEGRADED"
    return "DOWN"
