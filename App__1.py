import tkinter as tk
from tkinter import messagebox
import math

SCALE_FACTOR = 250

class MapCalculationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator Hărți - Scara 1:25000")
        self.root.configure(bg="#1e1e1e")

        label_style = {"bg": "#1e1e1e", "fg": "#dcdcdc"}
        entry_style = {"bg": "#1e1e1e", "fg": "#00ff00", "insertbackground": "#00ff00"}

        self.coord_frame = tk.Frame(root, padx=10, pady=10, bg="#1e1e1e")
        self.coord_frame.grid(row=0, column=0)

        tk.Label(self.coord_frame, text="Latitudine Punct 1:", **label_style).grid(row=0, column=0)
        self.lat1_entry = tk.Entry(self.coord_frame, **entry_style)
        self.lat1_entry.grid(row=0, column=1)

        tk.Label(self.coord_frame, text="Longitudine Punct 1:", **label_style).grid(row=1, column=0)
        self.lon1_entry = tk.Entry(self.coord_frame, **entry_style)
        self.lon1_entry.grid(row=1, column=1)

        tk.Label(self.coord_frame, text="Cota Punct 1 (m):", **label_style).grid(row=2, column=0)
        self.alt1_entry = tk.Entry(self.coord_frame, **entry_style)
        self.alt1_entry.grid(row=2, column=1)

        tk.Label(self.coord_frame, text="Latitudine Punct 2:", **label_style).grid(row=3, column=0)
        self.lat2_entry = tk.Entry(self.coord_frame, **entry_style)
        self.lat2_entry.grid(row=3, column=1)

        tk.Label(self.coord_frame, text="Longitudine Punct 2:", **label_style).grid(row=4, column=0)
        self.lon2_entry = tk.Entry(self.coord_frame, **entry_style)
        self.lon2_entry.grid(row=4, column=1)

        tk.Label(self.coord_frame, text="Cota Punct 2 (m):", **label_style).grid(row=5, column=0)
        self.alt2_entry = tk.Entry(self.coord_frame, **entry_style)
        self.alt2_entry.grid(row=5, column=1)
        self.calculate_button = tk.Button(self.coord_frame, text="Calculează", command=self.calculate, bg="#007acc",
                                          fg="#ffffff")
        self.calculate_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.result_frame = tk.Frame(root, padx=10, pady=10, bg="#1e1e1e")
        self.result_frame.grid(row=1, column=0)
        self.result_label = tk.Label(self.result_frame, text="", justify="left", bg="#1e1e1e", fg="#dcdcdc")
        self.result_label.pack()


        self.result_text = tk.Text(self.result_frame, height=8, width=40, bg="#1e1e1e", fg="#00ff00")
        self.result_text.pack()

    def calculate(self):
        try:

            lat1 = float(self.lat1_entry.get())
            lon1 = float(self.lon1_entry.get())
            alt1 = float(self.alt1_entry.get())

            lat2 = float(self.lat2_entry.get())
            lon2 = float(self.lon2_entry.get())
            alt2 = float(self.alt2_entry.get())


            distance_horizontal = self.calculate_horizontal_distance(lat1, lon1, lat2, lon2)
            distance_inclined = self.calculate_inclined_distance(distance_horizontal, alt1, alt2)
            slope = self.calculate_slope(distance_horizontal, alt1, alt2)


            result_text = f"Distanța Orizontală: {distance_horizontal:.2f} m\n"
            result_text += f"Distanța Înclinată: {distance_inclined:.2f} m\n"
            result_text += f"Panta: {slope:.2f}%"

            self.result_label.config(text=result_text)
            self.result_text.delete(1.0, tk.END)  # Curățare text anterior
            self.result_text.insert(tk.END, result_text)

        except ValueError:
            messagebox.showerror("Eroare", "Introduceți valori numerice valide pentru toate câmpurile!")

    def calculate_horizontal_distance(self, lat1, lon1, lat2, lon2):
        delta_lat = (lat2 - lat1) * SCALE_FACTOR
        delta_lon = (lon2 - lon1) * SCALE_FACTOR
        distance = math.sqrt(delta_lat ** 2 + delta_lon ** 2)
        return distance

    def calculate_inclined_distance(self, horizontal_distance, alt1, alt2):
        delta_alt = alt2 - alt1
        inclined_distance = math.sqrt(horizontal_distance ** 2 + delta_alt ** 2)
        return inclined_distance

    def calculate_slope(self, horizontal_distance, alt1, alt2):
        # Calculul pantei în procente (%)
        delta_alt = alt2 - alt1
        if horizontal_distance == 0:
            return 0
        slope = (delta_alt / horizontal_distance) * 100
        return slope

root = tk.Tk()
app = MapCalculationApp(root)
root.mainloop()
