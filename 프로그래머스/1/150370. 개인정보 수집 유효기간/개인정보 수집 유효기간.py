def solution(today, terms, privacies):

    termsDict = {}
    answer = []

    # 약관 별 기간 딕셔너리로 만듦
    for i in range(len(terms)):
        term, period = terms[i].split()
        termsDict[term] = period

    # privacies 를 날과 약관으로 나눔
    for i in range(len(privacies)):
        day, userTerm = privacies[i].split()
        year, month, date = day.split('.')
        # 날 -> 년, 월, 일로 분리
        todayYear, todayMonth, todayDate = today.split('.')

        # int 형으로 변환
        year = int(year)
        month = int(month)
        date = int(date)

        todayYear = int(todayYear)
        todayMonth = int(todayMonth)
        todayDate = int(todayDate)

        month += int(termsDict[userTerm])
        date -= 1

        if month > 12:
            year += month // 12
            month = month % 12
        if date == 0:
            date = 28
            month -= 1
        if month == 0:
            month = 12
            year -= 1
        print(year, month, date)

        # 비교
        if year < todayYear:
            answer.append(i+1)
        elif year == todayYear and month < todayMonth:
            answer.append(i+1)
        elif year == todayYear and month == todayMonth and date < todayDate:
            answer.append(i+1)
    return answer