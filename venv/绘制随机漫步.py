import matplotlib.pyplot as plt
from random_walk import RandomWalk
rw=RandomWalk()
rw.fill_walk()
point_numbers=list(range(rw.num_points))
plt.scatter(rw.x_valve,rw.y_valve,c=point_numbers,cmap=plt.cm.Reds,edgecolors="none",s=1)
plt.scatter(0,0,c="green",edgecolors="none",s=100)
plt.scatter(rw.x_valve[-1],rw.y_valve[-1],c="blue",edgecolors="none",s=100)
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.show()