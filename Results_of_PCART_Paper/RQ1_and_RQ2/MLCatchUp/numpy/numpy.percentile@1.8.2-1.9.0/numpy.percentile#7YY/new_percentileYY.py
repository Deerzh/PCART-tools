import numpy as np

def main():
    data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    p25 = np.percentile(a=data, q=25, axis=None, interpolation='linear', keepdims=False)
    print('25th percentile:', p25)
if __name__ == '__main__':
    main()
