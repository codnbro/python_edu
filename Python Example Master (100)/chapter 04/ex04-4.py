# 아래의 if 조건문에서 else 문의 위치에 따라 에러가 나는 것을 말해보시오.

# [1] : 카페 메뉴 선택기
btn = 3
if btn == 1:
        print( '아메리카노' )
else:
        print( '메뉴는 1, 2, 3번중 하나를 골라주세요!' )
elif btn == 2:
        print( '카페라떼' )
elif btn == 3:
        print( '아이스 카페라떼' )

# [2] : 카페 메뉴 선택기
btn = 3
if btn == 1:
        print( '아메리카노' )
elif btn == 2:
        print( '카페라떼' )
elif btn == 3:
        print( '아이스 카페라떼' )
