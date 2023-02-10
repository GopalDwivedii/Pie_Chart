import matplotlib.pyplot as plt

a = [23, 7, 67, 8, 90, 13, 34]
b = [45, 34, 6, 7, 9, 19, 36]
c = ['apple', 'banana', 'mango', 'papaya', 'guava', 'strawberry', 'pineapple']
e = [0, 0, 0.1, 0, 0.11, 0, 0]
plt.pie(a, labels=c, shadow=True, explode=e)
plt.show()
