
# 개발언어는 cpp, java, python 중 하나입니다.
# 직군은 backend, frontend 중 하나입니다.
# 경력은 junior, senior 중 하나입니다.
# 소울푸드는 chicken, pizza 중 하나입니다.
# 점수는 코딩테스트 점수를 의미하며, 1 이상 100, 000 이하인 자연수입니다.

def find(scores, target):
    start = 0
    end = len(scores)
    # score, idx
    while start < end:
        mid = (start + end) // 2
        if target == scores[mid][0]:
            return mid
        elif target < scores[mid][0]:
            end = mid - 1
        else:
            start = mid + 1
    return start



def solution(info, query):
    answers = []
    langs = {"cpp": set(), "java": set(), "python": set(), "-": set()}
    jobs = {"backend": set(), "frontend": set(), "-": set()}
    works = {"junior": set(), "senior": set(), "-": set()}
    foods = {"chicken": set(), "pizza": set(), "-": set()}
    scores = []

    
    infos = []
    for idx, i in enumerate(info):
        tmp = i.split(" ")
        langs[tmp[0]].add(idx)
        langs["-"].add(idx)
        jobs[tmp[1]].add(idx)
        jobs["-"].add(idx)
        works[tmp[2]].add(idx)
        works["-"].add(idx)
        foods[tmp[3]].add(idx)
        foods["-"].add(idx)
        scores.append((int(tmp[4]), idx))
    
    scores.sort()


    for q in query:
        ans = 0
        q = q.replace("and ", "")
        q = q.split(" ")
        result = langs[q[0]] & jobs[q[1]] & works[q[2]] & foods[q[3]]
        
        score = int(q[4])
        start = find(scores, score)
        tmp = set(sc[1] for sc in scores[start:])
        
        ans = len(result & tmp)

        answers.append(ans)
    
    return answers


    

print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
         "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], 
         ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))

    

