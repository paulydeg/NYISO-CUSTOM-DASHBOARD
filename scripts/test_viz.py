from nyisotoolkit import NYISOData
import pandas as pd
import matplotlib.pyplot as plt

# Fetch data for January 2024
data = NYISOData(dataset='load_h', year='2024').df
data.index = pd.to_datetime(data.index)
data = data.tz_convert('US/Eastern')
january_data = data.loc['2024-01']

# Plot the hourly load data
plt.figure(figsize=(12, 6))
plt.plot(january_data.index, january_data['Load'], label='Hourly Load')
plt.title('Hourly Load Data for January 2024 (NYISO)', fontsize=16)
plt.xlabel('Date and Time', fontsize=12)
plt.ylabel('Load (MW)', fontsize=12)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
