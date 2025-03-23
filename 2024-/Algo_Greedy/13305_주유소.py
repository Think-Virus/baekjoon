import sys


def input_data():
    n = int(sys.stdin.readline())
    distances = list(map(int, sys.stdin.readline().split()))
    gas_station = list(map(int, sys.stdin.readline().split()))

    return n, distances, gas_station


def solve(n, distances, gas_station):
    # cheapest = min(gas_station)
    total_fee = 0

    curr_gas = gas_station[0]
    going_distance = 0
    for i in range(n - 2):
        if curr_gas <= gas_station[i + 1]:
            going_distance += distances[i]
        else:
            if going_distance:
                total_fee += going_distance * curr_gas
            else:
                total_fee += distances[i] * curr_gas
            curr_gas = gas_station[i + 1]

            going_distance = 0

    total_fee += curr_gas * (going_distance + distances[n - 2])

    print(total_fee)


if __name__ == "__main__":
    n, distances, gas_station = input_data()
    solve(n, distances, gas_station)
