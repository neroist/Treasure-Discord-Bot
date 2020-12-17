class Player:
    """Represents a player object"""

    def __init__(self, name, **kwargs):
        self.name = name
        self.attrs = kwargs

    def __str__(self):
        return self.name

    def __getitem__(self, item):
        return getattr(self, item)

    def __bool__(self):
        return True

    def changeName(self, name):
        self.name = name

    def changeAttr(self, attr: str, value):
        self.attrs[attr] = value

    def delAttr(self, attr: str):
        del self.attrs[attr]

    def addAttr(self, attr: str, value):
        self.attrs.update({attr: value})

    def getAttrs(self):
        return self.attrs

    def getAttr(self, attr: str):
        return self.attrs[attr]

    def getName(self):
        return self.name
