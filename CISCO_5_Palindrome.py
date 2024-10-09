class Solution:

    """
    
    a b c b a
    | | | | |
        l    
        r

    a b c c b a

    """

    def longestPalindrome(self, s: str) -> str:
        KB = "" # initializes our knowledge base

        for i in range( len(s) ):
            # odd length
            l = i
            r = i
            while l > -1 and r < len(s) and s[l] == s[r]:
                if len(s[l:r+1]) > len(KB):
                    KB = s[l:r+1]

                l -= 1
                r += 1

            # even length 
            l = i
            r = i+1
            while l > -1 and r < len(s) and s[l] == s[r]:
                if len(s[l:r+1]) > len(KB):
                    KB = s[l:r+1]

                l -= 1
                r += 1
        
        if len(KB) < 1:
            KB = s[0]
        return KB





def main():
    solution = Solution()
    string_1 = "abcdcba"
    print(solution.longestPalindrome(string_1))
    print("the length of string_1 is -> ", len(string_1[0:8]))
    


if __name__ == "__main__":
    main()