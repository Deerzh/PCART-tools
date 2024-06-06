import numpy as np

def main():
    data = np.ma.array([[3, 2, 1], [6, 5, 4], [9, 8, 7]], mask=[[False, False, False], [False, True, False], [False, False, True]])
    sorted_indices = np.ma.argsort(a=data, axis=1, kind='quicksort', order=None, endwith=True)
    print('Original masked array:')
    print(data)
    print('Sorted indices along axis 1:')
    print(sorted_indices)
if __name__ == '__main__':
    main()