class StrKeyDict0(dict):
    def __missing__(self, key):
        #: check whether key is already a str. if it is, and it's missing
        #: raise KeyError.
        if isinstance(key, str):
            raise KeyEror(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default
    
    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()