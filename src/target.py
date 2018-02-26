class Target:
    def __init__(self, values_and_weights: {}):
        self.values_and_weights = {'A': 0, 'AW': 0, 'H': 0, 'HW': 0, 'D': 0, 'DW': 0,
                                   'CR': 0, 'CRW': 0, 'CA': 0, 'CAW': 0, 'HR': 0, 'HRW': 0,
                                   'DR': 0, 'DRW': 0, 'S': 0, 'SW': 0}
        self.set_values_and_weights(values_and_weights)

    def set_values_and_weights(self, values_and_weights):
        for key, tup in values_and_weights.items():
            value, weight = tup
            self.values_and_weights[key] = value
            self.values_and_weights[key + 'W'] = weight

    def get_cost(self, attributes):
        cost = 0
        for key, value in attributes.items():
            error = (self.values_and_weights[key] - value) ** 2
            cost += error * self.values_and_weights[key + 'W']
        return cost
