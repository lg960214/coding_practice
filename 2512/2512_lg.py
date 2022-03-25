import sys

sys.stdin = open('testcase.txt', 'r')
input = sys.stdin.readline

class Sol:
    def __init__(self):
        self.N = int(input())
        self.request = list(map(int, input().split()))
        self.M = int(input())

        self.request.sort(reverse=True)
        self.request.append(0)
        
        self.discriminative()

    def discriminative(self):
        sum_ = sum(self.request)

        if self.M >= sum_:
            print(self.request[0])
        else:
            for i in range(0, self.N+1):
                temp = self.request[i:]
                sum_ = sum(temp)
                sum_ += temp[0]*i

                if sum_ > self.M:
                    continue
                else:
                    if i == 0:
                        print(self.request[0])
                    else:
                        cal = self.M-sum_
                        result = self.request[i] + (cal//(i))
                        print(result)
                        break




if __name__ == '__main__':
    user = Sol()

