# 아래와 같이 쌍따옴표, 홑따옴표가 출력되도록 코드를 작성해보시오.
# 나는 엄마에게 말했다. "더 이상 '카레'는 먹기 싫어요!"라고..

sample1 = '나는 엄마에게 말했다."더 이상 카레 는 먹기 싫어요!"라고..'
sample2 = '나는 엄마에게 말했다."더 이상\'카레''\'는 먹기 싫어요!"라고..'
sample3 = "나는 엄마에게 말했다.\"더 이상'카레'는 먹기 싫어요!\"라고.."

print("[ 결과 출력 ]")
print(sample1)
print(sample2)
print(sample3)
print("나는 엄마에게 말했다."+"\"더 이상"+"'카레'"+"는 먹기 싫어요!"+"\""+"라고..")


'''
[ 결과 출력 ]
나는 엄마에게 말했다."더 이상 카레 는 먹기 싫어요!"라고..
나는 엄마에게 말했다."더 이상'카레'는 먹기 싫어요!"라고..
나는 엄마에게 말했다."더 이상'카레'는 먹기 싫어요!"라고..
나는 엄마에게 말했다."더 이상'카레'는 먹기 싫어요!"라고..
'''