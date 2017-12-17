import collections

#: 命名元组
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    #: 列表推导式
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


#: 设置排序权重
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    #: 当前card的大小索引值
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value*len(suit_values)+suit_values[card.suit]


