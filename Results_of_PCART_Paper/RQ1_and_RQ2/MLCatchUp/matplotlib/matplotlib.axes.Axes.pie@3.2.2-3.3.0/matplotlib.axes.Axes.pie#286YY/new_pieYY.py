import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(sizes, explode, labels, colors, '%1.1f%%', 0.85, True, 1.05, 90, counterclock=False, data=None, wedgeprops={'edgecolor': 'black'}, textprops={'color': 'white'}, frame=True, rotatelabels=True, radius=False, center=(0, 0), normalize=None)