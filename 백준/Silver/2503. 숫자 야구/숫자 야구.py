class Sol:
    number_list = []
    def __init__(self):
        for i in '123456789':
            for j in '123456789':
                for k in '123456789':
                    if ((i==j) or (j==k) or (k==i)): continue
                    self.number_list.append(i+j+k)

        self.N = int(input())

        for _ in range(self.N):
            target, s, b = map(str, input().split())
            temp_list = []

            for comp in self.number_list:
                s_cnt, b_cnt = 0, 0
                for i in range(3):
                    if (comp[i] == target[i]):
                        s_cnt += 1
                    elif (target[i] in comp):
                        b_cnt += 1
                if ((s_cnt == int(s)) and (b_cnt == int(b))):
                    temp_list.append(comp)

            self.number_list = temp_list

        print(len(self.number_list))


user = Sol()