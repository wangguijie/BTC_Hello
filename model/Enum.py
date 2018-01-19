
class Enum(set):
    def __getattr__(self, item):
        if item in self:
            return item.lower()
        raise AttributeError