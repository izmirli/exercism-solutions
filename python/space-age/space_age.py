"""Space Age."""
EARTH_SECONDS = 60 * 60 * 24 * 365.25
PLANET_RATIOS = {
    'mercury': 0.2408467,
    'venus': 0.61519726,
    'earth': 1.0,
    'mars': 1.8808158,
    'jupiter': 11.862615,
    'saturn': 29.447498,
    'uranus': 84.016846,
    'neptune': 164.79132
}


class SpaceAge:
    """Ages in Space - access age value on each planet."""

    def __init__(self, seconds: int):
        self.age = seconds

    def __getattr__(self, item: str):
        if not item.startswith("on_") or item.removeprefix("on_") not in PLANET_RATIOS:
            raise AttributeError(f"{item} is not a valid attribute.")
        planet = item.removeprefix("on_")
        return lambda planet = planet: round(self.age / (EARTH_SECONDS * PLANET_RATIOS[planet]), 2)
