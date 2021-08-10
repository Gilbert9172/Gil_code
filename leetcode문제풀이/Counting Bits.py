# 338번 : Counting Bits

# 정수를 비트로 변환
# 비트 x 자릿수(2^n) = sum(정수)
# 정수 n를 넣으면 결과가 비트의 합으로 나와야함

# 1. 정수를 bin function을 사용하여 변환
# 2. 출력된 이진문자열 slicing
# 3. str으로 되어있는 list요소들을 list(map(int,))을 통해 정수형 list로 변환

class Solution:
    def countBits(self, n: int):
        lst =[]
        for i in range(n+1):
            bit = bin(i)[2:]
        
            bit_lst = list(bit)
            Int_bit = list(map(int,bit_lst))
        
            lst.append(sum(Int_bit))
        return lst

