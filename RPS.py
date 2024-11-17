def player(prev_play, opponent_history=[]):
    # Track the opponent's move history
    if prev_play:
        opponent_history.append(prev_play)

    # Counter mapping
    counter = {"R": "P", "P": "S", "S": "R"}
    moves = ["R", "P", "S"]

    # Default move for the first round
    if not opponent_history:
        return "R"

    # 1. Detect patterns (cyclic bot)
    def detect_cycle(history, pattern_length=3):
        """Detect repeating patterns in opponent history."""
        if len(history) < pattern_length * 2:
            return None
        recent_pattern = history[-pattern_length:]
        for i in range(len(history) - pattern_length * 2 + 1):
            if history[i:i + pattern_length] == recent_pattern:
                return history[i + pattern_length]
        return None

    # Try detecting shorter cycles (e.g., 2 or 3 moves)
    predicted_move = detect_cycle(opponent_history, pattern_length=2)
    if not predicted_move:
        predicted_move = detect_cycle(opponent_history, pattern_length=3)

    if predicted_move:
        return counter[predicted_move]

    # 2. Frequency-based prediction (most common move)
    move_counts = {move: opponent_history.count(move) for move in moves}
    most_common_move = max(move_counts, key=move_counts.get)

    # Predict the most common move and counter it
    prediction = most_common_move
    return counter[prediction]
