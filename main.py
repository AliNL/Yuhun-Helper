# coding=utf-8

from src.helper import Helper
from src.target import Target


def main():
    helper = Helper()
    s = helper.shishen_store
    s['大天狗'].target = Target({'AW': 1, 'CRW': 3, 'CAW': 1})
    helper.find_best_solution_for(helper.shishen_store['大天狗'])


if __name__ == '__main__':
    main()
