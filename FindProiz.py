#!/usr/bin/env python3
# -*- encoding: utf-8
if __name__ == "__main__":
    mylst = list(map(int, input().split()))
    proiz = 1
    for i in mylst:
        if i>0:
            proiz=proiz * i
    print(proiz)


