# 전달받은 문자열에서 임의의 문자 하나를 화면에 출력하는 코드를 구현하시오.
# 이 문제는 random 모듈내 choice() 함수의 사용법을 아는지를 묻는 문제이다.
# 아래 코드에서 틀린 부분을 찾아서 설명해보시오.

a = random.choice( 'koreaKOREA' )
print( a )

b = random.choice( 'korea KOREA' )
print( b )

c = random.choice( [ 'k', 'o', 'r', 'e', 'a', '', 'K', 'O', 'R', 'E', 'A' ] )
print( c )

d = random.choice( [] )
print( d )
