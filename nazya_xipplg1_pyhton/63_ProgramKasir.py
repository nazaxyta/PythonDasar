import tkinter as tk

# Fungsi untuk menghitung total harga
def hitung_total():
    harga = float(entry_harga.get())
    kuantitas = int(entry_kuantitas.get())
    total = harga * kuantitas
    label_total.config(text=f"Total Harga: Rp {total}")

# Membuat jendela Tkinter
root = tk.Tk()
root.title("Program Kasir")

# Label untuk input harga
label_harga = tk.Label(root, text="Harga Barang:")
label_harga.pack()

entry_harga = tk.Entry(root)
entry_harga.pack()

# Label untuk input kuantitas
label_kuantitas = tk.Label(root, text="Kuantitas Barang:")
label_kuantitas.pack()

entry_kuantitas = tk.Entry(root)
entry_kuantitas.pack()

# Tombol untuk menghitung total
tombol_hitung = tk.Button(root, text="Hitung Total", command=hitung_total)
tombol_hitung.pack()

# Label untuk menampilkan total harga
label_total = tk.Label(root, text="Total Harga: Rp 0")
label_total.pack()

# Menjalankan loop utama Tkinter
root.mainloop()