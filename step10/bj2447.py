# -*- coding: cp949 -*- 
# ���� 2447�� ����� -10
# Ǯ�� ��� - ���� ����ִ� ������ ��Ģ�� ã�Ƽ� T(n) = 8T(n/3) + f(n) ��ȯ�Ŀ� �ش��ϴ� ���� ���� ������� �ذ�

n = int(input())
star = [['*' for i in range(n)] for j in range(n)]

def Star(i, j, size, list):
    if size == 3:
        list[i + 1][j + 1] = ' '
    else:
        Star(i, j, size // 3, list)
        Star(i, j + size // 3, size // 3, list)
        Star(i, j + 2 * (size // 3), size // 3, list)
        Star(i + size // 3, j, size // 3, list)
        Star(i + size // 3, j + 2 * (size // 3), size // 3, list)
        Star(i + 2 * (size // 3), j, size // 3, list)
        Star(i + 2 * (size // 3), j + size // 3, size // 3, list)
        Star(i + 2 * (size // 3), j + 2 * (size // 3), size // 3, list)
        for index in range(i + size // 3, i + 2 * (size // 3)):
            for indexj in range(j + size // 3, j + 2 * (size // 3)):
                list[index][indexj] = ' '

Star(0, 0, n, star)
for i in range(n):
    for j in range(n):
        print(star[i][j], end='')
    print()