from data.src.object import *

class Lawnmower(Object):  # 定义Lawnmower类，继承自object类
    def __init__(self, game, gridY):  # 初始化函数
        self.game = game
        super().__init__(game.screen, settings['lawnmower']['path'], settings['lawnmower']['size'], settings['lawnmower']['imageCount'])
        self.gridY = gridY
        self.pos = [LAWNMOWER_FIRST_X, GRID_Y[gridY]]
        self.name = "lawnmower"
        self.GoOut = 0
        self.Delete = 0
        self.updateGrid(self.pos)
        self.grid[1] += 1
        self.game.lawnmowerIf[self.grid[1]] = 1 # 标记草坪机已出现
        self.pos[1] += settings['lawnmower']['YposChange']
        self.bgmPlaying = False  # 草坪机音乐是否正在播放

    def run(self):  # 运行函数
        if self.pos[0] < LAWNMOWER_POS_X:  # 如果Card图片位置在卡片位置之上
            self.pos[0] += 1  # 向右移动
            self.update()
        if self.GoOut == 1:
            if not self.bgmPlaying:
                self.game.lawnmowerMusic.play()  # 循环播放草坪机音乐
                self.bgmPlaying = True
            self.pos[0] += 1
            if self.pos[0] >= GAME_SIZE[0]:
                self.Delete = 1
            self.update()
        self.draw()  # 绘制