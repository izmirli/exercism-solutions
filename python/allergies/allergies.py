class Allergies:
    """Person's allergies.

    Holds a person's allergies as a single score.
    Give access to getting his full allergies list, or checking
    if allergic to a single allergy.
    """
    ALRG = {
        'eggs': 1,
        'peanuts': 2,
        'shellfish': 4,
        'strawberries': 8,
        'tomatoes': 16,
        'chocolate': 32,
        'pollen': 64,
        'cats': 128,
    }

    def __init__(self, score: int):
        self.score = score

    def allergic_to(self, item: str) -> bool:
        """Is allergic to given allergy."""
        return item in self._lst

    @property
    def lst(self):
        """Return full allergies list."""
        return self._lst

    @property
    def score(self):
        """Get person's allergies score."""
        return self._score
    
    @score.setter
    def score(self, score: int):
        """Set allergies score + gnerate & set allergies list."""
        self._score = score
        self._lst = [a for a in self.ALRG if self._score & self.ALRG[a]]
