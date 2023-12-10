from typing import Tuple, List, Dict
from dataclasses import dataclass

@dataclass
class Card:
    id: int
    winning_numbers: Tuple[int]
    card_numbers: Tuple[int]

    @property
    def idx(self):
        return self.id-1

    def score(self) -> int:
        return int(2**(self.matches()-1))
    
    def matches(self) -> int:
        return len(set(self.winning_numbers).intersection(set(self.card_numbers)))

cards: List[Card] = list()

f = open("4.txt")

for line in f.readlines():
    
    card_name , numbers = line.strip().split(':')
    
    _,card_id = card_name.split()

    winning_numbers_str,card_numbers_str = numbers.split('|')
    winning_numbers = tuple(int(n) for n in winning_numbers_str.split())
    card_numbers = tuple(int(n) for n in card_numbers_str.split())

    cards.append(Card(int(card_id),winning_numbers,card_numbers))

f.close()

print(sum(card.score() for card in cards))

card_worth = [1]*len(cards)

for card in reversed(cards):
    for addition_worth in range(card.matches()):
        card_worth[card.idx] += card_worth[card.idx+addition_worth+1]

print(sum(card_worth))