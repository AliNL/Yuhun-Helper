import csv

from src.shishen import Shishen
from src.yuhun import Yuhun

SELECTION = [[2, 3, 4, 5],
             [1, 3, 4, 5],
             [1, 2, 4, 5],
             [1, 2, 3, 5],
             [1, 2, 3, 4],
             [0, 3, 4, 5],
             [0, 2, 4, 5],
             [0, 2, 3, 5],
             [0, 2, 3, 4],
             [0, 1, 4, 5],
             [0, 1, 3, 5],
             [0, 1, 3, 4],
             [0, 1, 2, 5],
             [0, 1, 2, 4],
             [0, 1, 2, 3]]


class Helper:
    def __init__(self):
        self.yuhun_store = []
        self.read_yuhun_store()
        self.shishen_store = {}
        self.read_shishen_list()

    def read_yuhun_store(self):
        with open('yuhun.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                yuhun = Yuhun(row.pop('Name'), int(row.pop('Position')))
                attributes = {key: float(value) for key, value in row.items() if value}
                yuhun.set_attributes(attributes)
                self.yuhun_store.append(yuhun)

    def read_shishen_list(self):
        with open('shishen.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                shishen = Shishen(row.pop('Name'))
                type_names = row.pop('Types')
                shishen.type_name = type_names.split('/')
                attributes = {key: float(value) for key, value in row.items()}
                attributes['HR'] = 0.0
                attributes['DR'] = 0.0
                shishen.attributes = attributes
                self.shishen_store[shishen.name] = shishen

    def find_best_solution_for(self, shishen, n=3):
        best_n_list = {}
        shishen.clear_yuhun_list()
        all_needed = {0, 1, 2, 3, 4, 5}
        yuhun_needed = [[], [], [], [], [], []]
        for yuhun in self.yuhun_store:
            if not shishen.type_name or yuhun.name == shishen.type_name:
                yuhun_needed[yuhun.position - 1].append(yuhun)
        for i in range(15):
            s = SELECTION[i]
            available = True
            other = list(all_needed - set(s))
            for j in s:
                if not yuhun_needed[j]:
                    available = False
                    break
            if not available:
                continue
            for yuhun_1 in yuhun_needed[s[0]]:
                for yuhun_2 in yuhun_needed[s[1]]:
                    for yuhun_3 in yuhun_needed[s[2]]:
                        for yuhun_4 in yuhun_needed[s[3]]:
                            for yuhun_5 in [yh for yh in self.yuhun_store if yh.position == other[0] + 1]:
                                for yuhun_6 in [yh for yh in self.yuhun_store if yh.position == other[1] + 1]:
                                    shishen.clear_yuhun_list()
                                    shishen.set_yuhun_list([yuhun_1, yuhun_2, yuhun_3, yuhun_4, yuhun_5, yuhun_6])
                                    best_n_list[shishen.cost] = shishen.yuhun_list[:]
                                    if len(best_n_list) > n:
                                        max_cost = 0
                                        for key in best_n_list:
                                            max_cost = key if key > max_cost else max_cost
                                        best_n_list.pop(max_cost)
        return best_n_list
