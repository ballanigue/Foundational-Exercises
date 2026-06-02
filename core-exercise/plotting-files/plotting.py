import numpy as np
import matplotlib.pyplot as plt

#Data points to be plotted
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

#Another set of data points
xpoints2 = np.array([1, 2, 6, 8])
ypoints2 = np.array([3, 8, 1, 10])

#Plot and display
plt.plot(xpoints, ypoints, 'o-')
      #display points only: 'o'
      #display points and lines: 'o-'
plt.show()    #This line is necessary to separate the plots that you want
              #to display. As long as this line does not appear, all graphs
              #will be contained in one plot.


plt.plot(xpoints, ypoints, 'o-r')
plt.plot(xpoints2, ypoints2, 's--b')
plt.show()

#Format data point size
plt.plot(xpoints, ypoints, 'o-r', ms = 20)
plt.plot(xpoints2, ypoints2, 's--b', ms = 5)
plt.show()

#Format linewidth
plt.plot(xpoints, ypoints, 'o-r', lw = 5)
plt.plot(xpoints2, ypoints2, 's--b', ms = 5, lw = 2)
plt.show()

#Labels and Title
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y, 'o-k', linestyle='--', marker='^', linewidth=3)

plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

#format labels and title
'''
family: serif, sans-serif, monospace
color: (see documentation for complete list)
size: any number'''
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'sans-serif','color':'red','size':15}
font3 = {'family':'monospace','color':'green','size':10}
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font3)
plt.title("Sports Watch Data", loc = 'right', fontdict=font1)

plt.show()
