#!/usr/bin/env python3
# -*- encoding: utf-8
if __name__ == "__main__":
    lst = list(map(int, input().split()))
    lst_min = lst.index(min(lst))
    lst[-1], lst[lst_min] = lst[lst_min], lst[-1]
    print(lst)


