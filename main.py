# coding=utf-8

from appJar import gui

from src.helper import Helper
from src.target import Target

TUHUN_TYPES = ['- -  无  - -', '阴摩罗', '心眼', '鸣屋', '狰', '轮入道', '蝠翼',
               '镇墓兽', '破势', '伤魂鸟', '网切', '三味', '针女',
               '树妖', '薙魂', '钟灵', '镜姬', '被服', '涅槃之火', '地藏像',
               '木魅', '日女巳时', '反枕', '招财猫', '雪幽魂', '魅妖', '珍珠',
               '火灵', '蚌精', '魍魉之匣', '返魂香', '狂骨', '幽谷响', '骰子鬼']
ATTRIBUTES = {'A': '攻击', 'H': '生命', 'D': '防御', 'S': '速度', 'CR': '暴击', 'CA': '暴击伤害', 'HR': '效果命中', 'DR': '效果抵抗'}
YUHUN_ATTRIBUTES = {'A': '攻击', 'AP': '攻击加成', 'H': '生命', 'HP': '生命加成', 'D': '防御', 'DP': '防御加成',
                    'CR': '暴击', 'CA': '暴击伤害', 'HR': '效果命中', 'DR': '效果抵抗', 'S': '速度'}
MAX_VALUES = {'A': 15000, 'H': 40000, 'D': 2000, 'CR': 1, 'CA': 4.5, 'HR': 1.4, 'DR': 1.4, 'S': 360}
KEY_ORDER = ['A', 'CR', 'CA', 'S', 'H', 'D', 'DR', 'HR']


def draw_radar_template(canvas, x, y):
    canvas.create_oval(x + 20, y + 20, x + 130, y + 130, outline='#DDDDDD', width=1)
    canvas.create_line(x + 75, y + 20, x + 75, y + 130, width=1)
    canvas.create_line(x + 20, y + 75, x + 130, y + 75, width=1)
    canvas.create_line(x + 36.11, y + 36.11, x + 113.89, y + 113.89, width=1)
    canvas.create_line(x + 36.11, y + 113.89, x + 113.89, y + 36.11, width=1)
    canvas.create_text(x + 75, y + 12, text='攻击')
    canvas.create_text(x + 125, y + 28, text='暴击')
    canvas.create_text(x + 138, y + 68, text='暴')
    canvas.create_text(x + 138, y + 82, text='伤')
    canvas.create_text(x + 125, y + 122, text='速度')
    canvas.create_text(x + 75, y + 138, text='生命')
    canvas.create_text(x + 25, y + 122, text='防御')
    canvas.create_text(x + 12, y + 68, text='抵')
    canvas.create_text(x + 12, y + 82, text='抗')
    canvas.create_text(x + 25, y + 28, text='命中')


def draw_radar_with_percentage(canvas, x, y, percentage_list):
    mid_x, mid_y = x + 75, y + 75
    canvas.delete('all')
    max_points = [(75, 20), (113.89, 36.11), (130, 75), (113.89, 113.89), (75, 130), (36.11, 113.89), (20, 75),
                  (36.11, 36.11)]
    result = []
    for i in range(len(KEY_ORDER)):
        p = percentage_list[KEY_ORDER[i]]
        this_x = (x + max_points[i][0]) * p + mid_x * (1 - p)
        this_y = (y + max_points[i][1]) * p + mid_y * (1 - p)
        result.append(this_x)
        result.append(this_y)

    canvas.create_polygon(*result, fill='#8888EE', outline="#6666FF")
    draw_radar_template(canvas, x, y)


class Window:
    def __init__(self, shishen_store):
        self.s = shishen_store
        self.canvas_x = 50
        self.canvas_y = 10
        self.target_shishen = None
        self.app = gui('御魂方案计算器', '900x400')
        self.app.startLabelFrame("目标设置", 0, 0, 1, 1)
        self.app.addLabel('shishen', '式神名称', 0, 0)
        option_list = list(shishen_store.keys())
        option_list.append('- -  空  - -')
        self.app.addOptionBox('shishen', option_list, 0, 1, 1, 1)
        self.app.setOptionBox('shishen', len(option_list) - 1, override=True)
        self.app.setOptionBoxChangeFunction('shishen', self.get_init_attributes)
        self.app.addLabel('weight', '属性权重', 0, 2, 2, 1)
        next_row = self.add_attribute_labels(ATTRIBUTES, 1, 0)
        self.add_weight_scales(ATTRIBUTES, 1, 2)
        self.app.addLabel('types', '四件套', next_row, 0, 1, 1)
        self.app.addOptionBox('types', TUHUN_TYPES, next_row, 1, 1, 1)
        self.app.addNamedButton('确定', 'ok', self.start, next_row, 2, 1, 1)
        self.app.addLabel('result', '', next_row, 3, 1, 1)
        self.app.disableButton('ok')
        self.app.stopLabelFrame()
        self.app.startTabbedFrame('Solutions', 0, 1)
        self.add_solution_tab('方案1')
        self.add_solution_tab('方案2')
        self.add_solution_tab('方案3')
        self.app.stopTabbedFrame()

        self.app.go()

    def add_attribute_labels(self, attributes, row0, col0, col=1, suffix=''):
        i = row0
        j = col0
        for key, name in attributes.items():
            self.app.addLabel(key + '_key_' + suffix, name, i, j, 1, 1)
            self.app.addLabel(key + '_value_' + suffix, '0', i, j + 1, 1, 1)
            i += 1
            if i > int((len(attributes) + 1) / col):
                i = row0
                j += 2
        return i

    def get_init_attributes(self, title):
        self.app.enableButton('ok')
        self.target_shishen = self.s[self.app.getOptionBox('shishen')]
        attributes = self.target_shishen.attributes
        for key, value in attributes.items():
            self.app.setLabel(key + '_value_', value)

    def set_attributes(self, name, attributes):
        percentage_list = {}
        for key, value in attributes.items():
            self.app.setLabel(key + '_value_' + name, '%.2f' % value)
            percentage_list[key] = value / MAX_VALUES[key]
        canvas = self.app.getCanvas(name)
        draw_radar_with_percentage(canvas, self.canvas_x, self.canvas_y, percentage_list)

    def add_weight_scales(self, attributes, row0, col0):
        i = row0

        def func(title):
            self.app.setLabel(title, self.app.getScale(title))

        for key in attributes:
            self.app.addScale(key + 'W', i, col0, 1, 1)
            self.app.setScaleRange(key + 'W', 0, 50, curr=1)
            self.app.addLabel(key + 'W', '1', i, col0 + 1, 1, 1)
            self.app.setScaleChangeFunction(key + 'W', func)
            i += 1

        return i

    def add_solution_tab(self, name):
        self.app.startTab(name)
        self.app.startFrame(name + 'left', 0, 0)
        canvas = self.app.addCanvas(name, 0, 0, 4, 1)
        draw_radar_template(canvas, self.canvas_x, self.canvas_y)
        self.add_attribute_labels(ATTRIBUTES, 1, 0, col=2, suffix=name)
        self.app.stopFrame()
        self.app.startFrame(name + 'right', 0, 1)
        self.add_yuhun_list_toggles(name, 0, 0)
        self.app.stopFrame()
        self.app.stopTab()

    def start(self, btn):
        weights = {}
        for key in ATTRIBUTES:
            weights[key + 'W'] = self.app.getScale(key + 'W')
        self.target_shishen.target = Target(weights)
        if self.app.getOptionBox('types') != '- -  无  - -':
            self.target_shishen.type_name = self.app.getOptionBox('types')
        best_n_list = helper.find_best_solution_for(self.target_shishen)
        if not best_n_list:
            self.app.setLabel('result', '无可用方案')
            return
        i = 1
        for yh_list in best_n_list.values():
            self.target_shishen.clear_yuhun_list()
            self.target_shishen.set_yuhun_list(yh_list)
            self.set_attributes('方案' + str(i), self.target_shishen.final_attributes)
            for yh in yh_list:
                the_dict = yh.get_dict()
                name = the_dict.pop('Name')
                k = the_dict.pop('Position') - 1
                self.app.setToggleFrameText('方案' + str(i) + '-' + str(k), str(k + 1) + '号位：' + name)
                j = 0
                for key, value in the_dict.items():
                    self.app.setLabel('方案' + str(i) + str(k) + 'yuhun_key_' + str(j), YUHUN_ATTRIBUTES[key])
                    self.app.setLabel('方案' + str(i) + str(k) + 'yuhun_value_' + str(j), value)
                    j += 1
            i += 1
        self.app.setLabel('result', '生成完毕！')

    def add_yuhun_list_toggles(self, name, row0, col0):
        for i in range(6):
            self.app.startToggleFrame(name + '-' + str(i), row0 + i, col0)
            self.app.setToggleFrameText(name + '-' + str(i), str(i + 1) + '号位：')
            for j in range(5):
                self.app.addLabel(name + str(i) + 'yuhun_key_' + str(j), '', j, 0)
                self.app.addLabel(name + str(i) + 'yuhun_value_' + str(j), '', j, 1)
            self.app.stopToggleFrame()


if __name__ == '__main__':
    helper = Helper()
    Window(helper.shishen_store)
