import sys

from PySide6.QtCore import Qt, QRect, QPoint
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QApplication, QWidget

from cat import Mochi
from config import (
    APP_NAME,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    SCALE,
)


class MochiWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(APP_NAME)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        self.setAttribute(Qt.WA_TranslucentBackground)

        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

        screen = QApplication.primaryScreen().availableGeometry()

        self.move(
            screen.center().x() - self.width() // 2,
            screen.center().y() - self.height() // 2,
        )

        self.mochi = Mochi()

        # ===== 拖拽 =====

        self.dragging = False
        self.drag_pos = QPoint()

    # -----------------------------

    def paintEvent(self, event):

        painter = QPainter(self)

        frame = self.mochi.current_frame()

        if frame.isNull():
            return

        painter.setRenderHint(
            QPainter.SmoothPixmapTransform,
            False,
        )

        target = QRect(
            0,
            0,
            frame.width() * SCALE,
            frame.height() * SCALE,
        )

        painter.drawPixmap(target, frame)

    # -----------------------------

    def mousePressEvent(self, event):

        if event.button() == Qt.LeftButton:

            self.dragging = True

            self.drag_pos = (
                event.globalPosition().toPoint()
                - self.frameGeometry().topLeft()
            )

    # -----------------------------

    def mouseMoveEvent(self, event):

        if self.dragging:

            self.move(
                event.globalPosition().toPoint()
                - self.drag_pos
            )

    # -----------------------------

    def mouseReleaseEvent(self, event):

        self.dragging = False


def main():

    app = QApplication(sys.argv)

    window = MochiWindow()

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()