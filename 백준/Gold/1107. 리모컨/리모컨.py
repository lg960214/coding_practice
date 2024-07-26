class Sol:
    def __init__(self):
        self._input()
        self.makeVirtualNumber()

        print(self.ans)

    def _input(self) -> None:
        whole_num = set(range(10))

        self.target = int(input())
        self.ans = abs(self.target-100)

        tf = input()
        if (tf != '0'):
            partial_num = set(map(int, input().split()))
            self.number = list(whole_num - partial_num)
        else:
            self.number = list(whole_num)

    def makeVirtualNumber(self) -> None:
        canUseNum = self.number

        for target in range(0, 1000001):
            for el in str(target):
                if not (int(el) in canUseNum):
                    break
            else:
                self.countPush(target)

    def countPush(self, comp_num: int) -> None:
        target_num = self.target
        comp_num_length = len(str(comp_num))

        pushCnt = abs(target_num - comp_num) + comp_num_length
        self.ans = min(pushCnt, self.ans)

user = Sol()