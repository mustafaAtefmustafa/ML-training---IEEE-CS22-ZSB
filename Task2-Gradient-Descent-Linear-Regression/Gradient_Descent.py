import csv
import matplotlib.pyplot as plt
import random


def main():
    # Load dataset
    x = []
    y = []
    alpha = 0.0005
    theta_0 = random.random()
    theta_1 = random.random()

    with open("dataset.csv", 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        for row in csv_reader:
            x.append(float(row[0]))
            y.append(float(row[1]))
    m = len(x)
    # Apply the algorithm
    # Gradient Descent
    for i in range(100):
        # theta0
        sum_0 = 0
        for i in range(m):
            sum_0 += (theta_0 + (theta_1 * x[i])) - y[i]
        temp_0 = theta_0 - alpha * (1 / m) * sum_0

        # theta1
        sum_1 = 0
        for i in range(m):
            sum_1 += ((theta_0 + (theta_1 * x[i])) - y[i]) * x[i]
        temp_1 = theta_1 - alpha * (1 / m) * sum_1

        # Update theta_0 and theta_1
        theta_0 = temp_0
        theta_1 = temp_1

    # plot
    plt.plot(x, y, 'bo')
    result = []
    for i in x:
        result.append(theta_0 + theta_1 * i)
    plt.plot(x, result, color="red")
    plt.show()


if __name__ == '__main__':
    main()
