import numpy as np
from lmfit import models
import matplotlib.pyplot as plt



def data_import(filename):
    # assign empty list for pulseheight and counts
    height = []
    counts = []

    # open fle in read mode
    with open(f'{filename}', 'r', newline='') as file:

        #to skip header
        #read and discard first line of file
        next(file)

        N = 0
        for line in file:
            N = N + 1
            #split column
            line_splitted = line.split(',')

            if N != 1:
                #convert data to float
                #append data to list
                height.append(float(line_splitted[0]))
                counts.append(float(line_splitted[1]))
        
    return height, counts

height, counts = data_import('datana22.csv')


#create new figure
plt.figure()

#create plot with fit
plt.plot(height, counts,'o')
plt.show()