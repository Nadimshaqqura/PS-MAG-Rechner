import tkinter as tk
from tkinter import messagebox
import math

def calculate():
    try:
        # Get inputs
        d_particle = float(entry_d_particle.get()) # um
        dichte_particle = float(entry_dichte_particle.get()) # g/cm3
        d_zelle = float(entry_d_zelle.get())       # mm
        wv = float(entry_wv.get())                 # g/100ml
        volumen_prope = float(entry_vol_prope.get()) # um (microliters)
        anteil_zelle_str = entry_anteil.get()      # e.g., 1/3
        volumen_inj = float(entry_vol_inj.get())   # um (microliters)

        # Parse fraction for anteil_zelle
        if '/' in anteil_zelle_str:
            num, den = map(float, anteil_zelle_str.split('/'))
            anteil_zelle = num / den
        else:
            anteil_zelle = float(anteil_zelle_str)

        # MATLAB Logic Implementation
        # F_zelle = 3.14 * (d_zelle * 10^-3)^2
        f_zelle = math.pi * (d_zelle * 1e-3)**2
        
        # F_particle = 3.14 * (d_particle * 10^-6)^2
        f_particle = math.pi * (d_particle * 1e-6)**2
        
        f_monolage = 0.9 * f_zelle
        anzahl_monolage = f_monolage / f_particle
        
        # volumen_inj = Vol_inj * 10^-9 (microliters to m3)
        vol_inj_m3 = volumen_inj * 1e-9
        
        anzahldichte_inj = anzahl_monolage / vol_inj_m3
        
        # Volumen_partikel = (4/3) * 3.14 * (d_particle * 10^-6 / 2)^3 (m3)
        volumen_partikel = (4/3) * math.pi * (d_particle * 1e-6 / 2)**3
        
        # masse_partikel = Volumen_partikel * dichte_particle * 10^6 (g)
        masse_partikel = volumen_partikel * dichte_particle * 1e6
        
        # n_prope = Anzahldichte_inj * Volumen_prope * 10^-9 * anteil_zelle
        n_prope = anzahldichte_inj * volumen_prope * 1e-9 * anteil_zelle
        
        # masse_prope = masse_partikel * n_prope
        masse_prope = masse_partikel * n_prope
        
        # volumen_Stamm = masse_prope * 100 * 1000 / wv
        volumen_stamm = masse_prope * 100 * 1000 / wv
        
        label_result.config(text=f"Volumen Stammsuspension: {volumen_stamm:.4f} µl")

    except Exception as e:
        messagebox.showerror("Fehler", f"Ungültige Eingabe: {str(e)}")

# GUI Setup
root = tk.Tk()
root.title("PS_Mag-Rechner v3")
root.geometry("500x550")

fields = [
    ("Durchmesser Partikel (µm):", "18"),
    ("Massendichte Partikel (g/cm³):", "1.6"),
    ("Durchmesser Zelle (mm):", "20"),
    ("wv (%):", "5"),
    ("Volumen Probe (µl):", "500"),
    ("Anteil zu bedeckenden Fläche der Zelle (z.B. 1/3):", "1/3"),
    ("Volumen Injektion (µl):", "30")
]

entries = {}

for i, (label_text, default_val) in enumerate(fields):
    tk.Label(root, text=label_text).pack(pady=(10, 0))
    entry = tk.Entry(root)
    entry.insert(0, default_val)
    entry.pack()
    entries[label_text] = entry

entry_d_particle = entries["Durchmesser Partikel (µm):"]
entry_dichte_particle = entries["Massendichte Partikel (g/cm³):"]
entry_d_zelle = entries["Durchmesser Zelle (mm):"]
entry_wv = entries["wv (%):"]
entry_vol_prope = entries["Volumen Probe (µl):"]
entry_anteil = entries["Anteil zu bedeckenden Fläche der Zelle (z.B. 1/3):"]
entry_vol_inj = entries["Volumen Injektion (µl):"]

btn_calc = tk.Button(root, text="Berechnen", command=calculate)
btn_calc.pack(pady=20)

label_result = tk.Label(root, text="Volumen Stammsuspension: -", font=("Arial", 10, "bold"))
label_result.pack()

root.mainloop()
