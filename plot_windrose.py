" Example wind rose subplots"

import numpy as np
import matplotlib.pyplot as plt
from windrose import WindroseAxes


# Specify filename to create windrose from


wind_speeds = np.array([12,10,13,15])
wind_dirs = np.array([60,76,32,80]) # in degrees


wind_speeds_bins = np.histogram(wind_speeds, 5)[1]

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='windrose')
ax1.bar(wind_dirs ,wind_speeds, normed=True, opening=0.8, edgecolor='white', bins=wind_speeds_bins)
ax1.set_title('test')

ax1.legend(bbox_to_anchor=(1.2 , -0.1))
plt.tight_layout()
plt.show()
