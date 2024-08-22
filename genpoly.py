import numpy as np
import math
from collections import deque

def remove_part_set(gruops, total, in_poly, b, index):
    # Use a stack to simulate recursion
    stack = deque([(gruops.copy(), total, in_poly.copy(), b, index)])

    while stack:
        gruops, total, in_poly, b, index = stack.pop()
        if b:
            if total == 0:
                print('in_poly from removing')
                print(in_poly)
                # print('total is=', total)
                continue
            elif total == 1:
                in_poly[2] += 1
                print('totoal is 1 in_poly from remove set')
                # print(gruops)
                print(in_poly)
                continue
            elif total < 0:
                print('tot<0')
                continue
        else:
            # if all 1 continu
            # print('gruops')
            # print(gruops)
            # print(total)
            if max(gruops[:len(gruops) - 2]) == 1:
                continue
            else:
                for i in range(len(gruops) - 2):
                    gruops[i] = min(gruops[len(gruops) - 1], gruops[i])

                if index < len(gruops) - 1 and gruops[index] > 1:
                    ngruops, ntotal, nin_poly = gruops.copy(), total, in_poly.copy()

                    gruops[index] -= 1

                    for j in range(len(nin_poly)):
                        nin_poly[j] -= math.comb(gruops[i], j)
                    total += gruops[i] * (gruops[i] - 1) / 2

                    stack = deque([(ngruops, ntotal, nin_poly, True, index)])
                if index < len(gruops) - 2 and gruops[index + 1] > 1:
                    ngruops, ntotal, nin_poly, index = gruops.copy(), total, in_poly.copy(), index + 1

                    gruops[index] -= 1

                    for j in range(len(nin_poly)):
                        nin_poly[j] -= math.comb(gruops[i], j)
                    total += gruops[i] * (gruops[i] - 1) / 2

                    stack = deque([(ngruops, ntotal, nin_poly, True, index)])


def add_set(gruops, total, in_poly):
    # Use a stack to simulate the recursion
    stack = deque([(gruops.copy(), total, in_poly.copy())])

    while stack:
        gruops, total, in_poly = stack.pop()

        if total == 0:
            print('in_poly middle from add set')
            print(in_poly)
            continue
        elif total == 1:
            in_poly[2] += 1
            print('totoal is 1 in_poly from add set')
            # print(gruops)
            print(in_poly)
            continue
        elif total < 0:
            print('tot<0')
            continue
        elif total > 1:

            add_size = int((1 + math.sqrt(1 + 8 * total)) / 2)
            ngruops, ntotal, nin_poly = gruops.copy(), total, in_poly.copy()
            for i in range(add_size):
                nin_poly[i] += math.comb(add_size, i)
            ngruops.append(add_size)
            ntotal -= add_size * (add_size - 1) // 2
            remove_part_set(ngruops, ntotal, nin_poly, False, 0)
            stack.append((ngruops, ntotal, nin_poly))

            if len(gruops) > 2 and gruops[len(gruops) - 1] > 2:
                size = gruops[len(gruops) - 1]
                ngruops, ntotal, nin_poly = gruops.copy(), total, in_poly.copy()
                for i in range(size):
                    nin_poly[i] -= math.comb(size, i)
                ntotal += size * (size - 1) // 2
                ngruops[len(gruops) - 1] -= 1
                size -= 1
                for i in range(size):
                    nin_poly[i] += math.comb(size, i)
                ntotal -= size * (size - 1) // 2
                remove_part_set(ngruops, ntotal, nin_poly, False, 0)
                stack.append((ngruops, ntotal, nin_poly))

            # ngruops, ntotal, nin_poly = gruops, total, in_poly
            # ngruops.append(add_size)
            stack.append((ngruops, ntotal, nin_poly))


def main():
    n = 7
    total = (n - 2) * (n - 1) / 2

    for k in range(1, n // 2 + 1):
        print('k is ', k)
        in_poly = np.array([math.comb(k, i) + math.comb(n - k, i) for i in range(n)])
        total = total - (k * (k - 1) / 2) - ((n - k) * (n - k - 1) / 2)

        gruops = [k, n - k]
        new_groupes = gruops.copy()
        new_total = total
        new_in_poly = in_poly
        if total == 0:
            print('in_poly main')
            print(in_poly)
        elif total == 1:
            in_poly[2] += 1
            print('totoal is 1 in_poly main')
            print(in_poly)
        elif total < 0:
            print('tot<0')
        elif total > 1:
            add_set(new_groupes, new_total, new_in_poly)

        total = (n - 2) * (n - 1) / 2


if __name__ == '__main__':
    main()
