import tkinter as tk
import math

# =========================
# FUNGSI
# =========================
def klik(nilai):
    entry.insert(tk.END, nilai)

def clear():
    entry.delete(0, tk.END)

def hapus():
    entry.delete(len(entry.get())-1, tk.END)

def hitung():
    try:
        ekspresi = entry.get()
        ekspresi = ekspresi.replace("^", "**")
        hasil = eval(ekspresi)
        entry.delete(0, tk.END)
        entry.insert(0, str(hasil))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def akar():
    try:
        nilai = float(entry.get())
        hasil = math.sqrt(nilai)
        entry.delete(0, tk.END)
        entry.insert(0, str(hasil))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def persen():
    try:
        nilai = float(entry.get())
        hasil = nilai / 100
        entry.delete(0, tk.END)
        entry.insert(0, str(hasil))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# =========================
# GUI
# =========================
root = tk.Tk()
root.title("Kalkulator Pro")
root.geometry("320x500")
root.configure(bg="#1e1e1e")

entry = tk.Entry(root, font=("Arial", 24), bd=10, relief=tk.FLAT,
                 bg="#2d2d2d", fg="white", justify="right")
entry.pack(fill="both", padx=10, pady=10, ipady=10)

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(expand=True, fill="both")

def buat_tombol(text, command, bg="#3a3a3a"):
    return tk.Button(frame, text=text, font=("Arial", 16),
                     command=command, bg=bg, fg="white",
                     activebackground="#555", relief=tk.FLAT)

tombol = [
    ('C', clear), ('⌫', hapus), ('%', persen), ('/', lambda: klik('/')),
    ('7', lambda: klik('7')), ('8', lambda: klik('8')), ('9', lambda: klik('9')), ('*', lambda: klik('*')),
    ('4', lambda: klik('4')), ('5', lambda: klik('5')), ('6', lambda: klik('6')), ('-', lambda: klik('-')),
    ('1', lambda: klik('1')), ('2', lambda: klik('2')), ('3', lambda: klik('3')), ('+', lambda: klik('+')),
    ('√', akar), ('0', lambda: klik('0')), ('.', lambda: klik('.')), ('=', hitung),
]

row = 0
col = 0

for (text, cmd) in tombol:
    btn = buat_tombol(text, cmd)
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

for i in range(5):
    frame.rowconfigure(i, weight=1)
for i in range(4):
    frame.columnconfigure(i, weight=1)

root.mainloop()