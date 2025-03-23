import sys
from collections import deque


def input_data():
    n = int(sys.stdin.readline())
    distances = list(map(int, sys.stdin.readline().split()))
    gas_station = deque(map(int, sys.stdin.readline().split()))

    return n, distances, gas_station


def solve(n, distances, gas_station):
    plan = []
    min_gas = float('inf')

    for i, gas in enumerate(gas_station):
        if i == n - 1: break

        if gas < min_gas:
            plan.append([gas, distances[i]])
            min_gas = gas
        else:
            plan[-1][1] += distances[i]

    total_fee = 0
    for gas, distance in plan:
        total_fee += gas * distance

    print(total_fee)


if __name__ == "__main__":
    n, distances, gas_station = input_data()
    solve(n, distances, gas_station)
