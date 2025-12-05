from data.src._BasicImports import *  # 导入基本导入模块

# 定义游戏结束文本类
class GameOverText(Object):
    # 初始化游戏结束文本类
    def __init__(self, screen):
        super().__init__(screen, settings['gameover']['path'], settings['gameover']['size'], 1)
        self.pos = list(settings['gameover']['pos'])
    def run(self):
        self.update()
        self.draw()