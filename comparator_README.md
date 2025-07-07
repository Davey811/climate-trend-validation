# Centennial Climate Verification

This repository shows, with open raw data, that **global warming is measurable, consistent, and real** — even using only **Centennial weather stations** with over 100 years of daily records.

## What we did

- Downloaded raw `.dly` daily temperature files from NOAA GHCN-D for **30 Centennial-like stations**.
- Computed daily mean temperatures: **(Tmax + Tmin) / 2**.
- Calculated annual mean temperatures for each station.
- Combined them into an unweighted global annual mean.
- Visualized the global trend.
- Compared the raw trend with HadCRUT, GISTEMP, and Berkeley Earth datasets.

## Key result

The raw Centennial data shows a warming trend of **+0.38 °C per decade**, consistent with major global datasets.

**No adjustments, no hidden models, no filtering — only raw station data.**

## How to replicate

1. Clone this repository.
2. Place `.dly` files in the `data/` folder.
3. Run:
   ```bash
   pip install -r requirements.txt
   python main.py
   ```
4. The script will:
   - Parse all `.dly` files.
   - Generate the global annual mean CSV.
   - Plot the trend and save the figure.

## Files

- `main.py` — Main script for processing the dataset.
- `utils.py` — Helper functions for `.dly` parsing and annual mean calculation.
- `requirements.txt` — Python dependencies.
- `outputs/` — Contains the final CSV and plot.

## License

Public domain. Use for climate communication and open science.
