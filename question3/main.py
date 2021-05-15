#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n, m = list(map(int, input().strip().split()))
  data = [set([i]) for i in range(n)]

  for i in range(m):
    a, b = list(map(int, input().strip().split()))
    data[a].add(b)
    data[b].add(a)

  result = 0
  result_set = []
  for i in range(n):
    for j in range(i, n):
      for k in range(j, n):
        merged_set = data[i] | data[j] | data[k]
        count = len(list(merged_set))
        if result < count:
          result = count
          result_set = [i, j, k]

  result_set = map(str, result_set)
  print(" ".join(result_set))

main()
