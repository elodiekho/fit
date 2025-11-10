import numpy as np
from lmfit import models
import matplotlib.pyplot as plt

from method import parabolic_fit, parabolic_function, methode

meto = methode()
print(meto.maximum(300, 700))

# #create new figure
# plt.figure()

# #create plot with fit
# plt.plot(x_section, y_section,'o')
# plt.plot(x_section, fit_result.best_fit, 'r-')
# plt.show()
