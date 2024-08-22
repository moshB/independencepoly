import math
import sys
from collections import deque

sys.setrecursionlimit(15000)


def remove_part_set(gruops, total, in_poly):

    stack = deque([(gruops, total, in_poly.copy())])
    # print('removeset')
    while stack:
        # print('while rm')
        gruops, total, in_poly = stack.pop()
        if total == 0:
            print('total=0')
            print('in_poly from removing')
            print(in_poly)
            continue
        for i in range(len(gruops)):
            if gruops[i] > 1:
                gruops[i] -= 1
                for gr in gruops:
                    gr = int(gr)
                    for j in range(gr + 1):
                        in_poly[j] -= math.comb(gr, j)
                    total += gr * (gr - 1) / 2
                    stack.append((gruops.copy(), total, in_poly.copy()))


def add_set(gruops, total, in_poly, add_size):
    print('add set')
    stack = deque([(gruops, total, in_poly.copy(), add_size)])
    while stack:
        gruops, total, in_poly, add_size = stack.pop()
        if total == 0:
            print('in_poly middle')
            print(in_poly)
            continue
        if total > 0:
            gruops.append(add_size)
            add_size = int(add_size)
            for i in range(add_size + 1):
                in_poly[i] += math.comb(add_size, i)
            total -= add_size * (add_size - 1) / 2

            gruopscopy = gruops.copy()
            in_polycopy = in_poly.copy()

            remove_part_set(gruops, total, in_poly)

            if add_size > 0:
                stack.append((gruopscopy, total, in_polycopy, add_size))
                gruops.pop()
                for i in range(add_size + 1):
                    in_poly[i] -= math.comb(add_size, i)
                total += add_size * (add_size - 1) / 2
                stack.append((gruops, total, in_polycopy, add_size - 1))
            else:
                # print('add . .else')
                # print(total)
                stack.append((gruopscopy, total, in_polycopy, total+1))
                # print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
                total = int(total)
                for i in range(total + 2):
                    in_poly[i] -= math.comb(total+1, i)
                total += (total+1) * (total+1 - 1) / 2


def main():
    n = 6
    total = (n - 2) * (n - 1) / 2

    for k in range(1, n // 2 + 1):
        in_poly = [math.comb(k, i) + math.comb(n - k, i) for i in range(n)]
        total = total - (k * (k - 1) / 2) - ((n - k) * (n - k - 1) / 2)
        gruops = [k, n - k]

        for t in range(2, n - 2 + 1):
            gruops.append(t)
            for i in range(t + 1):
                in_poly[i] += math.comb(t, i)
                total -= t * (t - 1) / 2
            if total == 0:
                print('in_poly for the first')
                print(in_poly)

            for s in range(1, k - 1 + 1):
                for j in range(1, max(s, t - s) + 1):
                    if s * (s - 1) / 2 + (t - s) * (t - s - 1) / 2 <= total:
                        in_poly[t] -= math.comb(s, j)
                        if t - s >= 0:
                            in_poly[t] -= math.comb(t - s, j)
                        total += s * (s - 1) / 2 + (t - s) * (t - s - 1) / 2
                        if total == 0:
                            print('in_poly')
                            print(in_poly)
                        else:
                            total = int(total)
                            add_set(gruops, total, in_poly, total)
                        in_poly[t] += math.comb(s, j)
                        if t - s >= 0:
                            in_poly[t] += math.comb(t - s, j)
                        total -= s * (s - 1) / 2 + (t - s) * (t - s - 1) / 2

            for i in range(t + 1):
                in_poly[t] -= math.comb(t, i)
                total += t * (t - 1) / 2
            gruops.pop()

        total = (n - 2) * (n - 1) / 2


if __name__ == '__main__':
    main()
