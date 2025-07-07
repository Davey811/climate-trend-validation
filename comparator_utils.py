import pandas as pd

def parse_dly(file_path):
    """
    Parse a GHCN-D .dly file, extract Tmax and Tmin, and compute daily mean temperature.
    """
    records = []
    with open(file_path, "r") as f:
        for line in f:
            year = int(line[11:15])
            month = int(line[15:17])
            element = line[17:21]
            if element in ["TMAX", "TMIN"]:
                for day in range(31):
                    value = int(line[21 + day * 8:26 + day * 8])
                    if value != -9999:
                        records.append({
                            "year": year,
                            "month": month,
                            "day": day + 1,
                            "element": element,
                            "value": value / 10
                        })
    df = pd.DataFrame(records)
    if df.empty:
        return pd.DataFrame()
    df_pivot = df.pivot_table(index=["year", "month", "day"], columns="element", values="value")
    df_pivot["TAVG"] = df_pivot[["TMAX", "TMIN"]].mean(axis=1)
    df_pivot = df_pivot.reset_index()
    return df_pivot
