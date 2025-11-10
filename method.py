import numpy as np
from lmfit import models
import matplotlib.pyplot as plt

from controll import data_import

# define parabolic function
def parabolic_function(x, a, b):
    y = a * ((x - b) ** 2)
    return y


# sigma 50 amplitude 1500
def gaussian_fit(y, xvalues):
    # create model
    y = np.asarray(y, dtype=float)
    x = np.asarray(xvalues, dtype=float)

    model_gauss = models.GaussianModel()
    initial_parameters = model_gauss.make_params(
        center=np.mean(x),
        sigma=(np.max(x) - np.min(x)) / 6,
        amplitude=np.max(y)
    )

    fit_result = model_gauss.fit(y, params=initial_parameters, x=x)

    return fit_result



class methode:
    
    def __init__(self):
        self.height, self.counts = data_import('datana22.csv')


    def maximum_gauss(self, min_x, max_x):

        count_section = []
        height_section = []

        for h, c in zip(self.height, self.counts):
            if  max_x > h > min_x:
                count_section.append(c)
                height_section.append(h)

        
        fit_result = gaussian_fit(count_section, height_section)
        print(fit_result.fit_report())

        max_y = max(fit_result.best_fit)

        #create new figure
        plt.figure()

        #create plot with fit
        plt.plot(height_section, count_section,'o')
        plt.ylim(0,3000)
        plt.plot(height_section, fit_result.best_fit, 'r-')
        plt.show()

        return max_y
    
meto = methode()
# print(meto.maximum(600, 1100))
print(meto.maximum_gauss(600,1100))
    


# #create new figure
# plt.figure()

# #create plot with fit
# plt.plot(x_section, y_section,'o')
# plt.plot(x_section, fit_result.best_fit, 'r-')
# plt.show()