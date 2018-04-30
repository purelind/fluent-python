import collections

class StrKeyDict(collections.UserDict):
    
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item

def main():
    skt = StrKeyDict()
    print(skt.keys())

if __name__ == '__main__':
    main()