from collections import defaultdict

def solution(id_list, report, k):
    answer = []

    id_reporting_user = dict()

    report_dict = defaultdict(set)

    for id in id_list:
        id_reporting_user[id] = set()

    for rep in report:
        i, r = rep.split(' ')
        report_dict[r].add(i)
        id_reporting_user[i].add(r)
    
    for key in report_dict.keys():
        if len(report_dict[key]) >= k:
            report_dict[key] = True
    
    for id in id_list:
        cnt = 0
        target = list(id_reporting_user[id])

        for tu in target:
            if report_dict[tu] == True:
                cnt += 1

        answer.append(cnt)
    
    
    
    
    return answer