set_ = set()

for _ in range(10):
    temp = int(input())

    set_.add(temp % 42)

print(len(set_))
