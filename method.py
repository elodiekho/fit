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
    model_gauss = models.GaussianModel()

    pars = model_gauss.guess(y, x = xvalues)

    params = model_gauss.param_names
    independent_variables = model_gauss.independent_vars
    # params = model_gauss.make_params(
    #         center = centervalue,
    #         sigma = sigmavalue,
    #         amplitude = amplitudevalue)
    
    #use model to fit
    fit_result = model_gauss.fit(y, pars, x = xvalues)

    return fit_result


def parabolic_fit(y, xvalues, avalue, bvalue):
    #create model
    mod_parabolic = models.Model(parabolic_function)
    
    # use model to fit
    fit_result = mod_parabolic.fit(y, x = xvalues, a = avalue, b = bvalue)

    #return fit results
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

        print(count_section)
        print(max(count_section))
        print(height_section)
        print(count_section)
        print(min_x)
        print(max_x)
        
        fit_result = gaussian_fit(np.array(count_section), np.array(height_section))
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
meto.maximum_gauss(float(600),float(1100))
    


# #create new figure
# plt.figure()

# #create plot with fit
# plt.plot(x_section, y_section,'o')
# plt.plot(x_section, fit_result.best_fit, 'r-')
# plt.show()