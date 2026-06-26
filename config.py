"""
Mochi Desktop Pet
配置文件
"""

from pathlib import Path

# ========= 基础信息 =========

APP_NAME = "Mochi Desktop Pet"
CAT_NAME = "Mochi"

# ========= 显示 =========

SCALE = 2

WINDOW_WIDTH = 32 * SCALE
WINDOW_HEIGHT = 32 * SCALE

FPS = 60

# ========= 移动 =========

WALK_SPEED = 1.5

IDLE_TIME_MIN = 2
IDLE_TIME_MAX = 5

# ========= 项目路径 =========

ROOT_DIR = Path(__file__).parent

ASSET_DIR = ROOT_DIR / "assets"

SAVE_FILE = ROOT_DIR / "save.json"

# ========= 动画 =========

DEFAULT_ANIMATION = "idle"

FRAME_DURATION = 120

# ========= 对话 =========

RANDOM_WORDS = [
    "喵～",
    "今天也要加油！",
    "摸摸我嘛。",
    "呼噜……",
    "想吃鱼。",
]