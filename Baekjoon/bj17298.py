# -*- coding: cp949 -*- 
# ���� 17298�� ��ū�� ���� Ǯ��
# Ǯ�� ��� - ���ÿ� ���� �ƴ� �ε����� �־��ִ� �������� ����Ͽ� �ذ�
import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
result = [-1] * n
indexStack = []

for i in range(n):
    while indexStack and num[indexStack[-1]] < num[i]:
        result[indexStack.pop()] = num[i]
    indexStack.append(i)

print(*result)