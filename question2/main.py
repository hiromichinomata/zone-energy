#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  is_prime = [True] * 10001
  for i in range(2, 10000):
    for j in range(i*2, 10000, i):
      is_prime[j] = False

  is_prime[1] = False

  result = 0
  for _ in range(20):
    arr = list(map(int, input().strip().split()))
    for num in arr:
      if is_prime[num]:
        result += 1
  print(result)

main()
