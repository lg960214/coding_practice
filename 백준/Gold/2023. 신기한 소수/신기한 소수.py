# permutation 문제로 보임

# [0] 번째 array 값 + [K] 번째 array 값으로 구성한다



def discriminate(num):
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            return False
    return True


def rec(step):
    for i in range(len(arr[step])):
        for j in '123456789':
            tmp_num = arr[step][i] + j
            if discriminate(int(tmp_num)):
                arr[step+1].append(tmp_num)
    return


arr = [[] for _ in range(9)]
arr[1] = ['2', '3', '5', '7']

N = int(input())

for i in range(1, N+1):
    rec(i)

for i in arr[N]:
    print(i)