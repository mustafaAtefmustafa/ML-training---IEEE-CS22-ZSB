import sys


def main():
    n = int(input("Enter the number of unkowns: "))
    print("Enter the coefficients of the augmanted matrix ")

    arr = []
    sol = [0] * n
    for i in range(n):
        arr.append(list(map(int, input().split())))

    # Gaussian Elimination Algorithm:
    for i in range(n):
        if arr[i][i] == 0:
            sys.exit("Division by zero")
        for j in range(i+1, n):
            ratio = arr[j][i] / arr[i][i]
            for k in range(n+1):
                arr[j][k] = arr[j][k] - ratio * arr[i][k]

    # Back substitution
    sol[n-1] = arr[n-1][n] / arr[n-1][n-1]
    for i in range(n-2, -1, -1):
        sol[i] = arr[i][n]

        for j in range(i+1, n):
            sol[i] = sol[i] - arr[i][j] * sol[j]
        sol[i] = sol[i] / arr[i][i]

    # display the solution:
    for i in range(n):
        print(f"X[{i}] = {sol[i]}")


if __name__ == '__main__':
    main()
