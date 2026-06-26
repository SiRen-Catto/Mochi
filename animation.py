"""
animation.py
负责加载和播放 Mochi 的像素动画
"""

from pathlib import Path

from PySide6.QtGui import QPixmap

from config import ASSET_DIR


class Animation:
    """
    一个动画，例如：

    idle
      idle_0.png
      idle_1.png
      idle_2.png
      idle_3.png
    """

    def __init__(self, name: str):

        self.name = name
        self.frames = []
        self.index = 0

        self.load()

    def load(self):
        """读取 assets/<动画名>/ 下所有 png"""

        folder = ASSET_DIR / self.name

        if not folder.exists():
            print(f"[Animation] 找不到动画：{folder}")
            return

        files = sorted(folder.glob("*.png"))

        for file in files:
            self.frames.append(QPixmap(str(file)))

        print(
            f"[Animation] {self.name}: "
            f"{len(self.frames)} frame(s)"
        )

    def current(self):

        if not self.frames:
            return QPixmap()

        return self.frames[self.index]

    def next(self):

        if not self.frames:
            return

        self.index += 1

        if self.index >= len(self.frames):
            self.index = 0

    def reset(self):

        self.index = 0

    def frame_count(self):

        return len(self.frames)