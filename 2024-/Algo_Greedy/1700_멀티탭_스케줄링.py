import sys


def input_data():
    n, k = map(int, sys.stdin.readline().split())
    machines = list(map(int, sys.stdin.readline().split()))
    machine_count = {i: 0 for i in range(1, k + 1)}
    for machine in machines:
        machine_count[machine] += 1

    return n, k, machines, machine_count


def solve(n, k, machines, machine_count):
    pluged = 0
    unpluged = 0
    plug = [-1] * (k + 1)

    for machine in machines:
        if pluged < n:
            machine_count[machine] -= 1
            pluged += 1
            plug[machine] = machine_count[machine]
        else:
            if plug[machine] != -1:
                if plug[machine] != 0:
                    plug[machine] -= 1
                machine_count[machine] -= 1
            else:
                min_i = k+1
                min_count = k+1
                tmp_count = 0

                for m_i, c in enumerate(plug):
                    if c == -1:
                        continue
                    else:
                        if min_count >= c:
                            min_i = m_i


if __name__ == "__main__":
    n, k, machines, machine_count = input_data()
    solve(n, k, machines, machine_count)
