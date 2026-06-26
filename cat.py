"""
cat.py
Mochi 本体
"""

from animation import Animation


class Mochi:

    def __init__(self):

        # ---------- 位置 ----------
        self.x = 200
        self.y = 200

        # ---------- 朝向 ----------
        self.face_right = True

        # ---------- 状态 ----------
        self.state = "idle"

        # ---------- 属性 ----------
        self.mood = 100
        self.hunger = 100

        # ---------- 动画 ----------
        self.animations = {
            "idle": Animation("idle"),
            "walk": Animation("walk"),
            "sleep": Animation("sleep"),
        }

        self.current_animation = self.animations["idle"]

    # -----------------------------

    def set_state(self, state):

        if state == self.state:
            return

        if state not in self.animations:
            return

        self.state = state

        self.current_animation = self.animations[state]
        self.current_animation.reset()

    # -----------------------------

    def update(self):

        """
        每一帧都会调用
        """

        self.current_animation.next()

    # -----------------------------

    def current_frame(self):

        return self.current_animation.current()