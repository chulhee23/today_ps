
def find(node, parents):
    if (node == parents[node]):
        return node
    else:
        parents[node] = find(parents[node], parents)
        return parents[node]


def solution(n, costs):
    # 부모의 정점
    parents = [i for i in range(n)]
    answer = 0
    # 비용 순으로 오름차순
    costs = sorted(costs, key=lambda cost: cost[2])

    for cost in costs:
        start = find(cost[0], parents)
        end = find(cost[1], parents)
        price = cost[2]
        # print(f"start: {start}, end: {end}, price: {price}")

        # 두 노드의 부모가 다름 => 연결 X
        if start != end:
            # start 의 부모 end로 설정 하여 연결
            parents[start] = end
            
            answer += price
    return answer

n = 4
costs = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]

print(solution(n, costs))
