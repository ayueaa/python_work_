from random import choice
class Randomwalk():
    def __init__(self,num_point=5000):
        self.num_point=num_point
        self.x_value=[0]
        self.y_value=[0]
    def fill_walk(self):
        while len(self.x_value)<self.num_point:
            x_direction=choice([1,-1])
            x_distance=choice([0,1,2,3,4])
            x_step=x_direction*x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3,4])
            y_step = y_direction * y_distance

            if x_step==0 and y_step==0:
                continue

            next_x=self.x_value[-1]+x_step
            next_y=self.y_value[-1]+y_step
            self.x_value.append(next_x)
            self.y_value.append(next_y)

import matplotlib.pyplot as plt
import time
start=time.time()
rw=Randomwalk(100000)
rw.fill_walk()
point_number=list(range(rw.num_point))
plt.scatter(rw.x_value,rw.y_value,c=point_number,edgecolors="none",s=1)
plt.scatter(0,0,c="red",edgecolors="none",s=50)
plt.scatter(rw.x_value[-1],rw.y_value[-1],c="black",edgecolors="none",s=50)
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.show()
end=time.time()
time=end-start
print("运行时间为{}".format(time))