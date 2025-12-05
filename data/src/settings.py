# 从 ./data/src/const 模块导入所有常量
from data.src.const import *

# 定义一个字典，用于存储游戏中各种元素的属性，后续游戏逻辑会依据这些属性运行
settings = {
    # 植物名称列表，索引 0 位置为空字符串，后续索引对应不同植物名称
    "plant_name": ["", "sunflower", "peashooter", "nut", "potato_mine", "chomper", "cherry_bomb", "jalapeno", "squash"],
    # 需要生长土壤的植物
    "need_grow_soil_plant": ["sunflower", "peashooter", "nut", "potato_mine", "chomper", "squash"],
    # 植物卡片图片路径列表，索引与 plant_name 列表对应，0 位置为空字符串
    "plant_card_path": ["",
                        "./data/image/PlantCard/Sunflower.png",  # 向日葵卡片图片路径
                        "./data/image/PlantCard/Peashooter.png", # 豌豆射手卡片图片路径
                        "./data/image/PlantCard/Nut.png",        # 坚果卡片图片路径
                        "./data/image/PlantCard/PotatoMine.png", # 土豆地雷卡片图片路径
                        "./data/image/PlantCard/Chomper.png",    # 食人花卡片图片路径
                        "./data/image/PlantCard/CherryBomb.png",  # 樱桃炸弹卡片图片路径
                        "./data/image/PlantCard/Jalapeno.png",  # 火爆辣椒卡片图片路径
                        "./data/image/PlantCard/Squash.png",    # 倭瓜卡片图片路径
                        ],
    # 游戏相关设置
    "game": {
        # 游戏音效相关设置
        "bgm":{
            "startMusic": "./data/bgm/Crazy Dave.mp3",       # 游戏开始界面音乐文件路径
            "startMusicVolume": 0.4,                       # 游戏开始界面音乐音量
            "gameMusic": "./data/bgm/Grasswalk.mp3",         # 游戏进行时背景音乐文件路径
            "gameMusicVolume": 0.4,                       # 游戏进行时背景音乐音量
            "sunlight": "./data/bgm/Sun.mp3",               # 收集阳光时音效文件路径
            "sunVolume": 0.9,                             # 收集阳光时音效音量
            "plant": "./data/bgm/Plant.mp3",                # 种植植物时音效文件路径
            "plantVolume": 0.1,                           # 种植植物时音效音量
            "zombieEat": "./data/bgm/ZombieEat.mp3",       # 僵尸啃食植物时音效文件路径
            "zombieEatVolume": 0.1,                       # 僵尸啃食植物时音效音量
            "potatoMineExplosion": "./data/bgm/PotatoMineExplosion.mp3",  # 土豆地雷爆炸时音效文件路径
            "potatoMineExplosionVolume": 0.4,               # 土豆地雷爆炸时音效音量
            "chomperCatch": "./data/bgm/ChomperCatch.mp3", # 食人花捕捉僵尸时音效文件路径
            "chomperCatchVolume": 0.1,                    # 食人花捕捉僵尸时音效音量
            "gameover": "./data/bgm/gameover.mp3",          # 游戏结束时音效文件路径
            "win": "./data/bgm/win.mp3",                    # 游戏胜利时音效文件路径
        },
        # 植物在网格中的位置偏移量
        "gridPlantPos":{
            "sunflower": (3, 0),    # 向日葵在网格中的位置偏移
            "peashooter": (10, 0),   # 豌豆射手在网格中的位置偏移
            "nut": (10, 5),          # 坚果在网格中的位置偏移
            "potato_mine": (8, 10),  # 土豆地雷在网格中的位置偏移
            "chomper": (4, -8),     # 食人花在网格中的位置偏移
            "cherry_bomb" : (0, 0),   # 樱桃炸弹在网格中的位置偏移
            "jalapeno" : (10, 0),      # 火爆辣椒在网格中的位置偏移
            "squash" : (-3, -105),        # 倭瓜在网格中的位置偏移
        },
        # 鼠标拖动植物时的位置偏移量
        "mousePlantPos":{
            "sunflower": (-30, -30),  # 拖动向日葵时的位置偏移
            "peashooter": (-30, -30), # 拖动豌豆射手时的位置偏移
            "nut": (-30, -30),        # 拖动坚果时的位置偏移
            "potato_mine": (-30, -30),# 拖动土豆地雷时的位置偏移
            "chomper": (-45, -50),    # 拖动食人花时的位置偏移
            "cherry_bomb": (-35, -35), # 拖动樱桃炸弹时的位置偏移
            "jalapeno": (-25, -35),    # 拖动火爆辣椒时的位置偏移
            "squash": (-32, -150),      # 拖动倭瓜时的位置偏移
        },
        # 植物动画帧切换的时间间隔
        "plantPreIndexTimeNumber":{
            "sunflower": 0.1,    # 向日葵动画帧切换时间间隔
            "peashooter": 0.08,  # 豌豆射手动画帧切换时间间隔
            "nut": 0.1,          # 坚果动画帧切换时间间隔
            "potato_mine": 0.2,  # 土豆地雷动画帧切换时间间隔
            "chomper": 0.1,      # 食人花动画帧切换时间间隔
            "cherry_bomb": 0.1,   # 樱桃炸弹动画帧切换时间间隔
            "jalapeno": 0.1,      # 火爆辣椒动画帧切换时间间隔
            "squash": 0.08,        # 倭瓜动画帧切换时间间隔
        },
        # 植物碰撞检测的 X 轴偏移量
        "detectionPlantXPos": {
            "lawnmower": -40,     # 草地机碰撞检测 X 轴偏移量
            "peashooter": -40,    # 豌豆射手碰撞检测 X 轴偏移量
            "sunflower": -40,     # 向日葵碰撞检测 X 轴偏移量
            "nut": -50,           # 坚果碰撞检测 X 轴偏移量
            "potato_mine": -50,   # 土豆地雷碰撞检测 X 轴偏移量
            "chomper": 0,         # 食人花碰撞检测 X 轴偏移量
            "cherry_bomb": 0,     # 樱桃炸弹碰撞检测 X 轴偏移量
            "jalapeno": 0,         # 火爆辣椒碰撞检测 X 轴偏移量
            "squash": 0,           # 倭瓜碰撞检测 X 轴偏移量
        },
        # 游戏中会出现的僵尸类型集合
        "zombieType": {
            "common_zombie",
            "conehead_zombie",
            "buckethead_zombie"
        },
        # 不同类型僵尸出现的概率，数值越大越容易出现
        "zombieChooseProbability": { 
            "common_zombie": 100,  # 普通僵尸出现概率为 100%
            "conehead_zombie": 50,  # 路障僵尸出现概率为 50%
            "buckethead_zombie": 50  # 铁桶僵尸出现概率为 50%
        },
        # 豌豆射手对不同类型僵尸的攻击力
        "peaAttackPower":{ 
            "common_zombie": 20, # 对普通僵尸的攻击力
            "conehead_zombie": 10, # 对路障僵尸的攻击力
            "buckethead_zombie": 10, # 对铁桶僵尸的攻击力
        },
        "zombie-burn": { # 僵尸燃烧状态相关设置
            "Path": "./data/image/Zombie/Burn/Burn%d.svg",  # 僵尸燃烧状态图片路径
            "ImageCount": 11,  # 僵尸燃烧状态图片数量
            "Size": (55, 60),  # 僵尸燃烧状态图片尺寸
            "Pos": (45, 40)   # 僵尸燃烧状态图片位置偏移
        },
    },
    # 阴影相关设置
    "shadow":{
        "name": "shadow",           # 阴影名称
        "path": "./data/image/Other/shadow.png" # 阴影图片文件路径
    },
    # 卡片选择框相关设置
    "ChooseCardFrame":{
        "name": "ChooseCardFrame",  # 卡片选择框名称
        "size": (470, 500),         # 卡片选择框尺寸
        "path": "./data/image/Other/ChooseCardFrame.png", # 卡片选择框图片文件路径
        "pos": (90, 90),            # 卡片选择框位置
    },
    "GrowSoil":{
        "name": "GrowSoil",  # 成长土壤名称
        "size": (80, 40),  # 成长土壤显示尺寸
        "path": "./data/image/GrowSoil/GrowSoil(%d).png",  # 成长土壤图片路径
        "imageCount": 6,  # 成长土壤图片数量
        "posChange": (-4, 50),  # 成长土壤位置偏移
    },
    # 豌豆射手相关属性设置
    "peashooter": {
        "name": "peashooter",  # 豌豆射手名称
        "gold": 100,           # 种植豌豆射手所需金币数量
        "size": (60, 80),  # 豌豆射手显示尺寸
        "path": "./data/image/Plant/Peashooter/Idle%d.png",  # 豌豆射手闲置状态图片路径
        "imageCount": 10,  # 豌豆射手闲置状态图片数量
        "shoot_path": "./data/image/Plant/Peashooter/Shoot%d.png",  # 豌豆射手射击状态图片路径
        "shoot_imageCount": 8,  # 豌豆射手射击状态图片数量
        "collisionSize": (60, 80),  # 豌豆射手实际碰撞盒尺寸（扣除透明区域）
    },
    # 向日葵相关属性设置
    "sunflower": {
        "name": "sunflower",  # 向日葵名称
        "gold": 50,           # 种植向日葵所需金币数量
        "size": (70, 80),  # 向日葵显示尺寸
        "path": "./data/image/Plant/Sunflower/Idle(%d).png",  # 向日葵闲置状态图片路径
        "imageCount": 18,  # 向日葵闲置状态图片数量
        "shoot_path": "./data/image/Plant/Sunflower/Shoot(%d).png",  # 向日葵产生阳光状态图片路径
        "shoot_imageCount": 18,  # 向日葵产生阳光状态图片数量
        "collisionSize": (60, 80),  # 向日葵实际碰撞盒尺寸（扣除透明区域）
    },
    # 坚果相关属性设置
    "nut": {
        "name": "nut",  # 坚果名称
        "path": "./data/image/Plant/Nut/Nut-1(%d).png",  # 坚果初始状态图片路径
        "imageCount": 16,  # 坚果初始状态图片数量
        "path1": "./data/image/Plant/Nut/Nut-1(%d).png",  # 坚果状态 1 图片路径
        "imageCount1": 16,  # 坚果状态 1 图片数量
        "path2": "./data/image/Plant/Nut/Nut-2 (%d).png",  # 坚果状态 2 图片路径
        "imageCount2": 11,  # 坚果状态 2 图片数量
        "path3": "./data/image/Plant/Nut/Nut-3 (%d).png",  # 坚果状态 3 图片路径
        "imageCount3": 15,  # 坚果状态 3 图片数量
        "gold": 50,           # 种植坚果所需金币数量
        "size": (60, 70),  # 坚果显示尺寸
        "collisionSize": (60, 70),  # 坚果实际碰撞盒尺寸（扣除透明区域）
    },
    # 土豆地雷相关属性设置
    "potato_mine": {
        "name": "potato_mine",  # 土豆地雷名称
        "gold": 25,           # 种植土豆地雷所需金币数量
        "size": (60, 60),  # 土豆地雷显示尺寸
        "growTime": 600,  # 土豆地雷成长所需时间
        "ExplosionTime": 20,  # 土豆地雷爆炸持续时间
        "initPath": "./data/image/Plant/PotatoMine/PotatoMineInit.png",  # 土豆地雷初始状态图片路径
        "initImageCount": 1,  # 土豆地雷初始状态图片数量
        "path": "./data/image/Plant/PotatoMine/PotatoMine (%d).png",  # 土豆地雷正常状态图片路径
        "imageCount": 8,  # 土豆地雷正常状态图片数量
        "ExplosionPath": "./data/image/Plant/PotatoMine/PotatoMineExplosion.png",  # 土豆地雷爆炸状态图片路径
        "ExplosionImageCount": 1,  # 土豆地雷爆炸状态图片数量
        "ExplosionSound": "./data/bgm/Explosion.mp3",  # 土豆地雷爆炸音效文件路径
        "collisionSize": (60, 60),  # 土豆地雷实际碰撞盒尺寸（扣除透明区域）
    },
    # 食人花相关属性设置
    "chomper": {
        "name": "chomper",  # 食人花名称
        "gold": 150,           # 种植食人花所需金币数量
        "size": (105, 95),  # 食人花显示尺寸
        "path": "./data/image/Plant/Chomper/Idle(%d).png",  # 食人花闲置状态图片路径
        "imageCount": 13,  # 食人花闲置状态图片数量
        "eatPath": "./data/image/Plant/Chomper/Eat(%d).png",  # 食人花进食瞬间图片路径
        "eatImageCount": 9,  # 食人花进食瞬间图片数量
        "eatingPath": "./data/image/Plant/Chomper/Eating(%d).png",  # 食人花进食过程图片路径
        "eatingImageCount": 6,  # 食人花进食过程图片数量
        "eatingTime": 180,  # 食人花进食持续时间
        "collisionSize": (65, 95),  # 食人花实际碰撞盒尺寸（扣除透明区域）
    },
    # 樱桃炸弹相关属性设置
    "cherry_bomb": {
        "name": "cherry_bomb",  # 樱桃炸弹名称
        "gold": 150,           # 种植樱桃炸弹所需金币数量
        "size": (80, 60),  # 樱桃炸弹显示尺寸
        "ExplosionPath": "./data/image/Plant/CherryBomb/Explosion(%d).png",  # 樱桃炸弹爆炸状态图片路径
        "ExplosionImageCount": 13,  # 樱桃炸弹爆炸状态图片数量
        "ExplosionSound": "./data/bgm/CherryBombExplosion.mp3",  # 樱桃炸弹爆炸音效文件路径
        "collisionSize": (80, 80),  # 樱桃炸弹实际碰撞盒尺寸（扣除透明区域）
        "initExplosionPath": "./data/image/Plant/CherryBomb/Idle(%d).png",  # 樱桃炸弹准备爆炸状态图片路径
        "initExplosionImageCount": 7,  # 樱桃炸弹准备爆炸状态图片数量
        "path" : "./data/image/Plant/CherryBomb/Idle(%d).png",  # 樱桃炸弹闲置状态图片路径
        "imageCount": 7,  # 樱桃炸弹闲置状态图片数量
        "ExplosionRange": [[-1, -1], [-1, 0], [-1, 1],
                           [0, -1], [0, 0], [0, 1],
                           [1, -1], [1, 0], [1, 1]],  # 樱桃炸弹爆炸范围相对位置
        "ExplosionSoundVolume": 0.5,  # 樱桃炸弹爆炸音效音量
        "ExplosionSize": (100, 95),  # 樱桃炸弹爆炸状态图片尺寸
        "ExplosionPosOffset": (-8, -10),  # 樱桃炸弹爆炸状态图片位置偏移量
    },
    # 火爆辣椒相关属性设置
    "jalapeno": {
        "name": "jalapeno",  # 火爆辣椒名称
        "gold": 125,           # 种植火爆辣椒所需金币数量
        "size": (60, 80),  # 火爆辣椒显示尺寸
        "path": "./data/image/Plant/Jalapeno/Jalapeno(%d).png",  # 火爆辣椒正常状态图片路径
        "imageCount": 8,  # 火爆辣椒正常状态图片数量
        "ExplosionPath": "./data/image/Plant/Jalapeno/JalapenoAttack(%d).png",  # 火爆辣椒爆炸状态图片路径
        "ExplosionImageCount": 8,  # 火爆辣椒爆炸状态图片数量
        "ExplosionSize": (679, 100),  # 火爆辣椒爆炸状态图片尺寸
        "ExplosionSound": "./data/bgm/JalapenoExplosion.mp3",  # 火爆辣椒爆炸音效文件路径
        "ExplosionSoundVolume": 0.5,  # 火爆辣椒爆炸音效音量
        "ExplosionPos": (GRID_LEFT_X, -15),  # 火爆辣椒爆炸状态图片位置偏移量
    },
    # 倭瓜相关属性设置
    "squash": {
        "name": "squash",  # 倭瓜名称
        "gold": 50,           # 种植倭瓜所需金币数量
        "size": (80, 180),  # 倭瓜显示尺寸
        "path": "./data/image/Plant/Squash/Squash/(%d).png",  # 倭瓜正常状态图片路径
        "imageCount": 17,  # 倭瓜正常状态图片数量
        "AttackPath": "./data/image/Plant/Squash/SquashAttack/(%d).png",  # 倭瓜攻击状态图片路径
        "AImageCount": 4,  # 倭瓜攻击状态图片数量
        "collisionSize": (80, 100),  # 倭瓜实际碰撞盒尺寸（扣除透明区域）
    },
    # 普通僵尸相关属性设置
    "common_zombie": {
        "name": "zombie",  # 普通僵尸名称
        "hp": 100,  # 普通僵尸生命值
        "size": (110, 110),  # 普通僵尸显示尺寸
        "attack_power": 20,  # 普通僵尸攻击力
        "path": "./data/image/Zombie/Zombie/Idle (%d).png",  # 普通僵尸闲置状态图片路径
        "imageCount": 18,  # 普通僵尸闲置状态图片数量
        "eatPath": "./data/image/Zombie/Zombie/Eat (%d).png",  # 普通僵尸进食状态图片路径
        "eatImageCount": 21,  # 普通僵尸进食状态图片数量
        "headlessPath": "./data/image/Zombie/Zombie/Headless (%d).png",  # 普通僵尸无头状态图片路径
        "headlessImageCount": 18,  # 普通僵尸无头状态图片数量
        "deadPath": "./data/image/Zombie/Zombie/die (%d).png",  # 普通僵尸死亡状态图片路径
        "deadImageCount": 10,  # 普通僵尸死亡状态图片数量
    },
    # 路障僵尸相关属性设置
    "conehead_zombie": {
        "name": "conehead_zombie",  # 路障僵尸名称
        "hp": 140,  # 路障僵尸生命值
        "size": (110, 110),  # 路障僵尸显示尺寸
        "attack_power": 30,  # 路障僵尸攻击力
        "path": "./data/image/Zombie/ConeheadZombie/walk(%d).png",  # 路障僵尸行走状态图片路径
        "imageCount": 21,  # 路障僵尸行走状态图片数量
        "eatPath": "./data/image/Zombie/ConeheadZombie/eat(%d).png",  # 路障僵尸进食状态图片路径
        "eatImageCount": 11,  # 路障僵尸进食状态图片数量
        "headlessPath": "./data/image/Zombie/Zombie/Headless (%d).png",  # 路障僵尸无头状态图片路径
        "headlessImageCount": 18,  # 路障僵尸无头状态图片数量
        "deadPath": "./data/image/Zombie/Zombie/die (%d).png",  # 路障僵尸死亡状态图片路径
        "deadImageCount": 10,  # 路障僵尸死亡状态图片数量
    },
    # 铁桶僵尸相关属性设置
    "buckethead_zombie": {
        "name": "buckethead_zombie",  # 铁桶僵尸名称
        "hp": 180,  # 铁桶僵尸生命值
        "size": (110, 110),  # 铁桶僵尸显示尺寸
        "attack_power": 30,  # 铁桶僵尸攻击力
        "path": "./data/image/Zombie/BucketheadZombie/walk(%d).png",  # 铁桶僵尸行走状态图片路径
        "imageCount": 15,  # 铁桶僵尸行走状态图片数量
        "eatPath": "./data/image/Zombie/BucketheadZombie/eat(%d).png",  # 铁桶僵尸进食状态图片路径
        "eatImageCount": 11,  # 铁桶僵尸进食状态图片数量
        "headlessPath": "./data/image/Zombie/Zombie/Headless (%d).png",  # 铁桶僵尸无头状态图片路径
        "headlessImageCount": 18,  # 铁桶僵尸无头状态图片数量
        "deadPath": "./data/image/Zombie/Zombie/die (%d).png",  # 铁桶僵尸死亡状态图片路径
        "deadImageCount": 10,  # 铁桶僵尸死亡状态图片数量
    },
    # 僵尸头部相关属性设置
    "zombie_head": {
        "path": "./data/image/Zombie/Zombie_Head/(%d).png",  # 僵尸头部图片路径
        "imageCount": 12,  # 僵尸头部图片数量
        "size": (110, 110),  # 僵尸头部显示尺寸
    },
    "lawnmower": {
        "name": "lawnmower",  # 草坪机名称
        "YposChange": 20,  # 草坪机y坐标偏移
        "path": "./data/image/Lawnmower/(%d).svg",  # 草坪机图片路径
        "size": (70, 60),  # 草坪机显示尺寸
        "imageCount": 3,  # 草坪机图片数量
        "collisionSize": (70, 60),  # 草坪机碰撞尺寸
        "Music": "./data/bgm/Lawnmower.mp3",  # 草坪机音乐文件路径
        "MusicVolume": 0.5,  # 草坪机音乐音量
    },
    # 阳光相关属性设置
    "sunlight": {
        "name": "sun",  # 阳光名称
        "path": "./data/image/Sunlight/(%d).png",  # 阳光图片路径
        "size": (60, 60),  # 阳光显示尺寸
        "imageCount": 30,  # 阳光图片数量
    },
    # 卡片框相关属性设置
    "cardframe": {
        "name": "cardframe",  # 卡片框名称
        "path": "./data/image/Other/CardFrame.png",  # 卡片框图片路径
        "size": (540, 90),  # 卡片框尺寸
        "pos": (20, 0),  # 卡片框位置
    },
    # 游戏背景相关属性设置
    "background": {
        "name": "background",  # 游戏背景名称
        "path": "./data/image/Other/background.png",  # 游戏背景图片路径
        "pos": (0, -130),  # 游戏背景位置
        "size": (1300, 800),  # 游戏背景尺寸
    },
    # 游戏开始界面背景相关属性设置
    "startBackground": {
        "name": "startBackground",  # 游戏开始界面背景名称
        "path": "./data/image/Other/Start-Background.png",  # 游戏开始界面背景图片路径
        "size": (1200, 700),  # 游戏开始界面背景尺寸
        "pos": (0, -50),  # 游戏开始界面背景位置
    },
    # 豌豆相关属性设置
    "pea": {
        "name": "pea",  # 豌豆名称
        "path": "./data/image/Other/Pea.png",  # 豌豆图片路径
        "size": (20, 20),  # 豌豆尺寸
    },
    # 铲子相关属性设置
    "shovel": {
        "name": "shovel",  # 铲子名称
        "path": "./data/image/Other/Shovel.png",  # 铲子图片路径
        "size": (60, 70),  # 铲子尺寸
    },
    # 铲子框相关属性设置
    "shovelFrame": {
        "name": "shovelFrame",  # 铲子框名称
        "path": "./data/image/Other/ShovelFrame.png",  # 铲子框图片路径
        "pos": (560, 0),  # 铲子框位置
        "size": (70, 70),  # 铲子框尺寸
    },
    # 游戏结束界面相关属性设置
    "gameover": {
        "name": "gameover",  # 游戏结束界面名称
        "path": "./data/image/Other/GameOver.png",  # 游戏结束界面图片路径
        "size": (800, 600),  # 游戏结束界面尺寸
        "pos": (200, 0),  # 游戏结束界面位置
    },
    # 游戏开始按钮相关属性设置
    "startButton": {
        "name": "startButton",  # 游戏开始按钮名称
        "path": "./data/image/Other/Adventure_1.png",  # 游戏开始按钮正常状态图片路径
        "onPath": "./data/image/Other/Adventure_0.png",  # 游戏开始按钮被选中状态图片路径
        "size": (350, 180),  # 游戏开始按钮尺寸
        "pos": (670, 50),  # 游戏开始按钮位置
    },
    # 确认开始游戏按钮相关属性设置
    "reallyButton": {
        "name": "startButton",  # 确认开始游戏按钮名称
        "path": "./data/image/Other/ReallyButton.png",  # 确认开始游戏按钮图片路径
        "size": (155, 35),  # 确认开始游戏按钮尺寸
        "pos": (247, 540),  # 确认开始游戏按钮位置
    },
}