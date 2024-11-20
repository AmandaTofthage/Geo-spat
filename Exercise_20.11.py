import numpy as np
import matplotlib.pyplot as plt

# Dataset 1: 
depth_m = np.array([10, 20, 30, 40, 50, 60, 80, 90, 100])
temperature_C = np.array([15, 16.5, 18, 19.5, 21, 22.5, 24, 25.5, 27, 28.5])

# Dataset 2
precipitation_mm = np.array([50, 75, 60, 90, 55, 85, 65, 95, 70, 80])
soil_ph = np.array([6.8, 7.0, 6.9, 6.5, 7.2, 6.6, 7.1, 6.4, 6.8, 7.0])

# Variance
var_temp = np.var(temperature_C)
var_soil_ph = np.var(soil_ph)

# Covariance
cov_temp_depth = np.cov(depth_m, temperature_C)[0, 1]
cov_precip_soil_ph = np.cov(precipitation_mm, soil_ph)[0, 1]

# Correlation
corr_temp_depth = np.corrcoef(depth_m, temperature_C)[0, 1]
corr_precip_soil_ph = np.corrcoef(precipitation_mm, soil_ph)[0, 1]

# Results
print("Dataset 1 (Depth vs Temperature):")
print(f"Variance (Temperature): {var_temp:.2f}")
print(f"Covariance: {cov_temp_depth:.2f}")
print(f"Correlation: {corr_temp_depth:.2f}")

print("\nDataset 2 (Precipitation vs Soil pH):")
print(f"Variance (Soil pH): {var_soil_ph:.2f}")
print(f"Covariance: {cov_precip_soil_ph:.2f}")
print(f"Correlation: {corr_precip_soil_ph:.2f}")

# Scatter plots
plt.figure(figsize=(10, 5))

# Dataset 1
plt.subplot(1, 2, 1)
plt.scatter(depth_m, temperature_C, color='blue', label='Dataset 1')
plt.title("Depth vs Temperature")
plt.xlabel("Depth (m)")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()

# Dataset 2
plt.subplot(1, 2, 2)
plt.scatter(precipitation_mm, soil_ph, color='green', label='Dataset 2')
plt.title("Precipitation vs Soil pH")
plt.xlabel("Precipitation (mm)")
plt.ylabel("Soil pH")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
