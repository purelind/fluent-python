class DoppeDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


if __name__ == '__main__':
    dd = DoppeDict(one=1)
    print(dd)
    dd["two"] = 2
    print(dd)
    dd.update(threee=3)
    print(dd)
