# Particle Suspension Volume Calculator (PS_Mag-Rechner)

A lightweight Python GUI application built with **Tkinter** to streamline laboratory workflow calculations. It computes the required stock suspension volume ($\mu L$) to achieve a specific monolayer particle coverage in experimental cell structures.

![App Interface]<img width="624" height="728" alt="ps_mag" src="https://github.com/user-attachments/assets/5b8adb4b-e329-4c7a-b3f6-ca3e192f1ef2" />


## Key Features


* **Physical & Geometric Calculations:**
  * Computes cross-sectional areas of particles and experimental cells.
  * Estimates particle capacity assuming an optimal 2D packing fraction ($90\%$).
  * Calculates individual particle volume and mass from material density ($\text{g/cm}^3$).
  * Scales outputs according to concentration percentage ($\% w/v$) and injection volumes.
* **Error Prevention:** Includes `try-except` validation blocks to handle invalid inputs gracefully.

## Mathematical Logic

1. **Cell & Particle Footprint:**
   $$F_{\text{cell}} = \pi \cdot r_{\text{cell}}^2$$
   $$F_{\text{particle}} = \pi \cdot r_{\text{particle}}^2$$
2. **Monolayer Capacity:** Assumes $90\%$ max packing efficiency ($F_{\text{monolayer}} = 0.9 \cdot F_{\text{cell}}$).
3. **Particle Mass:** Computed using 3D sphere volume and mass density:
   $$V_{\text{particle}} = \frac{4}{3} \pi r^3$$
4. **Stock Volume:** Solves for total mass and converts it into required stock solution microliters ($\mu L$).

## Requirements & Usage

### Prerequisites
* **Python 3.x** (Tkinter comes pre-installed with standard Python packages).

### Running the Application
1. Download or clone this repository.
2. Run the script via terminal or IDE:
   ```bash
   python ps_mag_rechner.py
