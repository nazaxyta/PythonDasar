import turtle as t

# Fungsi untuk menggambar lingkaran
def draw_circle(radius, color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Atur tampilan awal
t.speed(1)
t.bgcolor("white")

# Gambar lingkaran luar (lingkaran besar) dengan latar belakang putih
draw_circle(100, "white")

# Gambar lingkaran dalam (lingkaran kecil) dengan latar belakang biru
draw_circle(40, "blue")

# Sembunyikan turtle
t.hideturtle()

# Tahan tampilan hingga di-klik
t.done()
