# 난이도 EASY였지만...나에겐...Extreme Hard....
# 아쉽게도 유튜브 강의 영상에 있는 코드를 이해해보았다.

# 배운점 : python Built-in fuction인 zip에 대해서 알게됐다.
# 느낀점 : while문, lambda 익숙해져야 할 것 같다. 

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 0:
            return ("")
        if len(strs) == 1:
            return (strs[0])

        fix = strs[0]
        fix_len = len(fix)

        for i in strs[1:]:
            while fix != i[0:fix_len]:
                fix = fix[:fix_len-1]
                fix_len -= 1

                if fix_len == 0:
                    return ""
        return fix
