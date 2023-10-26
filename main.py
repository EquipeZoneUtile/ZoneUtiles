from icecream import ic
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

rectangle = plt.Rectangle((1,1), 4, 4)
ax.add_patch(rectangle)
ic(ax)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ic(ax.get_xlim())
plt.show()
