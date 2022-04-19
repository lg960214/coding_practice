n,m = tuple(map(int, input().split()))
book_minus = []
book_plus = []
books = list(map(int, input().split()))
# 음수, 정수 별로 분리하고 정렬
for book in books:
    if book > 0 :
        book_plus.append(book)
    else:
        book_minus.append(book * -1)
book_minus = sorted(book_minus,reverse=True)
book_plus = sorted(book_plus,reverse=True)   
answer = 0
minus_ind = 0
plus_ind = 0
# 모든 책 위치 중 가장 먼 것만 돌아올 필요 없음
if len(book_minus) > 0 :
    first_minus_book = book_minus[0]
else:
    first_minus_book = 0
if len(book_plus) > 0 :
    first_plus_book = book_plus[0]
else:
    first_plus_book = 0
    
if first_minus_book > first_plus_book:
    answer += first_minus_book
    minus_ind += m
else:    
    answer += first_plus_book
    plus_ind += m
# 나머지 책들은 m 씩 건너뛰면서 2 곱한 값을 더해줌(왔다갔다 2번이니까)
while minus_ind < len(book_minus):
    answer += 2 * book_minus[minus_ind]
    minus_ind += m
while plus_ind < len(book_plus):
    answer += 2 * book_plus[plus_ind]
    plus_ind += m
print(answer)

