# 다중 할당시 여러 개의 값을 여러 개의 변수에 각각 저장시키는 코드를 한줄로 구현하시오.
# 여러 개의 값 --> 100, 3.14, k, korea
# 여러 개의 변수 --> a, b, c, d


a, b, c, d = 100, 3.14, 'k', 'korea'
t= 100, 3,14, 'k', 'korea'

print("[ 결과 출력 ]")
print("a,b,c,d 변수의 값은: "+str(a)+" "+str(b)+" "+c+" "+d)
print(type(a), type(b), type(c), type(d))
print(t)
print(type(t))


'''
[ 결과 출력 ]
a,b,c,d 변수의 값은: 100 3.14 k korea
<class 'int'> <class 'float'> <class 'str'> <class 'str'>
(100, 3, 14, 'k', 'korea')
<class 'tuple'>
'''