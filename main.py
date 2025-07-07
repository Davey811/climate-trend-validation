import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.stats import linregress
from utils import parse_dly

def main():
    data_dir = Path("./data")
    all_data = []

    for file in data_dir.glob("*.dly"):
        df_station = parse_dly(file)
        if not df_station.empty:
            df_station["station"] = file.stem
            all_data.append(df_station)

    df_all = pd.concat(all_data, ignore_index=True)
    df_annual_station = df_all.groupby(["station", "year"])["TAVG"].mean().reset_index()
    df_annual_global = df_annual_station.groupby("year")["TAVG"].mean().reset_index()

    slope, intercept, *_ = linregress(df_annual_global["year"], df_annual_global["TAVG"])
    trend_per_decade = slope * 10

    plt.figure(figsize=(10, 6))
    plt.plot(df_annual_global["year"], df_annual_global["TAVG"], marker="o", color="black", label="Centennial Raw (Model)")
    plt.plot(
        df_annual_global["year"],
        intercept + slope * df_annual_global["year"],
        color="red",
        linestyle="--",
        label=f"Trend: {trend_per_decade:.2f} °C/decade"
    )
    plt.xlabel("Year")
    plt.ylabel("Global Annual Mean Temperature (°C)")
    plt.title("Global Annual Mean Temperature (Raw, Centennial Stations)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    Path("outputs").mkdir(exist_ok=True)
    df_annual_global.to_csv("outputs/centennial_annual_mean_temperature.csv", index=False)
    plt.savefig("outputs/centennial_trend_plot.png", dpi=300)
    print(f"Done. Trend: {trend_per_decade:.3f} °C/decade")

if __name__ == "__main__":
    main()
