import sys
import sqlite3
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QGraphicsDropShadowEffect
)
from PySide6.QtGui import (
    QPainter, QColor, QPen, QPixmap
)
from PySide6.QtCore import Qt


class MainMenu(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("JORMOS Strategic Games")
        self.setFixedSize(1081, 1018)

        self.pixel_font = "Press Start 2P"
        self.title_font = "Orbitron"

        self.username = self.get_username()

        self.init_ui()

    # =====================================
    # USERNAME HOLEN
    # =====================================
    def get_username(self):
        try:
            conn = sqlite3.connect("users.db")
            cur = conn.cursor()

            cur.execute("""
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT
                )
            """)

            cur.execute(
                "SELECT username FROM users ORDER BY id DESC LIMIT 1"
            )
            row = cur.fetchone()

            conn.close()

            if row:
                return row[0]
            return "?"

        except:
            return "?"

    # =====================================
    # UI
    # =====================================
    def init_ui(self):

        # USERNAME
        self.user_box = QLabel(
            f"USER: {self.username}", self
        )
        self.user_box.setGeometry(850, 18, 200, 42)
        self.user_box.setAlignment(Qt.AlignCenter)

        self.user_box.setStyleSheet(f"""
            color:white;
            background:#d100ff;
            border:2px solid #ff44ff;
            font-size:10px;
            font-family:{self.pixel_font};
        """)
        self.glow(self.user_box, "#ff00ff", 220)

        # LEFT LOGO
        self.left_logo = QLabel(self)
        pix1 = QPixmap("HHBK_LOGO_1.png").scaled(
            180, 180,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.left_logo.setPixmap(pix1)
        self.left_logo.setGeometry(300, 130, 180, 180)
        self.glow(self.left_logo, "#00ffff", 300)

        # RIGHT LOGO
        self.right_logo = QLabel(self)
        pix2 = QPixmap("JORMOS.png").scaled(
            180, 180,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.right_logo.setPixmap(pix2)
        self.right_logo.setGeometry(610, 130, 180, 180)
        self.glow(self.right_logo, "#ff00ff", 300)

        # X
        self.cross = QLabel("×", self)
        self.cross.setGeometry(520, 210, 50, 40)
        self.cross.setAlignment(Qt.AlignCenter)

        self.cross.setStyleSheet(f"""
            color:#88aaff;
            font-size:28px;
            font-family:{self.pixel_font};
            background:transparent;
        """)
        self.glow(self.cross, "#88aaff", 150)

        # TITLE
        self.title = QLabel("STRATEGIC GAMES", self)
        self.title.setGeometry(220, 355, 640, 50)
        self.title.setAlignment(Qt.AlignCenter)

        self.title.setStyleSheet(f"""
            color:#7185ff;
            font-size:34px;
            font-family:{self.title_font};
            font-weight:900;
            letter-spacing:4px;
            background:transparent;
        """)
        self.glow(self.title, "#7185ff", 220)

        # SUBTITLE
        self.sub = QLabel(
            "DENKEN. SPIELEN. GEWINNEN", self
        )
        self.sub.setGeometry(180, 415, 720, 30)
        self.sub.setAlignment(Qt.AlignCenter)

        self.sub.setStyleSheet(f"""
            color:#33eaff;
            font-size:12px;
            font-family:{self.pixel_font};
            background:transparent;
        """)
        self.glow(self.sub, "#33eaff", 160)

        # BUTTONS
        self.make_btn("▸ START GAME ◂", 560, "#45e6ff")
        self.make_btn("★ LEADERBOARD ★", 640, "#ff00ff")
        self.make_btn("✕ EXIT ✕", 720, "#ff0033", True)

    # =====================================
    # BUTTON
    # =====================================
    def make_btn(self, text, y, color, close_btn=False):

        btn = QPushButton(text, self)
        btn.setGeometry(330, y, 420, 52)

        btn.setStyleSheet(f"""
            QPushButton {{
                background-color:{color};
                color:white;
                border:2px solid {color};
                font-size:13px;
                font-family:{self.pixel_font};
                font-weight:bold;
            }}

            QPushButton:hover {{
                background-color:#ff00ff;
                border:2px solid #ff66ff;
                color:white;
            }}

            QPushButton:pressed {{
                background-color:#ff33ff;
                color:white;
            }}
        """)

        self.glow(btn, color, 340)

        if close_btn:
            btn.clicked.connect(self.close)

    # =====================================
    # GLOW
    # =====================================
    def glow(self, widget, color, blur):
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(blur)
        effect.setOffset(0, 0)
        effect.setColor(QColor(color))
        widget.setGraphicsEffect(effect)

    # =====================================
    # BACKGROUND
    # =====================================
    def paintEvent(self, event):

        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor("#040014"))

        painter.setPen(Qt.NoPen)

        painter.setBrush(QColor(0, 255, 255, 35))
        painter.drawEllipse(-250, -50, 650, 650)

        painter.setBrush(QColor(255, 0, 255, 30))
        painter.drawEllipse(700, 120, 500, 700)

        painter.setBrush(QColor(0, 180, 255, 18))
        painter.drawEllipse(360, 470, 340, 340)

        pen = QPen(QColor("#0b3a55"))
        pen.setWidth(1)
        painter.setPen(pen)

        for x in range(0, self.width(), 18):
            painter.drawLine(x, 0, x, self.height())

        for y in range(0, self.height(), 18):
            painter.drawLine(0, y, self.width(), y)

        # PIXELS
        pink_pixels = [
            (60, 100), (140, 220), (250, 650),
            (940, 80), (980, 340), (820, 900)
        ]

        for px, py in pink_pixels:
            painter.fillRect(px, py, 8, 8, QColor("#ff00ff"))

        cyan_pixels = [
            (130, 50), (310, 800), (760, 120),
            (1010, 620)
        ]

        for px, py in cyan_pixels:
            painter.fillRect(px, py, 8, 8, QColor("#00ffff"))


# =====================================
# START
# =====================================
app = QApplication(sys.argv)

window = MainMenu()
window.show()

sys.exit(app.exec())
