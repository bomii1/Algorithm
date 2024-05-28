def solution(friends, gifts):
    friendsDict = {}
    history = {}
    nextMonthGift = [0] * len(friends)

    # 돌면서 딕셔너리 초기화
    for i in range(len(friends)):
        friendsDict[friends[i]] = i
        history[friends[i]] = [0] * len(friends)

    # 선물 준 사람 받은 사람 기록하기
    for i in range(len(gifts)):
        sender, receiver = gifts[i].split()
        history[sender][friendsDict[receiver]] += 1

    for i in range(len(friends)):
        for j in range(i, len(friends)):
            if history[friends[i]][j] > history[friends[j]][i]: # i 가 더 큼
                nextMonthGift[i] += 1
            elif history[friends[i]][j] < history[friends[j]][i]: # j 가 더 큼
                nextMonthGift[j] += 1
            else: # 선물을 주고 받은 기록이 없거나 서로 같은 개수의 선물을 주고 받음
                sendPointX, receivePointX = sum(history[friends[i]]), 0
                sendPointY, receivePointY = sum(history[friends[j]]), 0

                for k in range(len(friends)):
                    receivePointX += history[friends[k]][i]
                    receivePointY += history[friends[k]][j]
                if (sendPointX - receivePointX) > (sendPointY - receivePointY): # 왼쪽 > 오른쪽
                    nextMonthGift[i] += 1
                elif (sendPointX - receivePointX) < (sendPointY - receivePointY): # 왼쪽 < 오른쪽
                    nextMonthGift[j] += 1
    answer = max(nextMonthGift)
    return answer

