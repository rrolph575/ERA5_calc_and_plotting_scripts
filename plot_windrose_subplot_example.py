" Example wind rose subplots"

import numpy as np
import matplotlib.pyplot as plt
from windrose import WindroseAxes

wind_speeds1 = np.array([12,10,13,15])
wind_dirs1 = np.array([60,76,32,80]) # in degrees

wind_speeds2 = np.array([23,12,10,8])
wind_dirs2 = np.array([23,45,29,13])

wind_speeds_bins = np.histogram(wind_speeds2, 5)[1]

fig = plt.figure()
ax1 = fig.add_subplot(121, projection='windrose')
ax1.bar(wind_dirs1 ,wind_speeds1, normed=True, opening=0.8, edgecolor='white', bins=wind_speeds_bins)
ax1.set_title('test')
ax2 = fig.add_subplot(122, projection='windrose')
ax2.bar(wind_dirs2, wind_speeds2, normed=True, opening=0.8, edgecolor='white', bins=wind_speeds_bins)

# ax1.legend()
ax2.legend(bbox_to_anchor=(1.2 , -0.1))
plt.tight_layout()
plt.show()
