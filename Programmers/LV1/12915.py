# 문자열 내 마음대로 정렬하기
def solution(strings, n):
    # 람다식 활용 -> n의 인덱스 우선으로 정렬후 사전순 정렬
    strings.sort(key=lambda x: (x[n],x))
    return strings

solution(["sun", "bed", "car"], 1)