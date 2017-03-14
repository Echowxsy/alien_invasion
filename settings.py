class Settings():
    """储存设置类"""

    def __init__(self):
        # 屏幕设置
        self.screen_width = 800  # 高
        self.screen_height = 600  # 宽
        self.bg_color = (230, 230, 230)  # 背景颜色
        self.caption = "Alien Invasion"  # 标题名称

        # ship 飞船
        self.ship_limit = 3  # 飞船数量

        # bullet 子弹
        self.bullet_width = 300   # 子弹宽度
        self.bullet_height = 10  # 子弹长度
        self.bullet_color = 60, 60, 60  # 子弹颜色
        self.bullets_allowed = 3  # 同时存在的子弹数目

        # alien 外星人
        self.fleet_drop_speed = 10  # 外星人下降速度

        self.speedup_scale = 1.1  # 游戏加快速率
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """动态设置 随着游戏进程变化"""

        self.ship_speed_factor = 1.5  # 飞船移动速度
        self.bullet_speed_factor = 3  # 子弹速度
        self.alien_speed_factor = 1  # 外星人移动速度
        self.fleet_direction = 1  # 外星人移动方向
        # 1：右 -1：左
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)
