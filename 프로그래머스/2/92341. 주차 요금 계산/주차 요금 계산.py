import sys
import math

def solution(fees, records):
    answer = []

    # 차번호 오름차순으로 정렬
    records = sorted(records, key=lambda record: record[6:10])

    # 시간, 요금
    basicTime = fees[0]
    basicFee = fees[1]
    excessTime = fees[2]
    excessFee = fees[3]

    # in, out
    inRecords = {}
    outRecords = {}

    # 딕셔너리에 넣기
    for i in range(len(records)):
        time, num, inout = records[i].split()

        if inout == "IN":
            if inRecords.get(num) is None:
                inRecords[num] = []
            inRecords[num].append(time)
        else:
            if outRecords.get(num) is None:
                outRecords[num] = []
            outRecords[num].append(time)
    # 요금 계산
    for i, (num, inoutList) in enumerate(inRecords.items()):
        totalFees = 0
        totalTime = 0

        if outRecords.get(num) is None:
            inH, inM = inRecords[num][0].split(":")
            inH = int(inH)
            inM = int(inM)

            totalTime += (23-inH) * 60 + (59-inM)
        else:
            for j in range(len(outRecords[num])):
                inH, inM = inRecords[num][j].split(":")
                outH, outM = outRecords[num][j].split(":")
                inH = int(inH)
                inM = int(inM)
                outH = int(outH)
                outM = int(outM)

                totalTime += (outH-inH) * 60 + (outM-inM)

            if len(outRecords[num]) < len(inRecords[num]):
                inH, inM = inRecords[num][-1].split(":")
                inH = int(inH)
                inM = int(inM)
                totalTime += (23-inH) * 60 + (59-inM)

        if totalTime <= basicTime:
            totalFees = basicFee
        else:
            totalFees = basicFee + (math.ceil((totalTime-basicTime)/excessTime) * excessFee)
        answer.append(totalFees)
    return answer



