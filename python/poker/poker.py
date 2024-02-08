"""Poker exercise.

Pick the best hand(s) from a list of poker hands.
See wikipedia for an overview of poker hands...

https://exercism.org/tracks/python/exercises/poker
"""
from operator import lt, le, eq, ne, ge, gt
from collections import Counter
from enum import IntEnum
from typing import Callable

CARD_VALUES = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
               "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
HANDS = IntEnum(
    'HandRanking',
    ['HIGH_CARD', 'ONE_PAIR', 'TWO_PAIR', 'THREE_OF_A_KIND', 'STRAIGHT',
     'FLUSH', 'FULL_HOUSE', 'FOUR_OF_A_KIND', 'STRAIGHT_FLUSH']
)


class PokerHand:
    """A comparable Poker hand."""

    def __init__(self, hand: str) -> None:
        self.hand = hand
        self.cards: list[tuple] | None = None
        self.cards_ranks: list[int] | None = None
        self.cards_suits: list[str] | None = None
        self.hand_rank: dict[str, IntEnum | list[int]] | None = None
        self.process_hand()

    def process_hand(self) -> None:
        """Process hand to set its data and enable comparison with other hands."""
        cards = sorted(
            [(card[:-1], card[-1]) for card in self.hand.split()],
            key=lambda x: CARD_VALUES[x[0]],
            reverse=True
        )
        if len(cards) != 5:
            raise ValueError(f"PokerHand should have 5 cards, but found {len(cards)} instead")

        self.cards = cards
        self.cards_ranks = [CARD_VALUES[c[0]] for c in cards]
        self.cards_suits = [c[1] for c in cards]

        rank_counter = Counter(self.cards_ranks)
        most_common = rank_counter.most_common()
        if self.is_straight():
            if self.is_flush():
                self.hand_rank = {'rank': HANDS.STRAIGHT_FLUSH, 'tie': [self.cards_ranks[0]]}
            else:
                self.hand_rank = {'rank': HANDS.STRAIGHT, 'tie': [self.cards_ranks[0]]}
        elif self.is_flush():
            self.hand_rank = {'rank': HANDS.FLUSH, 'tie': self.cards_ranks}
        elif most_common[0][1] == 4:
            self.hand_rank = {'rank': HANDS.FOUR_OF_A_KIND, 'tie': [most_common[0][0], most_common[1][0]]}
        elif most_common[0][1] == 3:
            if most_common[1][1] == 2:
                self.hand_rank = {'rank': HANDS.FULL_HOUSE, 'tie': [most_common[0][0], most_common[1][0]]}
            else:
                self.hand_rank = {'rank': HANDS.THREE_OF_A_KIND, 'tie': [
                    most_common[0][0], *[c for c in self.cards_ranks if c != most_common[0][0]]
                ]}
        elif most_common[0][1] == 2:
            if most_common[1][1] == 2:
                self.hand_rank = {'rank': HANDS.TWO_PAIR, 'tie': [most_common[0][0], most_common[1][0], most_common[2][0]]}
            else:
                self.hand_rank = {'rank': HANDS.ONE_PAIR, 'tie': [
                    most_common[0][0], *[c for c in self.cards_ranks if c != most_common[0][0]]
                ]}
        else:
            self.hand_rank = {'rank': HANDS.HIGH_CARD, 'tie': self.cards_ranks}

    def is_flush(self) -> bool:
        """Check if all hand's cards are of the same suit."""
        return len(set(self.cards_suits)) == 1

    def is_straight(self) -> bool:
        """Check if it's a hand that contains five cards of sequential rank."""
        if self.cards_ranks == [14, 5, 4, 3, 2]:
            self.cards_ranks = [5, 4, 3, 2, 1]
            return True
        return self.cards_ranks[::-1] == list(range(self.cards_ranks[-1], self.cards_ranks[-1] + 5))

    def compare(self, other: 'PokerHand', op: Callable[[int, int], bool]) -> bool:
        """Compare of two Poker hands by given operator according to Poker rules.

        :param other: the Poker hands to compare to
        :param op: the operator to compare by
        :return: True if compared as expected by operator, False otherwise
        """
        if self.hand_rank['rank'] == other.hand_rank['rank']:
            for this_card, other_card in zip(self.hand_rank['tie'], other.hand_rank['tie']):
                if this_card == other_card:
                    continue
                else:
                    return op(this_card, other_card)
        return op(self.hand_rank['rank'], other.hand_rank['rank'])

    def __lt__(self, other: 'PokerHand') -> bool:
        """Poker hands less than."""
        return self.compare(other, lt)

    def __le__(self, other: 'PokerHand') -> bool:
        """Poker hands less than or equal to."""
        return self.compare(other, le)

    def __eq__(self, other: 'PokerHand') -> bool:
        """Poker hands equal."""
        return self.compare(other, eq)

    def __ne__(self, other: 'PokerHand') -> bool:
        """Poker hands not equal."""
        return self.compare(other, ne)

    def __ge__(self, other: 'PokerHand') -> bool:
        """Poker hands greater than or equal to."""
        return self.compare(other, ge)

    def __gt__(self, other: 'PokerHand') -> bool:
        """Poker hands greater than."""
        return self.compare(other, gt)

    def __repr__(self) -> str:
        """Represent object's main data."""
        return (f"cards: {self.hand}; rank: [{self.hand_rank['rank'].value}] {self.hand_rank['rank'].name}; "
                f"tie: {self.hand_rank['tie']};")


def best_hands(hands: list[str]) -> list[str]:
    """Get best hands, out of given hands, according to Poker rules."""
    the_best_hands: list[PokerHand] | None = None
    for hand in hands:
        this_hand = PokerHand(hand)
        if the_best_hands is None or this_hand > the_best_hands[0]:
            the_best_hands = [this_hand]
        elif this_hand == the_best_hands[0]:
            the_best_hands.append(this_hand)

    return [hand.hand for hand in the_best_hands]


if __name__ == '__main__':
    """Print test cases."""
    print(f"{PokerHand('4S 5S 7S 8S 6S')=}")
    print(f"{PokerHand('2S KS 2H 2D 2C')=}")
    print(f"{PokerHand('2S KS 2H 2D KC')=}")
    print(f"{PokerHand('AS 5S 7S 8S JS')=}")
    print(f"{PokerHand('AS KS QH JD 10C')=}")
    print(f"{PokerHand('4S AH 3S 2D 5H')=}")
    print(f"{PokerHand('2S 7S 2H 2D QC')=}")
    print(f"{PokerHand('6S 5S 6H 9D 5C')=}")
    print(f"{PokerHand('AS 5S AH 8D JC')=}")
    print(f"{PokerHand('AS 5S 7H 8D JC')=}")

    pair1 = PokerHand('2S KS 3H 2D 3C')
    pair2 = PokerHand('3S 4S 2H 3D 2C')
    print(f"\n{pair1=}\n{pair2=}")
    print(f"{pair1 == pair2=}")
    print(f"{pair1 > pair2=}")
    print(f"{pair1 < pair2=}")
    print(f"{pair1 >= pair2=}")
    print(f"{pair1 <= pair2=}")
    print(f"{pair1 != pair2=}")

    print()
    print(f'{best_hands(["KS AH AS AD AC", "4H AH 3H 2H 5H"])=}')

    print()
    hnds = ["4D 5S 6S 8D 3C", "2S 4C 7S 9H 10H", "3S 4S 5D 6H JH", "3H 4H 5C 6C JD"]
    for i, hnd in enumerate(hnds):
        print(f"  {i}) {PokerHand(hnd)=}")
    print(f'{best_hands(hnds)=}')
