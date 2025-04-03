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

    for i, machine in enumerate(machines):
        machine_count[machine][0] += 1
        heapq.heappush(machine_count[machine][1], i)

    return n, k, machines, machine_count


def solve(n, k, machines, machine_count):
    plugged = 0
    unplugged = 0
    plug = [-1] * (k + 1)

    for machine in machines:
        # print(machine)
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
                latest_machine = k + 1
                # min_count = k + 1
                tmp_count = 0

                for m_i, c in enumerate(plug):
                    if c == -1:
                        continue
                    else:
                        if c == 0:
                            latest_machine = m_i
                            break

                        if latest_machine == k+1:
                            latest_machine = m_i

                        if machine_count[latest_machine][1][0] < machine_count[m_i][1][0]:
                            latest_machine = m_i
                        tmp_count += 1
                        if tmp_count == n:
                            break
                plug[latest_machine] = -1
                machine_count[machine][0] -= 1
                plug[machine] = machine_count[machine][0]
                heapq.heappop(machine_count[machine][1])
                unplugged += 1
        # curr_tmp = []
        # for i in range(1, k + 1):
        #     if plug[i] != -1:
        #         curr_tmp.append(i)
        # print(curr_tmp)

    print(unplugged)


if __name__ == "__main__":
    n, k, machines, machine_count = input_data()
    solve(n, k, machines, machine_count)
