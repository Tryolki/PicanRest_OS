class Star(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __json__(self):
        return dict(
            name=self.name,
            weight=self.weight
        )

    def __repr__(self):
        return "Star(%s, %s)" % (
            self.name,
            self.weight
        )
