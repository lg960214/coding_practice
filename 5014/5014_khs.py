f, s, g, u, d = tuple(map(int, input().split()))
answer = 0  
if s < g:
    if u != 0:
        first_up = (g - s) // u
    else:
        first_up = 0
    if s == g :
        print(0)
    elif u == 0:
        print('use the stairs') 
    elif s + first_up * u == g:
        print(first_up)    
    else:
        if u % 2 == 0 and d % 2 == 0 and (s % 2 != g % 2):
            print('use the stairs')
        else:    
            answer += first_up
            now = s + first_up * u
            now_list = [i*u+s for i in range(1, first_up+1)]

            no_answer = 0
            while True:
                if now < g :
                    if now + u <= f:
                        now += u
                    else:
                        now -= d
                else:
                    if now - d <= 0:
                        now += u
                    else:
                        now -= d
                if now <= 0 or now>f:
                    no_answer = 1
                    break 
                answer += 1
                if now == g:
                    print(answer)
                    break
                if now in now_list:
                    no_answer = 1
                    break
            if no_answer == 1:        
                print('use the stairs')     
                
else:
    if d != 0:
        first_up = (s - g) // d
    else:
        first_up = 0
    if s == g :
        print(0)
    elif d == 0:
        print('use the stairs') 
    elif s - first_up * d == g:
        print(first_up)    
    else:
        if u % 2 == 0 and d % 2 == 0 and (s % 2 != g % 2):
            print('use the stairs')
        else:    
            answer += first_up
            now = s - first_up * d
            now_list = [s - i*d for i in range(1, first_up+1)]

            no_answer = 0
            while True:
                if now < g :
                    if now + u <= f:
                        now += u
                    else:
                        now -= d
                else:
                    if now - d <= 0:
                        now += u
                    else:
                        now -= d
                if now <= 0 or now >f:
                    no_answer = 1
                    break 
                answer += 1
                if now == g:
                    print(answer)
                    break
                if now in now_list:
                    no_answer = 1
                    break 
            if no_answer == 1:        
                print('use the stairs')     

