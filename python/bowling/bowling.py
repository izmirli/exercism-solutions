"""Bowling exercise."""


class BowlingGame:
    def __init__(self):
        self.frames: list[list[int]] = [[]]

    def roll(self, pins: int) -> None:
        """

        """
        current_frame = len(self.frames)
        if not 0 <= pins <= 10:
            raise ValueError(f"Pins value mast be 0-10, but got: {pins}.")
        if sum(self.frames[current_frame - 1]) + pins > 10:
            raise ValueError(
                f"Invalid 2nd throw - both throws can have up to 10 pins knocked down, "
                f"but 1st was: {self.frames[current_frame - 1][0]} "
                f"& 2nd was: {self.frames[current_frame - 1][1]}."
            )
        if current_frame > 10:
            if sum(self.frames[9]) != 10:
                raise ValueError("cannot throw bonus with an open tenth frame")
            if len(self.frames[9]) == 2 and (current_frame >= 12 or len(self.frames[10])):
                raise ValueError("Tenth frame is spare, no more than one bonus throw.")
            if current_frame > 12 or current_frame == 12 and self.frames[10][0] != 10:
                raise ValueError("Cannot roll after bonus rolls for strike.")

        self.frames[current_frame - 1].append(pins)
        if pins == 10 or len(self.frames[current_frame - 1]) == 2:
            self.frames.append([])

    def score(self) -> int:
        """Calculate the total score for that game."""
        if len(self.frames) < 10:
            raise UserWarning(f"Game mast have at least 10 frames - incomplete game cannot be scored.")
        total = 0
        for frame_index, frame_rolls in enumerate(self.frames):
            if frame_index > 9:
                break
            round_rolls_sum = sum(frame_rolls)
            total += round_rolls_sum
            if round_rolls_sum == 10:
                total += self.frames[frame_index + 1][0]
                if len(frame_rolls) != 2:
                    total += self.frames[frame_index + 1][1] if len(self.frames[frame_index + 1]) == 2 \
                        else self.frames[frame_index + 2][0]

        return total
