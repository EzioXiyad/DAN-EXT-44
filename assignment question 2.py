
import os, shutil

os.makedirs("temperatures", exist_ok=True)


for file in os.listdir():
    if file.endswith(".csv"):
        shutil.move(file, f"temperatures/{file}")

import glob
all_files = glob.glob("temperatures/*.csv")
print("Found files:", all_files[:5])  # show first 5

all_files = glob.glob("temperatures/*.csv")

import os
import pandas as pd
import numpy as np


folder_path = "temperatures"

all_data = pd.DataFrame()


for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)
        all_data = pd.concat([all_data, df], ignore_index=True)

months = ['January','February','March','April','May','June','July','August','September','October','November','December']

for month in months:
    all_data[month] = pd.to_numeric(all_data[month], errors='coerce')

print(all_data.head())

seasons = {
    "Summer": ['December','January','February'],
    "Autumn": ['March','April','May'],
    "Winter": ['June','July','August'],
    "Spring": ['September','October','November']
}

seasonal_avg = {}

for season, season_months in seasons.items():
    # Flatten all temperature values for the season
    temp_values = all_data[season_months].values.astype(float).flatten()
    # Remove NaN values
    temp_values = temp_values[~np.isnan(temp_values)]
    # Calculate mean
    seasonal_avg[season] = round(np.mean(temp_values), 2)

with open("average_temp.txt", "w") as f:
    for season, avg in seasonal_avg.items():
        f.write(f"{season}: {avg}°C\n")

print("Seasonal averages calculated and saved to average_temp.txt")
print(seasonal_avg)

range_list = []

for _, row in all_data.iterrows():
    station_name = row['STATION_NAME']
    # Convert row values to float to avoid TypeError
    temps = row[months].astype(float).values
    temps = temps[~np.isnan(temps)]  # Remove NaNs
    if len(temps) > 0:
        temp_range = np.max(temps) - np.min(temps)
        range_list.append((station_name, temp_range, np.max(temps), np.min(temps)))

max_range_value = max(range_list, key=lambda x: x[1])[1]


max_range_stations = [r for r in range_list if r[1] == max_range_value]


with open("largest_temp_range_station.txt", "w") as f:
    for station in max_range_stations:
        f.write(f"Station {station[0]}: Range {station[1]:.1f}°C "
                f"(Max: {station[2]:.1f}°C, Min: {station[3]:.1f}°C)\n")

print("Largest temperature range calculated and saved to largest_temp_range_station.txt")

std_list = []

for _, row in all_data.iterrows():
    station_name = row['STATION_NAME']
    # Convert temperatures to float and remove NaNs
    temps = row[months].astype(float).values
    temps = temps[~np.isnan(temps)]
    if len(temps) > 0:
        std_dev = np.std(temps)
        std_list.append((station_name, std_dev))

min_std_value = min(std_list, key=lambda x: x[1])[1]
max_std_value = max(std_list, key=lambda x: x[1])[1]

most_stable_stations = [s for s in std_list if s[1] == min_std_value]
most_variable_stations = [s for s in std_list if s[1] == max_std_value]

with open("temperature_stability_stations.txt", "w") as f:
    for s in most_stable_stations:
        f.write(f"Most Stable: Station {s[0]}: StdDev {s[1]:.1f}°C\n")
    for s in most_variable_stations:
        f.write(f"Most Variable: Station {s[0]}: StdDev {s[1]:.1f}°C\n")

print("Temperature stability calculated and saved to temperature_stability_stations.txt")

std_list = []

for _, row in all_data.iterrows():
    station_name = row['STATION_NAME']
    # Convert temperatures to float and remove NaNs
    temps = row[months].astype(float).values
    temps = temps[~np.isnan(temps)]
    if len(temps) > 0:
        std_dev = np.std(temps)
        std_list.append((station_name, std_dev))

min_std_value = min(std_list, key=lambda x: x[1])[1]
max_std_value = max(std_list, key=lambda x: x[1])[1]

most_stable_stations = [s for s in std_list if s[1] == min_std_value]
most_variable_stations = [s for s in std_list if s[1] == max_std_value]


with open("temperature_stability_stations.txt", "w") as f:
    for s in most_stable_stations:
        f.write(f"Most Stable: Station {s[0]}: StdDev {s[1]:.1f}°C\n")
    for s in most_variable_stations:
        f.write(f"Most Variable: Station {s[0]}: StdDev {s[1]:.1f}°C\n")

print("Temperature stability calculated and saved to temperature_stability_stations.txt")