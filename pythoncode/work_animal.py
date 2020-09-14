# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         work_animal
# Description:  面向对象和yaml练习
# Author:       yanghao
# Date:         2020/6/8
# -------------------------------------------------------------------------------
import yaml


class Animal:
    def __init__(self, name, color, age, sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    def can_call(self):
        print(f"{self.name}can call")

    def can_run(self):
        print(f"{self.name}can run")


class Cat(Animal):
    def __init__(self, name, color, age, sex):
        super().__init__(name, color, age, sex)
        self.hair = "short"

    def catch_mouse(self):
        print(f"{self.name},{self.color},{self.age},{self.sex},{self.hair} catch mouse")

    def can_call(self):
        print(f"{self.name}can Mews")


class Dog(Animal):
    def __init__(self, name, color, age, sex):
        super().__init__(name, color, age, sex)
        self.hair = "long"

    def can_call(self):
        print(f"{self.name}can WangWang")

    def watch_home(self):
        print(f"{self.name},{self.color},{self.age},{self.sex},{self.hair} watch home")


if __name__ == '__main__':
    with open("animal_config.yaml") as f:
        data = yaml.safe_load(f)
    cat = Cat(data[0]['cat']['name'], data[0]['cat']['color'], data[0]['cat']['age'], data[0]['cat']['sex'])
    cat.catch_mouse()
    dog = Dog(data[1]['dog']['name'], data[1]['dog']['color'], data[1]['dog']['age'], data[1]['dog']['sex'])
    dog.watch_home()
