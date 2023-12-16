#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def zero(*args):
    if args:
        v = [float(arg) for arg in args]
        p = 1
        z1 = 0
        z2 = 0
        if 0 in v:
         z1 = v.index(0)
         z2 = v.index(0, z1+1)
         for arg in v[z1+1:z2]:
             p *= arg 
        else:
            return None
        return p
    else:
        return None


if __name__ == "__main__":
    print(zero(0, 8, 9, 0, 7, 4))
    print(zero())
    print(zero(2, 9, 0, 6, 1, 8, 9, 4, 2, 9, 0))
    print(zero(9, 8, 5, 2, 9, 5, 1, 9, 4))
