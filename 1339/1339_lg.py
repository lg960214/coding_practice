import sys
from collections import defaultdict, deque

sys.stdin = open('testcase.txt','r')
input = sys.stdin.readline


class Sol:
    def __init__(self):
        N = int(input())
        max_ = 0
        dict_ = defaultdict(int)
        word_list = []
        num_queue = deque([i for i in range(9, -1, -1)])

        for _ in range(N):
            word = str(input().rstrip())
            word_list.append(word)

            max_ = max(len(word), max_)

            for i in range(0, len(word)):
                dict_[word[i]] += 10**(len(word)-i)

        set_ = set(dict_)

        list_ = []

        for factor in set_:
            list_.append([dict_[factor], factor])

        list_.sort(reverse=True)
        alphabet = dict()

        for i in range(len(set_)):
            alphabet[list_[i][1]] = num_queue.popleft()

        print(alphabet)

        sum_ = 0

        for i in range(N):
            word = word_list[i]
            num = ''
            for apb in word:
                num += str(alphabet[apb])

            sum_ += int(num)

        print(sum_) 

if __name__ == '__main__':
    user = Sol()