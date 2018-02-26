KEY = {'阴摩罗': 'AP', '心眼': 'AP', '鸣屋': 'AP', '狰': 'AP', '轮入道': 'AP', '蝠翼': 'AP',
       '镇墓兽': 'CR', '破势': 'CR', '伤魂鸟': 'CR', '网切': 'CR', '三味': 'CR', '针女': 'CR',
       '树妖': 'HP', '薙魂': 'HP', '钟灵': 'HP', '镜姬': 'HP', '被服': 'HP', '涅槃之火': 'HP', '地藏像': 'HP',
       '木魅': 'DP', '日女巳时': 'DP', '反枕': 'DP', '招财猫': 'DP', '雪幽魂': 'DP', '魅妖': 'DP', '珍珠': 'DP',
       '火灵': 'HR', '蚌精': 'HR', '魍魉之匣': 'DR', '返魂香': 'DR', '狂骨': 'AP', '幽谷响': 'DR', '骰子鬼': 'DR'}
VALUE = {'AP': 0.15, 'CR': 0.15, 'HP': 0.15, 'DP': 0.30,
         'HR': 0.15, 'DR': 0.15}


class Shishen:
    def __init__(self, name, attributes=None, type_names=None, target=None, level=40):
        self.name = name
        self.attributes = {'A': 0, 'H': 0, 'D': 0, 'CR': 0, 'CA': 0,
                           'HR': 0, 'DR': 0, 'S': 0}
        if attributes:
            self.attributes = attributes
        self.type_names = None
        if type_names:
            self.type_names = type_names
        self.target = target
        self.level = level
        self.yuhun_list = []
        self.final_attributes = self.attributes.copy()
        self.cost = 99999999
        if target:
            self.cost = self.target.get_cost(self.final_attributes)

    def set_yuhun_list(self, yuhun_list: []):
        self.yuhun_list = yuhun_list
        self.get_final_attributes()
        if self.target:
            self.cost = self.target.get_cost(self.final_attributes)

    def clear_yuhun_list(self):
        self.yuhun_list = []
        self.final_attributes = self.attributes.copy()
        if self.target:
            self.cost = self.target.get_cost(self.final_attributes)

    def get_final_attributes(self):
        yuhun_attributes = {'A': 0, 'AP': 0, 'H': 0, 'HP': 0, 'D': 0, 'DP': 0,
                            'CR': 0, 'CA': 0, 'HR': 0, 'DR': 0, 'S': 0}
        yuhun_name = {}
        for yuhun in self.yuhun_list:
            if yuhun.name in yuhun_name:
                yuhun_name[yuhun.name] += 1
            else:
                yuhun_name[yuhun.name] = 1
            for key, value in yuhun.attributes.items():
                yuhun_attributes[key] += value
        for name, number in yuhun_name.items():
            if number > 1:
                yuhun_attributes[KEY[name]] += VALUE[KEY[name]]
        for key, value in self.attributes.items():
            if key in ['A', 'H', 'D']:
                self.final_attributes[key] = value + value * yuhun_attributes[key + 'P'] + yuhun_attributes[key]
            else:
                self.final_attributes[key] = value + yuhun_attributes[key]
