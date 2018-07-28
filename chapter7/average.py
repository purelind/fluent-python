class Averager():
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


def make_averager2():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager


def main():
    aver = make_averager()
    aver(3)
    aver(4)
    print(aver.__code__.co_varnames)
    print(aver.__code__.co_freevars)
    print(aver.__closure__)
    print(aver.__closure__[0].cell_contents)


if __name__ == '__main__':
    main()
