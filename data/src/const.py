DEFAULT_FPS = 60  # 屏幕刷新率
GAME_SIZE = (1200, 600)  # 游戏窗口大小
GAME_SET_WINDOW_SIZE = (600, 400)  # 游戏设置窗口大小
USER_PATH = "./data/user/user.json"  # 用户密码文件路径
ICON_PATH = "./data/image/Other/icon.ico"  # 游戏图标路径
GAME_TITLE = "植物大战僵尸"  # 游戏窗口标题
GAME_VERSION = "2.4.8"  # 游戏版本号
ZONBIE_FIRST_X = 800  # 僵尸第一次出现的横坐标
ZOMBIE_TIME = 600  # 僵尸出现的时间间隔
SUNLIGHT_TIME = 900  # 阳光出现的时间间隔
PLANT_HP = 100  # 植物的生命值
NUT_HP = 100  # 坚果的生命值
SUNLIGHT_DELETE_TIME = 450  # 阳光消失的时间间隔

GRID_COUNT = (9, 5)  # 网格的行列数
GRID_TOP_Y = 108  # 网格的顶部纵坐标
GRID_DOWN_Y = 530  # 网格的底部纵坐标
GRID_LEFT_X = 230  # 网格的左边横坐标
GRID_RIGHT_X = 908  # 网格的右边横坐标
GRID_SIZE = (75, 85)  # 网格的大小
GRID_X = []  # 网格的横坐标
GRID_Y = []  # 网格的纵坐标
RIGHT_VIRTUAL_GRID_X = GRID_LEFT_X + (GRID_COUNT[0] + 1) * GRID_SIZE[0]  # 右侧虚拟网格的横坐标
CHOOSE_CARD_FRAME_CARD_COUNT = (8, 5)  # 选择卡片框的卡片行列数

CHOOSE_CARD_FRAME_CARD_X = []  # 选择卡片框的卡片横坐标
CHOOSE_CARD_FRAME_CARD_Y = []  # 选择卡片框的卡片纵坐标
CHOOSE_CARD_FRAME_LEFT_X = 112  # 选择卡片框的左边横坐标
CHOOSE_CARD_FRAME_CARD_X_SPACING = 7  # 卡片之间的间距
CHOOSE_CARD_FRAME_TOP_Y = 132  # 选择卡片框的顶部纵坐标
CHOOSE_CARD_FRAME_CARD_Y_SPACING = 5  # 卡片之间的间距
CHOOSE_CARD_FRAME_CARD_SIZE = (47, 65)  # 选择卡片框的卡片大小

CARD_POS_Y = 10  # 卡片所在的纵坐标
CARD_FIRST_X = 100  # 卡片第一次出现的横坐标
CARD_SIZE = (50, 70)  # 卡片的大小
CARD_FIRST_Y = -10  # 卡片第一次出现的纵坐标

LAWNMOWER_FIRST_X = 0  # 草地机第一次出现的横坐标
LAWNMOWER_POS_X = 170  # 草地机所在的横坐标

WHITE = (255, 255, 255)  # 白色
BLACK = (0, 0, 0)  # 黑色

PEATIME = 7  # 豌豆产生时间间隔
SUNTIME = 14  # 阳光产生时间间隔