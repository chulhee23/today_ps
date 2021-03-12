def solution(tickets):
    t = dict()
    for ticket in tickets:
        if ticket[0] in t:
            t[ticket[0]].append(ticket[1])
        else:
            t[ticket[0]] = [ticket[1]]

    for k in t.keys():
        t[k].sort(reverse=True)

    st = ["ICN"]
    answer = []

    while st:
        top = st[-1]
        if top not in t or len(t[top]) == 0:
            answer.append(st.pop())

        else:
            st.append(t[top][-1])
            t[top].pop()

    answer.reverse()

    return answer



print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print("----------")


# 테스트 케이스 추가
print(solution([['ICN', 'B'], ['ICN', 'C'], ['C', 'D'], ['D', 'ICN']]))
print("----------")


print(solution([['ICN', 'B'], ['B', 'C'], ['C', 'ICN'], ['ICN', 'D'], ['ICN', 'E'], ['E', 'F']]))


