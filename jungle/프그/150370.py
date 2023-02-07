# today = "2022.05.19"
# terms = ["A 6", "B 12", "C 3"]
# privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]


def main(today, terms, privacies):
    answer = []
    ty, tm, td = today.split('.')
    ty, tm, td = int(ty), int(tm), int(td)
    for i in range(len(privacies)):
        year, t = privacies[i].split(' ')
        y, m, d = year.split('.')
        y, m, d = int(y), int(m), int(d)
        tempY = ty - y
        tempm = tm - m
        tempd = td - d
        total = 0
        total = tempY * 12 * 28 + tempm*28 + tempd
        for term in terms:
            termT, termM = term.split()
            if termT == t:
                tagetT = termM

        if int(tagetT)*28 <= total:
            answer.append(i+1)
    return answer


if __name__ == '__main__':
    today = "2022.05.19"
    terms = ["A 6", "B 12", "C 3"]
    privacies = ["2021.05.02 A", "2021.07.01 B",
                 "2022.02.19 C", "2022.02.20 C"]
    main(today, terms, privacies)
