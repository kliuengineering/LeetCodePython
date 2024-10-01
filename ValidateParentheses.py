class Solution:
    def isValid(self, s: str) -> bool:
        rc = True

        # if there is a bracket not matched, then the string is invalid
        if len(s) % 2 != 0:
            rc = False
            return rc
        
        # maps out all the pairs
        table = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }
        
        # O(n) space
        stack = []

        # O(n) algo
        for itr in s:

            if itr in table:
                if len(stack)>0 and stack[-1] == table[itr]:
                    stack.pop()
                else:
                    rc = False
                    break

            else:
                stack.append(itr)

        if len( stack ) != 0:
            rc = False
        
        return rc


def main():
    solution = Solution()
    s = "{[]}"
    s2 = "{}[]()"
    s3 = "{[}]{}"
    s4 = "]]]]"
    print( solution.isValid(s) )
    print( solution.isValid(s2) )
    print( solution.isValid(s3) )
    print(  solution.isValid(s4) )


if __name__ == "__main__":
    main()