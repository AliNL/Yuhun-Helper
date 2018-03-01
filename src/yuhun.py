class Yuhun:
    def __init__(self, name, position, attributes=None, stars=6, level=15):
        super().__init__()
        if attributes is None:
            attributes = {}
        self.name = name
        self.position = position
        self.stars = stars
        self.level = level
        self.attributes = {'A': 0, 'AP': 0, 'H': 0, 'HP': 0, 'D': 0, 'DP': 0,
                           'CR': 0, 'CA': 0, 'HR': 0, 'DR': 0, 'S': 0}
        self.set_attributes(attributes)
        self.shishen = None

    def set_attributes(self, attributes: {}):
        for key, value in attributes.items():
            self.attributes[key] = value

    def set_level(self, level):
        self.level = level

    def get_dict(self):
        this_dict = {key: value for key, value in self.attributes.items() if value}
        this_dict['Name'] = self.name
        this_dict['Position'] = self.position
        return this_dict
