import matplotlib.pyplot as plt
x_value=list(range(1,1001))
y_valve=[x**2 for x in x_value]
plt.scatter(x_value,y_valve,c=y_valve,cmap=plt.cm.Reds,edgecolors="none",s=40)
plt.title("square numbers",fontsize=24)
plt.xlabel("valve",fontsize=14)
plt.ylabel("square value",fontsize=14)
plt.tick_params(axis="both",which="major",labelsize=14)
plt.savefig("Squares_plot.png",bbox_inches="tight")