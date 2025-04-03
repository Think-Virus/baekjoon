import sys
import heapq


def input_data():
    n, k = map(int, sys.stdin.readline().split())
    machines = []
    machine_count = {i: [0, []] for i in range(1, k + 1)}
    pre_machine = 0
    for machine in map(int, sys.stdin.readline().split()):
        if machine != pre_machine:
            machines.append(machine)
            pre_machine = machine

    for machine in machines:
        machine_count[machine][0] += 1
        heapq.heappush(machine_count[machine][1], machine)

    return n, k, machines, machine_count


def solve(n, k, machines, machine_count):
    plugged = 0
    unplugged = 0
    plug = [-1] * (k + 1)

    for machine in machines:
        if plugged < n:
            machine_count[machine][0] -= 1
            heapq.heappop(machine_count[machine][1])
            plugged += 1
            plug[machine] = machine_count[machine][0]
        else:
            if plug[machine] != -1:
                if plug[machine] != 0:
                    plug[machine] -= 1
                machine_count[machine][0] -= 1
                heapq.heappop(machine_count[machine][1])
            else:
                min_i = k + 1
                min_count = k + 1
                tmp_count = 0

                for m_i, c in enumerate(plug):
                    if c == -1:
                        continue
                    else:
                        if min_count > c:
                            min_i = m_i
                            min_count = c
                        elif min_count == c:
                            if c == 0:
                                continue
                            if machine_count[min_i][1][0] > machine_count[m_i][1][0]:
                                min_i = m_i
                        tmp_count += 1
                        if tmp_count == n:
                            break
                plug[min_i] = -1
                machine_count[machine][0] -= 1
                plug[machine] = machine_count[machine][0]
                heapq.heappop(machine_count[machine][1])
                unplugged += 1

    print(unplugged)


if __name__ == "__main__":
    n, k, machines, machine_count = input_data()
    solve(n, k, machines, machine_count)
