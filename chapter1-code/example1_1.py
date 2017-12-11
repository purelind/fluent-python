import collections

#: 命名元组
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    #: 列表推导式
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamons clubs heart'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._card)

    def __getitem__(self, position):
        return self._cards[position]


