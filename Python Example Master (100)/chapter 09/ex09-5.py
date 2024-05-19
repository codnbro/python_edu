# 정렬 알고리즘중 삽입 정렬 알고리즘을 코드로 구현하시오.
# 이때, 첫 번째 반복문은 for문으로 구현하고, 두 번째 반복문은 while문으로 구현하시오.

# [ ! ] : 삽입 정렬
#  '삽입'이라는 단어에서 알 수 있듯이 정렬 대상이 자기 위치를 찾아서 들어간다(삽입)라는 의미이다.
# 정렬 대상의 1번째 인덱스(두 번째) 값과 1-1번째(즉, 0번째) 시작으로 순회하면서 비교 및 자기 위치에 가서 삽입.
# 구구단과 같이 중첩된 이중 반복문안에서 삽입 정렬이 이뤄진다. --> 따라서 반복은 n-1 만큼 --> for i in range( 1, len(lst) ):
# 첫 번째 반복문 --> 왼쪽에서 오른쪽으로 진행하면서 맨 끝까지 순회한다. --> 마치 구구단의 2단 부터 9단 까지 순회하듯이..
# 두 번째 반복문 --> 오른쪽에서 왼쪽 끝까지 2개씩 값을 비교하면서 순회한다. --> 마치 2단의 1부터 9까지 순회하듯이..
