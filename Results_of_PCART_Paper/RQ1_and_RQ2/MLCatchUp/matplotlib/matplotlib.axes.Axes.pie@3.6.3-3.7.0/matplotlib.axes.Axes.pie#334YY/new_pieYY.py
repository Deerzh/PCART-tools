import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, None, ['A', 'B', 'C', 'D'], None, '%1.1f%%', 0.6, startangle=90, labeldistance=1.1, normalize=True, radius=1, wedgeprops=None, counterclock=True, shadow=False, hatch=None)