import tkinter as tk
from tkinter import messagebox, Canvas
from datetime import datetime

def calcul_julian_date(year, month, day, hour, minute, second):
    if month <= 2:
        year -= 1
        month += 12
    JD = int(365.25 * year) + int(30.6001 * (month + 1)) + day + (hour + minute / 60 + second / 3600) / 24 + 1720981.5
    MJD = JD - 2400000.5
    return JD, MJD

def invers_julian_to_gregorian(JD):
    a = int(JD + 0.5)
    b = a + 1537
    c = int((b - 122.1) / 365.25)
    d = int(365.25 * c)
    e = int((b - d) / 30.6001)
    day = b - d - int(30.6001 * e)
    month = e - 1 - 12 * int(e / 14)
    year = c - 4715 - int((7 + month) / 10)
    return year, month, day

def calcul_zi_saptamana(JD):
    return int(JD + 0.5) % 7

def calcul_gps_week(JD):
    if 2444244.5 <= JD <= 2451412.5:
        GPSWEEK = int((JD - 2444244.5) / 7)
    elif 2451412.5 < JD <= 2458580.5:
        GPSWEEK = int((JD - 2451412.5) / 7)
    elif JD > 2458580.5:
        GPSWEEK = int((JD - 2458580.5) / 7)
    else:
        GPSWEEK = None
    return GPSWEEK

def calcul_secunda(gps_week_day, hour, minute, second):
    sec_day = hour * 3600 + minute * 60 + second
    sec_week = gps_week_day * 86400 + sec_day
    return sec_day, sec_week

def calcul():
    try:
        year = int(entry_year.get())
        month = int(entry_month.get())
        day = int(entry_day.get())
        hour = int(entry_hour.get())
        minute = int(entry_minute.get())
        second = int(entry_second.get())

        JD, MJD = calcul_julian_date(year, month, day, hour, minute, second)
        year_rev, month_rev, day_rev = invers_julian_to_gregorian(JD)
        zi_sapt = calcul_zi_saptamana(JD)
        gps_week = calcul_gps_week(JD)
        gps_day = zi_sapt
        sec_day, sec_week = calcul_secunda(zi_sapt, hour, minute, second)

        # Afisarea rezultatelor in widget-ul Text
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"JD: {JD:.2f}\nMJD: {MJD:.2f}\n")
        result_text.insert(tk.END, f"Data inversă: {day_rev}-{month_rev}-{year_rev}\n")
        result_text.insert(tk.END, f"Ziua săptămânii (0=L, ..., 6=D): {zi_sapt}\n")
        result_text.insert(tk.END, f"Săptămâna GPS: {gps_week}\n")
        result_text.insert(tk.END, f"Secunda zilei: {sec_day}\n")
        result_text.insert(tk.END, f"Secunda săptămânii: {sec_week}")
    except ValueError:
        messagebox.showerror("Eroare", "Introduceți valori numerice valide pentru toate câmpurile.")

# Interfața grafică
root = tk.Tk()
root.title("Sisteme de localizare prin GPS")
root.geometry("600x400")
root.configure(bg="#1E1E1E")


canvas = Canvas(root, width=120, height=120, bg="#1E1E1E", highlightthickness=0)
canvas.grid(row=0, column=2, rowspan=5, padx=10)

# Cerc pentru glob
canvas.create_oval(10, 10, 110, 110, fill="#4CAF50", outline="white")  # Verde pământ și contur alb

# Linii pentru longitudini și latitudini
for i in range(20, 100, 20):
    canvas.create_line(10, i, 110, i, fill="white", width=1)  # paralele
    canvas.create_line(i, 10, i, 110, fill="white", width=1)  # meridiane

canvas.create_line(60, 10, 60, 110, fill="blue", width=2)  # Meridian central albastru
canvas.create_line(10, 60, 110, 60, fill="blue", width=2)  # Ecuator albastru

# Etichete și casete de introducere
label_fg = "white"  # Culoare text albă pentru contrast cu fondul gri
tk.Label(root, text="Ziua", bg="#1E1E1E", fg=label_fg).grid(row=0, column=0, sticky="w")
entry_day = tk.Entry(root)
entry_day.grid(row=0, column=1, pady=5)

tk.Label(root, text="Luna", bg="#1E1E1E", fg=label_fg).grid(row=1, column=0, sticky="w")
entry_month = tk.Entry(root)
entry_month.grid(row=1, column=1, pady=5)

tk.Label(root, text="Anul", bg="#1E1E1E", fg=label_fg).grid(row=2, column=0, sticky="w")
entry_year = tk.Entry(root)
entry_year.grid(row=2, column=1, pady=5)

tk.Label(root, text="Ora", bg="#1E1E1E", fg=label_fg).grid(row=3, column=0, sticky="w")
entry_hour = tk.Entry(root)
entry_hour.grid(row=3, column=1, pady=5)

tk.Label(root, text="Minut", bg="#1E1E1E", fg=label_fg).grid(row=4, column=0, sticky="w")
entry_minute = tk.Entry(root)
entry_minute.grid(row=4, column=1, pady=5)

tk.Label(root, text="Secundă", bg="#1E1E1E", fg=label_fg).grid(row=5, column=0, sticky="w")
entry_second = tk.Entry(root)
entry_second.grid(row=5, column=1, pady=5)

# Rezultate și buton
btn_calcul = tk.Button(root, text="Calculează", command=calcul, bg="#444444", fg="white", relief="raised")
btn_calcul.grid(row=6, column=0, columnspan=2, pady=10)

# Zonă mare pentru rezultate
result_text = tk.Text(root, height=10, width=50, bg="#252526", fg="white", relief="flat")
result_text.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
