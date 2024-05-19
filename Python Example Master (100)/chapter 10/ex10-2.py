# 아래 코드의 결과로 출력되는 값을 예상하여 말해보시오.

# [1] : 함수 작성
# ---------------------------------------
def reverse_txt( str_ ):
        count = 0
        txt = ''
        for letter in str_:
                txt = letter + txt
                count += 1
                if count > 2:
                        break                        
        
        return txt
# ---------------------------------------
# [2] : 함수 호출
print( '[ 출력 결과 ]' )
print( '-' * 140 )
result = reverse_txt( ‘korea’ )
print( result )
