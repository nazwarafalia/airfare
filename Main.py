import tkinter as tk
from tkinter import messagebox

# Function to handle booking process
def pesan():
    jmlh_tiket = int(jmlh_tiket_entry.get())
    num_array = []
    num = int(num_penumpang_entry.get())
    for i in range(num):
        n = f"Orang ke {i + 1}"
        num_array.append(n)
    total_tiket = jmlh_tiket * harga
    result = f"Nama Pemesan:\n" + "\n".join(num_array) + f"\n\nTotal Harga: Rp.{total_tiket:,}"
    messagebox.showinfo("Pemesanan Berhasil", result)

# Function to select destination and price
def pilih_tujuan():
    global harga
    tujuan = int(tujuan_var.get())
    if tujuan == 1:
        harga = 1500000
    elif tujuan == 2:
        harga = 975000
    elif tujuan == 3:
        harga = 920000
    elif tujuan == 4:
        harga = 750000
    else:
        harga = 0
    pesan()

# Main window
app = tk.Tk()
app.title("Travelio Booking")
app.configure(bg='#F0F8FF')

# Title Label
title_label = tk.Label(app, text="Travelio Book Flight Ticket", font=("Helvetica", 16, "bold"), bg='#4682B4', fg='white', pady=10)
title_label.grid(row=0, column=0, columnspan=2, sticky="ew")

# Destination Selection
tk.Label(app, text="Pilih Tujuan:", font=("Helvetica", 12), bg='#F0F8FF').grid(row=1, column=0, sticky="w", padx=10, pady=5)
tujuan_var = tk.IntVar()
tk.Radiobutton(app, text="Jakarta", variable=tujuan_var, value=1, font=("Helvetica", 12), bg='#F0F8FF').grid(row=2, column=0, sticky="w", padx=10)
tk.Radiobutton(app, text="Bandung", variable=tujuan_var, value=2, font=("Helvetica", 12), bg='#F0F8FF').grid(row=3, column=0, sticky="w", padx=10)
tk.Radiobutton(app, text="Yogyakarta", variable=tujuan_var, value=3, font=("Helvetica", 12), bg='#F0F8FF').grid(row=4, column=0, sticky="w", padx=10)
tk.Radiobutton(app, text="Surabaya", variable=tujuan_var, value=4, font=("Helvetica", 12), bg='#F0F8FF').grid(row=5, column=0, sticky="w", padx=10)

# Input Fields for Number of Tickets and Passengers
tk.Label(app, text="Jumlah Tiket:", font=("Helvetica", 12), bg='#F0F8FF').grid(row=6, column=0, sticky="w", padx=10, pady=5)
jmlh_tiket_entry = tk.Entry(app, font=("Helvetica", 12))
jmlh_tiket_entry.grid(row=6, column=1, padx=10, pady=5)

tk.Label(app, text="Jumlah Penumpang:", font=("Helvetica", 12), bg='#F0F8FF').grid(row=7, column=0, sticky="w", padx=10, pady=5)
num_penumpang_entry = tk.Entry(app, font=("Helvetica", 12))
num_penumpang_entry.grid(row=7, column=1, padx=10, pady=5)

# Button to Confirm Booking
pesan_button = tk.Button(app, text="Pesan", command=pilih_tujuan, font=("Helvetica", 12, "bold"), bg='#4682B4', fg='white', padx=10, pady=5)
pesan_button.grid(row=8, column=0, columnspan=2, pady=10)

# Adjust spacing and alignment
for widget in app.winfo_children():
    widget.grid_configure(padx=10, pady=5)

app.mainloop()