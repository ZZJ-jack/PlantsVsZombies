from data.src.object import *

class Squash(Object):
    def __init__(self, game, pos):  # 初始化函数
        self.plantType = "squash" # 设置植物类型为倭瓜
        self.game = game  # 保存游戏引用
        super().__init__(game.screen, settings[self.plantType]["path"], settings[self.plantType]["size"], settings[self.plantType]["imageCount"], self.plantType)  # 调用父类初始化函数，传入屏幕对象和设置参数
        self.pos = list(pos)
        self.pos[0] += settings["game"]["gridPlantPos"][self.plantType][0]
        self.pos[1] += settings["game"]["gridPlantPos"][self.plantType][1]
        self.updateGrid(self.pos)
        self.state = "Idle"
        self.delete = 0
    
    def run(self):
        self.update()
        if self.state == "Attack" and self.imageIndex == self.imageCount:
            self.delete = 1
        self.draw()