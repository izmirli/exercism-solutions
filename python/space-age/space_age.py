class SpaceAge:
    """Ages in Space - queiq access age on each planet.

    Orbital period on Earth is 31,557,600 seconds (365.25 days).
    """
    
    def __init__(self, seconds: int):
        self.age = seconds

    def how_old(self, orbital_period: float) -> float:
        """Calculate age on a planet with the given orbital period.
        
        :param orbital_period: the orbital period in earth years
        :return: how old on planet (rounded to 2 decimals)
        """
        return round(self.age / (31_557_600 * orbital_period), 2)

    def on_earth(self) -> float:
        return self.how_old(1)

    def on_mercury(self) -> float:
        return self.how_old(0.2408467)

    def on_venus(self) -> float:
        return self.how_old(0.61519726)

    def on_mars(self) -> float:
        return self.how_old(1.8808158)

    def on_jupiter(self) -> float:
        return self.how_old(11.862615)

    def on_saturn(self) -> float:
        return self.how_old(29.447498)

    def on_uranus(self) -> float:
        return self.how_old(84.016846)

    def on_neptune(self) -> float:
        return self.how_old(164.79132)
