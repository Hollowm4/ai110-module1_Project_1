#FIX: Refactored logic into logic_utils.py using Claude Code).

def get_range_for_difficulty(difficulty: str): #Edit
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):  #Edit
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."
    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."
    return True, value, None


def check_guess(guess, secret):  #Edit
    """
    Compare guess to secret and return (outcome, message).

    ✅ Bug 1 fix: messages are now correctly directional.
       guess > secret → "Too High" → tell player to go LOWER
       guess < secret → "Too Low"  → tell player to go HIGHER
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"   # ✅ was incorrectly "Go HIGHER!"
        else:
            return "Too Low", "📈 Go HIGHER!"   # ✅ was incorrectly "Go LOWER!"
    except TypeError:
        g = str(guess)
        if g == str(secret):
            return "Win", "🎉 Correct!"
        if g > str(secret):
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"



def update_score(current_score: int, outcome: str, attempt_number: int, attempt_limit: int):  #Edit
    """
    Update score based on outcome and attempt number.

    ✅ Bug 3 fix: uses a proper linear formula so that:
       - Winning on attempt 1 of 8  → 100 points
       - Winning on attempt 4 of 8  → 62.5 points  (rounds to 63)
       - Winning on attempt 8 of 8  → minimum 10 points
       - Wrong guesses              → no score (floor at 0)
    """
    if outcome == "Win":
        points = 100 * (attempt_limit - attempt_number + 1) / attempt_limit
        points = max(10, round(points))   # minimum 10 so a late win still rewards
        return current_score + points

    if outcome in ("Too High", "Too Low"):
        return max(0, current_score - 5)  # floor at 0, never go negative

    return current_score
