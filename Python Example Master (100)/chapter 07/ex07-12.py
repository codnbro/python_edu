# 함수 호출시 파라미터 갯수를 알 수 없는 상황에서는 함수를 어떻게 만들어야하는지 예제로 설명하시오.
# 이 문제는 가변길이 인수 목록을 어떻게 받는지를 아는지 묻는 문제이다.

def my_func( _________________ ):
        n = 0
        for i in _____________:
                n += i
        return n
 
# [2] : 함수 호출
a = my_func( 1, 1, 1, 1 )
print( '[2-1] 입력 파라미터 4개의 합 : ', a )
b = my_func( 1, 2, 3, 4, 5, 6, 7, 8, 9 )
print( '[2-2] 입력 파라미터 9개의 합 : ', b )
[ 출력 결과 ]
---------------------------------------------------------------------
[2-1] 입력 파라미터 4개의 합 :  4
[2-2] 입력 파라미터 9개의 합 :  45