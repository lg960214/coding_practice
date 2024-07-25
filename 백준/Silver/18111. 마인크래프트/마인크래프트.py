class Sol:
    answer = 1e9
    height = -1

    def __init__(self):
        self._initialize()
        self._input()

        for threshold in range(self.min_, self.max_+1):
            if not (self.ifPossible(threshold)): continue

            time = self.calculateTime(threshold)
            if (self.answer >= time):
                self.height = threshold
                self.answer = time

    def calculateTime(self, thr: int) -> int:
        t_in = 2
        t_out = 1

        cal_t = 0
        for i in range(self.N):
            for j in range(self.M):
                target = self.arr[i][j] - thr
                if (target < 0):
                    cal_t -= target*t_out
                elif (target > 0):
                    cal_t += target*t_in

        return cal_t


    def ifPossible(self, thr: int) -> bool:
        temp_sum = self.num_block - self.floor_size*thr + self.B
        
        if (0 <= temp_sum):
            return True

    def _initialize(self):
        self.arr = []
        self.min_ = 256
        self.max_ = 0

    def _input(self):
        self.N, self.M, self.B = map(int, input().split())

        for i in range(self.N):
            temp_lst = list(map(int, input().split()))
            self.min_ = min(self.min_, min(temp_lst))
            self.max_ = max(self.max_, max(temp_lst))
            self.arr.append(temp_lst)

        self.floor_size = self.N * self.M

        self.num_block = 0
        for i in range(self.N):
            self.num_block += sum(self.arr[i])

user = Sol()
print(user.answer, user.height)