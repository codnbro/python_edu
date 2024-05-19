# 파이썬 문법중 is 연산자를 이용한 출력 결과를 설명하시오.
# 아래 코드의 결과로 출력되는 값은 무엇인지 말해보시오. ( True, False 둘중 하나로 출력됨 )

# [1]
a = [ 1, 2, 3, 4, 5 ]
b = a
c = [ 1, 2, 3, 4, 5 ]

# [2] : 다음의 출력 결과를 말해보시오?
print( '[2-1] a is b = ', a is b )
print( '[2-2] a is c = ', a is c )
print( '[2-3] b is c = ', b is c )

'''
[2-1] a is b =  True
[2-2] a is c =  False
[2-3] b is c =  False
'''