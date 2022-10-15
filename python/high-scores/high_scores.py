"""High Scores."""


class HighScores:
    """Manage a game player's High Score list."""

    def __init__(self, scores: list):
        """Initialize scores."""
        self.scores = scores

    def latest(self):
        """Return latest score."""
        return self.scores[-1]

    def personal_best(self):
        """Return best score."""
        return max(self.scores)

    def personal_top_three(self):
        """Return top 3 best scores."""
        return sorted(self.scores, reverse=True)[:3]
