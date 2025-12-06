from data.src._BasicImports import *  # 导入基本的模块和常量
from data.src._GameObjectImports import * # 导入各个游戏对象的类
from data.src.Game import *  # 导入游戏处理核心
# 定义游戏类
class Pvz:
    def __init__(self): # 初始化游戏
        self.running = False  # 设置游戏运行状态
        self.really = False  # 设置游戏开始状态
        icon = pygame.image.load(ICON_PATH)# 加载图标图像
        pygame.display.set_icon(icon)# 设置窗口图标
        CHOOSE_CARD_FRAME_CARD_X.append(0)
        CHOOSE_CARD_FRAME_CARD_Y.append(0)
        for i in range(1, CHOOSE_CARD_FRAME_CARD_COUNT[0] + 1):
            CHOOSE_CARD_FRAME_CARD_X.append(CHOOSE_CARD_FRAME_LEFT_X + (i - 1) * (CHOOSE_CARD_FRAME_CARD_SIZE[0] + CHOOSE_CARD_FRAME_CARD_X_SPACING))
        for i in range(1, CHOOSE_CARD_FRAME_CARD_COUNT[1] + 1):
            CHOOSE_CARD_FRAME_CARD_Y.append(CHOOSE_CARD_FRAME_TOP_Y + (i - 1) * (CHOOSE_CARD_FRAME_CARD_SIZE[1] + CHOOSE_CARD_FRAME_CARD_Y_SPACING))
        self.login = ""  # 初始化登录状态为空字符串

    def start(self, game, GameSetWindow): # 游戏开始界面
        pygame.init()  # 初始化pygame
        self.screen = pygame.display.set_mode(GAME_SIZE)  # 设置游戏窗口
        pygame.display.set_caption(GAME_TITLE + "V" + GAME_VERSION)  # 设置游戏窗口标题
        self.FPS = DEFAULT_FPS  # 设置游戏帧率
        self.clock = pygame.time.Clock()  # 设置时钟
        self.game = Game(game)  # 创建游戏处理核心实例
        self.ObjectGame = game  # 保存游戏对象实例
    
        self.loading_music()  # 加载音乐
        self.initialize_list()  # 初始化列表
        self.initialize_instance()  # 初始化实例

        self.GameSetWindow = GameSetWindow  # 保存游戏设置窗口实例

        self.startTime = 0
        # 播放音乐
        self.startMusic.play(-1)  # -1 表示无限循环
        # self.load()  # 加载游戏数据

        while not self.running:  # 当游戏还没开始时
            for event in pygame.event.get():  # 获取所有事件
                if event.type == pygame.QUIT:  # 如果事件类型为退出
                    os._exit(0)
            
            self.screen.fill(WHITE)  # 填充屏幕为白色
            self.startBackground.run()  # 运行开始背景

            # 判断是否点击开始按钮
            if self.startButton.start:
                self.startTime += 1
            if self.startTime == 20:
                self.running = True
            
            self.startButton.run()  # 运行开始按钮
            pygame.display.flip()  # 更新屏幕
            self.clock.tick(self.FPS)  # 设置帧率

    def chooseCard(self): # 选择卡片
        self.startMusic.stop()  # 停止开始音乐
        self.gameMusic.play(-1)  # -1 表示无限循环
        self.selectedCard = [] # 创建一个空列表来存储选中的卡片

        while not self.really: # 当游戏还在选择卡片时
            for event in pygame.event.get():  # 获取所有事件
                if event.type == pygame.QUIT:  # 如果事件类型为退出
                    os._exit(0)

            self.screen.fill(WHITE)  # 填充屏幕为白色
            self.background.run()  # 运行背景
            self.game.run()  # 运行游戏处理
            self.CardFrame.run()  # 运行卡片框
            self.ChooseCardFrame.run() # 运行选择卡片框

            for card in self.displayed_card:  # 遍历卡片
                card.run()  # 运行卡片
            for card in self.selectedCard:
                card.run()  # 运行选中的卡片
            for num in range(0, len(self.displayed_card_shadow_list)):
                if self.displayed_card[num].use:
                    self.displayed_card_shadow_list[num].run()  # 运行阴影
            
            self.reallyButton.run()  # 运行确定按钮
            if self.reallyButton.start:
                self.really = True

            pygame.display.flip()  # 更新屏幕
            self.clock.tick(self.FPS)  # 设置帧率

    def run(self): # 游戏运行界面
        for card in self.selectedCard:  # 遍历卡片列表
            self.card.append(Card(self.screen, card.name, card.PosNumber))  # 创建卡片实例
            self.card_shadow_list.append(Shadow(self.screen, CARD_SIZE, [CARD_FIRST_X + (CARD_SIZE[0] + 7) * self.selectedCard.index(card), CARD_POS_Y]))  # 创建阴影实例

        while self.running:  # 当游戏运行时
            if not self.gameover:
                for event in pygame.event.get():  # 获取所有事件
                    if event.type == pygame.QUIT:  # 如果事件类型为退出
                        os._exit(0)
                    elif pygame.mouse.get_pressed()[0]:  # 如果鼠标左键被按下
                        if not self.plant:
                            for card in self.card:  # 遍历卡片
                                if card.READY:
                                    if click(card.pos, card.size, pygame.mouse.get_pos()):  # 如果点击卡片
                                        if self.game.CheckPlant_Grid(card.name):
                                            self.plant = True
                                            self.plantType = card.number
                                            self.plantName = card.name

                                            self.Plant.name = self.plantName
                                            self.Plant.path = settings[self.plantName]['path']
                                            self.Plant.imageCount = settings[self.plantName]['imageCount']
                                            self.Plant.size = settings[self.plantName]['size']
                                            self.Plant.preIndexTimeNumber = settings['game']['plantPreIndexTimeNumber'][self.plantName]
                                            
                                            self.gridPlant.plantName = self.plantName
                                            self.gridPlant.path = settings[self.plantName]['path']
                                            self.gridPlant.imageCount = settings[self.plantName]['imageCount']
                                            self.gridPlant.size = settings[self.plantName]['size']
                                            self.gridPlant.preIndexTimeNumber = settings['game']['plantPreIndexTimeNumber'][self.plantName]
                                            
                self.screen.fill(WHITE)  # 填充屏幕为白色
                self.background.run()  # 运行背景
                self.game.run()  # 运行游戏核心

                self.CardFrame.run()  # 运行卡片框
                for card in self.card:
                    card.run()  # 运行卡片
                self.game.shovelFrame.run()  # 运行铲子框

                text_surface = pygame.font.Font(None, 33).render(str(self.game.gold), True, (0, 0, 0))
                # 设置文本表面的位置
                text_rect = text_surface.get_rect()
                text_rect.center = (60, 75)
                # 将文本表面绘制到屏幕上
                self.screen.blit(text_surface, text_rect)

                if self.plant: # 如果正在种植：种植
                    if self.game.CheckInGarden(pygame.mouse.get_pos()):
                        self.gridPlant.run()
                    if pygame.mouse.get_pressed()[0]:  #如果鼠标左键被按下
                        if not self.game.CheckAddPlant(pygame.mouse.get_pos(), self.plantType)['plant']: # 如果不能种植
                            continue # 跳过此次循环
                        for plant in settings["need_grow_soil_plant"]:
                            if plant == self.plantName:
                                self.growSoil_list.append(GrowSoil(self.ObjectGame, self.game.CheckAddPlant(pygame.mouse.get_pos(), self.plantType)['pos'])) #添加生长土壤到生长土壤列表
                                break
                        if self.plantType == 1: #如果种植的是阳光花
                            self.sunflower_list.append(Sunflower(self.ObjectGame, self.game.CheckAddPlant(pygame.mouse.get_pos(), self.plantType)['pos'])) #添加阳光花到阳光花列表
                            self.plant = False
                        elif self.plantType == 2: #如果种植的是豌豆射手
                            self.peashooter_list.append(Peashooter(self.ObjectGame, self.game.CheckAddPlant(pygame.mouse.get_pos(), self.plantType)['pos'])) #添加射手到射手列表
                            self.plant = False
                        elif self.plantType == 3: #如果种植的是坚果
                            self.nut_list.append(Nut(self.ObjectGame, self.game.CheckAddPlant(pygame.mouse.get_pos(), self.plantType)['pos'])) #添加坚果到坚果列表
                            self.plant = False
                        elif self.plantType == 4: #如果种植的是土豆地雷
                            self.potatoMine_list.append(PotatoMine(self.ObjectGame, self.game.CheckAddPlant(pygame.mouse.get_pos(), self.plantType)['pos'])) #添加坚果到坚果列表
                            self.plant = False
                        elif self.plantType == 5: #如果种植的是大嘴花
                            self.chomper_list.append(Chomper(self.ObjectGame, self.game.CheckAddPlant(pygame.mouse.get_pos(), self.plantType)['pos'])) #添加大嘴花到大嘴花列表
                            self.plant = False
                        elif self.plantType == 6: #如果种植的是樱桃炸弹
                            self.cherryBomb_list.append(CherryBomb(self.ObjectGame, self.game.CheckAddPlant(pygame.mouse.get_pos(), self.plantType)['pos'])) #添加樱桃炸弹到樱桃炸弹列表
                            self.plant = False
                        elif self.plantType == 7: #如果种植的是火爆辣椒
                            self.jalapeno_list.append(Jalapeno(self.ObjectGame, self.game.CheckAddPlant(pygame.mouse.get_pos(), self.plantType)['pos']))
                            self.plant = False
                        elif self.plantType == 8: #如果种植的是倭瓜
                            self.squash_list.append(Squash(self.ObjectGame, self.game.CheckAddPlant(pygame.mouse.get_pos(), self.plantType)['pos']))
                            self.plant = False
                        self.game.gold -= settings[settings['plant_name'][self.plantType]]['gold'] # 扣除金币

                for potatoMine in self.potatoMine_list:  # 遍历土豆地雷列表
                    if potatoMine.delete:
                        self.potatoMine_list.remove(potatoMine)
                        continue
                    potatoMine.run()

                for peashooter in self.peashooter_list:  # 遍历射手列表
                    peashooter.run()  # 运行射手

                for sunflower in self.sunflower_list:  # 遍历阳光花列表
                    sunflower.run()  # 运行阳光花

                for nut in self.nut_list: # 遍历坚果列表
                    nut.run() # 运行坚果
                
                for squash in self.squash_list:  # 遍历倭瓜列表
                    squash.run()  # 运行倭瓜
                
                for zombie in self.zombie_list:  # 遍历普通僵尸列表
                    zombie.run()  # 运行僵尸
                    if zombie.delete:  # 如果僵尸需要被删除
                        self.zombie_list.remove(zombie)  # 从普通僵尸列表中删除僵尸

                for head in self.zombieHead_list:  # 遍历僵尸头列表
                    head.run()  # 运行僵尸头
                    if head.delete:  # 如果僵尸头需要被删除
                        self.zombieHead_list.remove(head)  # 从僵尸头列表中删除僵尸头

                for chomper in self.chomper_list:  # 遍历大嘴花列表
                    chomper.run()  # 运行大嘴花
                
                for pea in self.pea_list:  # 遍历子弹列表
                    pea.run()  # 运行子弹
                    if pea.delete:  # 如果子弹需要被删除
                        self.pea_list.remove(pea)  # 从子弹列表中删除子弹

                for cherryBomb in self.cherryBomb_list:  # 遍历樱桃炸弹列表
                    cherryBomb.run()  # 运行樱桃炸弹

                for jalapeno in self.jalapeno_list:  # 遍历火爆辣椒列表
                    jalapeno.run()  # 运行火爆辣椒
                
                for growSoil in self.growSoil_list:  # 遍历生长土壤列表
                    growSoil.run()  # 运行生长土壤

                # 遍历卡片阴影列表
                for shadow in self.card_shadow_list:
                    # 获取当前阴影在列表中的索引位置
                    number = self.card_shadow_list.index(shadow)
                    # 检查卡片是否准备就绪且不能在当前网格种植
                    if self.card[number].READY and not self.game.CheckPlant_Grid(self.card[number].name):
                        # 运行阴影效果（显示不可用状态）
                        shadow.run()

                for lawnmower in self.lawnmower_list:  # 遍历草地机列表
                    lawnmower.run()  # 运行草地机

                for sunlight in self.sunlight_list:  # 遍历阳光列表
                    sunlight.run()  # 运行阳光

                self.game.shovel.run()  # 运行铲子
                
                if self.plant: # 如果正在种植
                    self.Plant.run()  # 运行种植提示

                for index in range(1, GRID_COUNT[1]) : # 遍历网格行数
                    flag = False  # 初始化标志为False
                    for zombie in self.zombie_list:  # 遍历僵尸列表
                        if zombie.posY == -1: # 如果僵尸的Y位置为-1
                            continue # 跳过此次循环
                        if zombie.grid[1] == index:  # 如果僵尸在当前行
                            flag = True  # 设置标志为True
                            break  # 跳出循环
                    self.zombiePos[index] = flag  # 更新僵尸位置列 是否有僵尸在当前行

            elif self.gameover: # 如果游戏结束
                for event in pygame.event.get():  # 获取所有事件
                    if event.type == pygame.QUIT:  # 如果事件类型为退出
                        os._exit(0)
                        
                self.screen.fill(WHITE)  # 填充屏幕为白色
                self.background.run()  # 运行背景
                self.game.run()  # 运行游戏核心

                self.CardFrame.run()  # 运行卡片框
                for card in self.card:
                    card.run()  # 运行卡片
                self.game.run()
                self.game.shovelFrame.run()  # 运行铲子框
                self.game.shovel.run()  # 运行铲子
                self.gameover_text.run() # 运行游戏结束文本

            self.clock.tick(self.FPS)  # 设置帧率
            pygame.display.flip()  # 更新屏幕
               
    def initialize_list(self): # 初始化列表
        self.zombie_list = []  # 普通僵尸列表
        self.sunflower_list = []  # 阳花列表
        self.sunlight_list = []  # 阳光列表
        self.peashooter_list = []  # 射手列表
        self.chomper_list = []  # 大嘴花列表
        self.pea_list = []  # 子弹列表
        self.zombieHead_list = []  # 僵尸头列表
        self.nut_list = []  # 坚果列表
        self.cherryBomb_list = []  # 樱桃炸弹列表
        self.jalapeno_list = []  # 火爆辣椒列表
        self.potatoMine_list = []  # 土豆地雷列表
        self.squash_list = []  # 倭瓜列表
        self.growSoil_list = []  # 生长土壤列表
        self.displayed_card_shadow_list = []  # 选择用卡片阴影列表
        self.card_shadow_list = []  # 卡片阴影列表
        self.zombiePos = [0, 0, 0, 0, 0, 0]  # 僵尸位置列表
        self.lawnmower_list = []  # 草地机列表
        self.lawnmowerIf = [0, 0, 0, 0, 0, 0]  # 草坪机是否已出现列表
    
    def SetWindowAtTheTop(self): # 设置窗口置顶
        import ctypes
        from ctypes import wintypes

        # 定位ctypes中的user32
        user32 = ctypes.WinDLL('user32', use_last_error=True)

        # 定义SetWindowPos函数
        SetWindowPos = user32.SetWindowPos
        SetWindowPos.argtypes = [wintypes.HWND, wintypes.HWND, wintypes.INT, wintypes.INT, wintypes.INT, wintypes.INT, wintypes.UINT]
        SetWindowPos.restype = wintypes.BOOL

        def set_window_topmost(hwnd):
            # HWND_TOPMOST是特殊的标志，表示窗口应该置于所有非顶置窗口之上
            HWND_TOPMOST = -1
            # 设置窗口为始终在最前面
            SetWindowPos(hwnd, HWND_TOPMOST, 0, 0, 0, 0, 0x0001)  # 0x0001 是SWP_NOMOVE | SWP_NOSIZE，意味着不改变位置和大小
        
        # 获取Pygame窗口的HWND
        pygame_hwnd = pygame.display.get_wm_info()['window']
        set_window_topmost(pygame_hwnd) # 设置窗口为最前面

    def CancelWindowAtTheTop(self): # 取消窗口置顶
        import ctypes
        from ctypes import wintypes

        # 定位ctypes中的user32
        user32 = ctypes.WinDLL('user32', use_last_error=True)

        # 定义SetWindowPos函数
        SetWindowPos = user32.SetWindowPos
        SetWindowPos.argtypes = [wintypes.HWND, wintypes.HWND, wintypes.INT, wintypes.INT, wintypes.INT, wintypes.INT, wintypes.UINT]
        SetWindowPos.restype = wintypes.BOOL

        def cancel_window_topmost(hwnd):
            # HWND_NOTOPMOST是特殊的标志，表示窗口不再置于所有非顶置窗口之上
            HWND_NOTOPMOST = -2
            # 取消窗口的始终在最前面状态
            SetWindowPos(hwnd, HWND_NOTOPMOST, 0, 0, 0, 0, 0x0001)

        # 获取Pygame窗口的HWND
        pygame_hwnd = pygame.display.get_wm_info()['window'] 
        cancel_window_topmost(pygame_hwnd)  # 取消窗口的最前面状态

    def initialize_instance(self):  # 初始化实例
        self.background = Background(self.screen)  # 创建背景实例

        self.plant = False  # 设置植物状态
        self.Plant = Plant(self.screen)  # 创建种植提示实例
        self.plantType = 0  # 种植植物类型
        self.plantName = ""  # 种植植物名称

        self.gridPlant = gridPlant(self.screen)  # 创建种植提示实例
        self.ChooseCardFrame = ChooseCardFrame(self.screen)  # 创建选择卡片框实例

        self.CardFrame = CardFrame(self.screen)  # 创建卡片框实例
        self.card = []  # 卡片实例列表
        self.displayed_card = []  # 显示卡片实例列表

        self.gameover_text = GameOverText(self.screen)  # 创建游戏结束文本实例
        self.gameover = False  # 设置游戏结束状态

        rankY = 1
        number = 1
        for rankX in range(1, len(settings['plant_name'])):  # 遍历卡片列表
            self.displayed_card.append(DisplayedCard(self.screen, 
                                                     settings['plant_name'][number],
                                                     (rankX, rankY)
                                                    )
                                      )
            self.displayed_card_shadow_list.append(Shadow(self.screen, 
                                                          CHOOSE_CARD_FRAME_CARD_SIZE,
                                                          (CHOOSE_CARD_FRAME_CARD_X[rankX],
                                                           CHOOSE_CARD_FRAME_CARD_Y[rankY])
                                                         )
                                                  )
            number += 1

        self.startBackground = StartBackground(self.screen)  # 创建开始背景实例
        self.startButton = StartButton(self.screen)  # 创建开始按钮实例
        self.reallyButton = ReallyButton(self.ObjectGame)  # 创建开始按钮实例

        for i in range(GRID_COUNT[1]):  # 遍历草地机列表
            self.lawnmower_list.append(Lawnmower(self.ObjectGame, i + 1))  # 创建草地机实例

    def loading_music(self): # 加载音乐
        # 加载背景音乐
        self.gameMusic = pygame.mixer.Sound(settings['game']['bgm']['gameMusic'])
        # 设置音乐参数
        self.gameMusic.set_volume(settings['game']['bgm']['gameMusicVolume'])  # 设置音量

        # 加载开始音乐
        self.startMusic = pygame.mixer.Sound(settings['game']['bgm']['startMusic'])
        # 设置音乐参数
        self.startMusic.set_volume(settings['game']['bgm']['startMusicVolume'])  # 设置音量

        # 加载阳光音乐
        self.sunMusic = pygame.mixer.Sound(settings['game']['bgm']['sunlight'])
        # 设置音乐参数
        self.sunMusic.set_volume(settings['game']['bgm']['sunVolume'])  # 设置音量

        self.cherryBombExplosionMusic = pygame.mixer.Sound(settings['cherry_bomb']['ExplosionSound'])  # 加载樱桃炸弹爆炸音效
        self.cherryBombExplosionMusic.set_volume(settings['cherry_bomb']['ExplosionSoundVolume'])  # 设置音量

        self.jalapenoExplosionMusic = pygame.mixer.Sound(settings['jalapeno']['ExplosionSound'])  # 加载火爆辣椒爆炸音效
        self.jalapenoExplosionMusic.set_volume(settings['jalapeno']['ExplosionSoundVolume'])  # 设置音量

        self.lawnmowerMusic = pygame.mixer.Sound(settings['lawnmower']['Music'])  # 加载草地机音乐
        self.lawnmowerMusic.set_volume(settings['lawnmower']['MusicVolume'])  # 设置音量

    def load(self): # 加载游戏数据
        with open('data/save/map.json', 'r') as map:
            map = [list(item) for item in json.loads(map)]
        with open('data/save/gold.json', 'r') as gold:
            gold = json.load(gold.read())

    def save(self): # 保存游戏数据
        with open('data/save/map.json', 'w') as map:
            map.write(str(self.game.map) + '\n')
        with open('data/save/gold.json', 'w') as gold:
            gold.write(str(self.game.gold))