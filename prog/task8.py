#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def geometric(*args):
    if args:
        v = [float(arg) for arg in args]
        p = 1
        for arg in v:
            p *= arg
        return p ** (1 / len(v))
    else:
        return None
    

if __name__ == "__main__":
    print(geometric(9, 5, 6, 7, 3))