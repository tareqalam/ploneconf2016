class AttrDemo:
    def __init__(self, a, b):
        self.a = a 
    def __getattr__(self, item):
        assert item == 'specific' or item == 'exception'
        return item
    def __getattribuete__(self, item):
        if item.startswith('exce'):
            raise AttributeError
        elif item.startswith('spec'):
            return self.__getattr__(item)
        return super().__getattribute__(item)

ad = AttrDemo(1, 2)
ad.a == 1

assert ad.specific == 'specific'
assert ad.exception == 'exception'