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

# Disclaimer
This experiment uses raw data from 30 NOAA stations with over 100 years of continuous observations to compute annual means and verify whether the global warming trend emerges without filtering or complex models.

## Methodological limitations:
– No area weighting:
The selected stations do not fully represent the global land surface distribution, so the computed mean does not reflect an exact global average temperature.

– No homogenization:
No corrections are applied for instrumental changes, site relocations, or urban heat island effects, which may introduce noise into the data. However, such local variations do not erase the long-term climate trend.

– Partial series:
Some historical periods may have incomplete coverage or a varying number of available stations, which can slightly influence annual means.

– Does not replace official datasets:
Datasets like HadCRUT5, GISTEMP, and Berkeley Earth apply data quality controls, homogenization, and area weighting to robustly estimate global temperatures. This experiment does not replace these datasets but qualitatively checks whether their observed trends are visible in raw data.

## Why this experiment is useful:
– It demonstrates that the global warming trend is clearly visible even in raw data, without corrections or complex models, countering the claim that the signal is an artifact of data processing.

– It allows anyone to verify in a simple and transparent way that global warming is real and observable in the primary data.

– It serves as an educational starting point for those wishing to explore climate datasets independently.
