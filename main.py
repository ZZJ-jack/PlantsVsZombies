from data.src.PVZ import *  # 导入游戏类
from data.src.GameSet import *  # 导入游戏设置窗口类
from data.src.versionLogWindow import VersionLogWindow  # 导入版本更新日志窗口类
import threading # 导入多线程

class Main: # 主函数
    def __init__(self):
        # 显示版本更新日志窗口
        self.show_version_log_window()
        self.game = Pvz() # 创建游戏实例
        self.GameSetWindow = GameSet(self.game) # 创建游戏设置窗口
        self.RunGame = threading.Thread(target = self.CreateGameInstance) # 创建多线程:游戏运行窗口
        self.RunGameSetWindow = threading.Thread(target = self.CreateGameSet) # 创建多线程:游戏设置窗口
    
    def show_version_log_window(self):
        """显示版本更新日志窗口"""
        version_window = VersionLogWindow()
        version_window.show()
    
    def run(self):
        self.RunGame.start() # 启动游戏
        self.runGameSet() # 启动游戏设置窗口

    def runGameSet(self):
        self.RunGameSetWindow.start() # 启动游戏设置窗口
        self.GameSetWindow.StartLogin() # 启动登录窗口
        self.GameSetWindow.loginWindow.mainloop() # 运行登录窗口
        self.GameSetWindow.SetWindow.mainloop() # 运行窗口

    def CreateGameInstance(self): # 创建游戏实例
        self.game.start(self.game, self.GameSetWindow) # 开始游戏
        self.game.chooseCard() # 选择卡牌
        self.game.run() # 运行游戏
        self.game.save() # 保存游戏

    def CreateGameSet(self): # 创建游戏设置窗口
        pass

if __name__ == '__main__': # 如果是主程序
    main = Main() # 创建主函数
    main.game.main = main  # 保存主函数实例
    main.run() # 运行主函数