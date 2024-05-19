# 아래의 코드를 수정하여 최고, 최저 점수가 동시에 출력되도록 구현하시오.
# 한 반의 학생들 10명에 대한 영어 점수표가 리스트로 있다.
# 함수를 만들어 영어 점수표를 함수로 전달하면 최고 점수와 최저 점수가 동시에 나오도록 구현해본 것이다.

# [1] : 함수 작성
def max_min_in_list(lst):
        return min(lst)
        return max(lst)

# [2]  : 영어 점수표 --> list
english_score = [ 35, 90, 58, 30, 98, 56, 89, 78, 91, 67 ]

# [3] : 함수 호출 및 결과 출력하기
result = max_min_in_list(english_score)
print( result )


