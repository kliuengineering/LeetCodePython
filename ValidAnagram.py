from typing import Set


class Solution:
    def isAnagram( self, s:str, t:str ) -> bool:
        flag = True
        KBS = {}
        KBT = {}

        for itrS in s:
            if itrS in KBS:
                KBS[itrS] += 1
            else:
                KBS[itrS] = 1
        
        for itrT in t:
            if itrT in KBT:
                KBT[itrT] += 1
            else:
                KBT[itrT] = 1

        if KBS != KBT:
            flag = False
        
        return flag


def main():
    s = "HelloWorld"
    t = "WorldHello"
    u = "Hi"

    mySolution = Solution()
    print( mySolution.isAnagram(s, t) )
    print( mySolution.isAnagram(s, u) )


if __name__ == "__main__":
    main()