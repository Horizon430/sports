import matplotlib.pyplot as plt

#background color
plt.rcParams['axes.facecolor']='tab:blue'

#out side of court
plt.plot([0,0],[0,46],color="white")
plt.plot([0,88],[46,46],color="white")
plt.plot([88,88],[46,0],color="white")
plt.plot([0,88],[0,0],color="white")

#court

plt.plot([5,5],[5,41], color="white")
plt.plot([5,83],[41,41], color="white")
plt.plot([5,83],[5,5], color="white")
plt.plot([83,83],[5,41], color="white")

plt.plot([5,83],[36.5,36.5], color="white")
plt.plot([5,83],[9.5,9.5], color="white")
plt.plot([23,23],[9.5,36.5], color="white")
plt.plot([65,65],[9.5,36.5], color="white")

plt.plot([23,65],[23,23], color="white")
plt.plot([44,44],[5,41], color="white")

plt.show()
