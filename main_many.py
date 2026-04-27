import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

# =========================
# Fenster
# =========================
root = tk.Tk()
root.title("JORMOS DAME")
root.geometry("1300x950")
root.configure(bg="#040014")
root.resizable(False, False)

# =========================
# Farben
# =========================
bg = "#040014"
panel = "#07001d"
blue = "#66F2FF"
pink = "#ff00ff"
white = "#ffffff"
purple = "#21003f"
dark1 = "#090018"
dark2 = "#1a0835"

# =========================
# Logo laden OHNE Pixel Effekt
# =========================
img = Image.open("JORMOS.png")
img = img.resize((220, 220), Image.LANCZOS)
logo_img = ImageTk.PhotoImage(img)

# =========================
# Layout
# =========================
left = tk.Frame(root, bg=panel, width=280, height=950)
left.pack(side="left", fill="y")
left.pack_propagate(False)

right = tk.Frame(root, bg=panel, width=220, height=950)
right.pack(side="right", fill="y")
right.pack_propagate(False)

center = tk.Frame(root, bg=bg)
center.pack(fill="both", expand=True)

# =========================
# LINKS
# =========================
tk.Label(left, image=logo_img, bg=panel).pack(pady=25)

tk.Label(
    left,
    text="THINK SMART. PLAY JORMOS.",
    fg=pink,
    bg=panel,
    font=("Consolas", 11, "bold")
).pack(pady=(0, 25))

def left_button(text):
    tk.Button(
        left,
        text=text,
        fg=blue,
        bg=purple,
        activebackground=pink,
        activeforeground=white,
        font=("Consolas", 15, "bold"),
        width=16,
        height=2,
        bd=2,
        relief="groove",
        cursor="hand2"
    ).pack(pady=10)

left_button("PLAY")
left_button("GAMES")
left_button("LEADERBOARD")
left_button("SETTINGS")
left_button("EXIT")

# =========================
# TITEL
# =========================
top = tk.Frame(center, bg=panel, height=110)
top.pack(fill="x", padx=20, pady=20)
top.pack_propagate(False)

title_frame = tk.Frame(top, bg=panel)
title_frame.pack(expand=True)

tk.Label(
    title_frame,
    text="JORMOS ",
    fg=blue,
    bg=panel,
    font=("Arial Black", 30)
).pack(side="left")

tk.Label(
    title_frame,
    text="DAME",
    fg=pink,
    bg=panel,
    font=("Arial Black", 30)
).pack(side="left")

# =========================
# Spielfeld
# =========================
canvas = tk.Canvas(
    center,
    width=720,
    height=560,
    bg=panel,
    highlightbackground=blue,
    highlightthickness=3
)
canvas.pack()

cell = 80
ox = 120
oy = 35

# Brett
for row in range(6):
    for col in range(6):
        x1 = ox + col * cell
        y1 = oy + row * cell
        x2 = x1 + cell
        y2 = y1 + cell

        color = dark1 if (row + col) % 2 == 0 else dark2

        canvas.create_rectangle(
            x1, y1, x2, y2,
            fill=color,
            outline="#1d1d45"
        )

# Pink Steine
for row in range(2):
    for col in range(6):
        if (row + col) % 2 == 1:
            x = ox + col * cell + 40
            y = oy + row * cell + 40
            canvas.create_oval(
                x-24, y-24, x+24, y+24,
                fill=pink,
                outline=white,
                width=2
            )

# Blaue Steine
for row in range(4, 6):
    for col in range(6):
        if (row + col) % 2 == 1:
            x = ox + col * cell + 40
            y = oy + row * cell + 40
            canvas.create_oval(
                x-24, y-24, x+24, y+24,
                fill=blue,
                outline=white,
                width=2
            )

# Auswahlfeld
canvas.create_rectangle(
    ox + 3*cell,
    oy + 3*cell,
    ox + 4*cell,
    oy + 4*cell,
    outline=blue,
    width=3
)

# =========================
# Buttons unter Brett
# =========================
bottom = tk.Frame(center, bg=bg)
bottom.pack(pady=18)

def bottom_btn(text):
    tk.Button(
        bottom,
        text=text,
        fg=blue,
        bg=panel,
        activebackground=pink,
        activeforeground=white,
        font=("Consolas", 14, "bold"),
        width=15,
        height=2,
        bd=2,
        relief="groove"
    ).pack(side="left", padx=10)

bottom_btn("GAMES")
bottom_btn("SETTINGS")
bottom_btn("LEADERBOARD")

# =========================
# RECHTS
# =========================
def side_box(text, color):
    tk.Label(
        right,
        text=text,
        fg=color,
        bg=purple,
        font=("Consolas", 15, "bold"),
        width=13,
        height=3,
        bd=2,
        relief="groove"
    ).pack(pady=20)

side_box("TURN\nYOUR TURN", blue)
side_box("DIFFICULTY\nMEDIUM", pink)
side_box("RULES", white)
side_box("SURRENDER", white)

# Start

root.mainloop()
