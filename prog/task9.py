#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def garmonic(*args):
    if args:
        v = [float(arg) for arg in args]
        sum = 0
        for arg in v:
            sum += 1 / arg
        return len(args) / sum
    else:
        return None
    

if __name__ == "__main__":
    print(garmonic(6, 7, 8, 9, 4))
    print(garmonic())
