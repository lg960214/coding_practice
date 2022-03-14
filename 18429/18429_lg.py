import sys
import itertools 

class Sol:
    weight = 500
    answer = 0

    def __init__(self):
        self.N, self.K = map(int, input().split())
        self.weight_kit = list(map(int, input().split()))
        
        self.comb = itertools.permutations(self.weight_kit, self.N)

        for case in self.comb:
            self.cal(case)
        
        print(self.answer)
    
    def cal(self, case_):
        list_ = case_
        weight_decay = 500
        assignment = True

        for factor in list_:
            weight_decay += factor
            weight_decay -= self.K

            if self.weight <= weight_decay:
                pass
            else:
                assignment = False
                break
        
        if assignment == True:
            self.answer += 1



if __name__ == '__main__':
    user = Sol()