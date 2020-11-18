def solution(prices):
    answer = [0 for _ in range(len(prices))]
    for i in range(1, len(prices)):
        price = prices[i-1]
        count = 0
        for j in range(i, len(prices)):
            next_price = prices[j]
            count += 1
            if price > next_price:
                break

        answer[i-1] = count
    return answer
