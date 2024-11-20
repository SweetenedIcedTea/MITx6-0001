import math
import sys

def polysum(n: int, s: int)-> float:
    if n < 3:
        sys.exit("A polygon must have 3 or more sides")
    pi = math.pi
    area = (0.25*n*s**2)/(math.tan(pi/n))
    perm = n*s
    return round(area + perm**2, 4)

def main():
    print(polysum(5, 3))
    return 0

if __name__ == "__main__":
    main()