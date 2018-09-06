import matplotlib.pyplot as plt
import numpy as np

##Input N data points as a 2D list or array
##and the function will perform an N-degree
##polynomial fit of the data. Will excluded singluar
##value matrix results.
def CurveFit(points):

    if type(points) == type(list()):
        points = np.array(points)

    for i in range(len(points)):
        for j in range(len(points)):
            if (i != j and (points[i] == points[j]).all()) or (i != j and points[i][0] == points[j][0]):
                print("Singular value matrix solution")
                return False

    num_vars = points.shape[0]

    A = np.zeros((points.shape[0], num_vars))
    b = np.zeros((points.shape[0], 1))

    for i,point in enumerate(points):
        A[i] = np.array([point[0]**j for j in list(range(0, num_vars))[::-1]])
        b[i] = point[1]

    for point in points:
        plt.scatter(point[0], point[1])

    coefficients = np.linalg.solve(A, b)

    x = np.linspace(points.min(), points.max(), 100) if abs(points.min()) > points.max() else np.linspace(-points.max(), points.max(), 100)
    y = np.zeros_like(x)
    for j,i in zip(list(range(0, num_vars))[::-1], range(coefficients.shape[0])):
        y += coefficients[i]*x**j

    plt.plot(x, y)

    plt.show()

    return A, b, coefficients
