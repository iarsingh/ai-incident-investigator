TOOLS = ["timeline", "hypothesize"]
WRITES = ("declare sevs", "page",)


class InputError(ValueError):
    pass


def run(goal, payload):
    if not isinstance(goal, str) or not goal.strip():
        raise InputError("goal is empty")
    if any(word in goal.lower() for word in WRITES):
        return {"refused": True, "reason": "This agent only reads or plans. It does not write.", "tools": [], "wrote": False, "applied": False}
    facts = " ".join(payload.get("facts") or []).lower(); result = "bad_deploy" if "rollout" in facts else "saturation" if "cpu" in facts else "unknown"
    return {"refused": False, "tools": TOOLS, "hypothesis": result, "wrote": False, "applied": False}
