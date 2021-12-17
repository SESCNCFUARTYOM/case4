#!/usr/bin/env python3
# -*- encoding: utf-8
if __name__ == "__main__":
    a = list(map(int, input().split()))
    a_max = a.index(max(a))
    a[0], a[a_max] = a[a_max], a[0]
    print(a)

