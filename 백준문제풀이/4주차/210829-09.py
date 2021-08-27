"""
문제 번호 : 2941
단계 : 문자열
제목 : 크로아티아 알파벳
알고리즘 : 구현 / 문자열
"""

# 문자를 split, slicing

# 문자 입력
N = input()

# 변경된 문자들
letters = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in letters:
    N = N.replace(i,'*')
print(len(N))