import sys
input = sys.stdin.readline

n = int(input())

num_list = []

for _ in range(n):
    x,y = map(int,input().split())
    num_list.append((x,y))

num_list.sort()

for i in num_list:
    print(i[0],i[1])