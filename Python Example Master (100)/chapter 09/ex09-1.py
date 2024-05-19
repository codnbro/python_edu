# 여러 값이 들어있는 리스트에서 최곳값을 출력하는 함수를 직접 구현하시오.
# 이때, max() 함수를 사용해서는 안된다.

# [2] : 리스트
english_score = [ 33, 44, 55, 66, 77, 88, 99, 11, 22, 60 ]

# [3] : 함수 호출 및 결과 출력하기
result = max_in_list( english_score )
print( '[3-1] 직접 구현한 max() : ', result )
print( '[3-2] 내장 max() : ', max(english_score) )


[3-1] 직접 구현한 max() :  99
[3-2] 내장 max() :  99
