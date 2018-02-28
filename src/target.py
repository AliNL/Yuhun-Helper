class Target:
    def __init__(self, values_and_weights: {}):
        self.values_and_weights = {'A': 15000, 'AW': 0.1, 'H': 40000, 'HW': 0.1, 'D': 2000, 'DW': 0.1,
                                   'CR': 1, 'CRW': 0.1, 'CA': 4.5, 'CAW': 0.1, 'HR': 1.4, 'HRW': 0.1,
                                   'DR': 2, 'DRW': 0.1, 'S': 360, 'SW': 0.1}
        self.set_values_and_weights(values_and_weights)

    def set_values_and_weights(self, values_and_weights):
        for key, value in values_and_weights.items():
            self.values_and_weights[key] = value

    def get_cost(self, attributes):
        cost = 0
        for key, value in attributes.items():
            if self.values_and_weights[key]:
                error = abs(1 - value / self.values_and_weights[key])
                cost += error * self.values_and_weights[key + 'W']
        return cost
