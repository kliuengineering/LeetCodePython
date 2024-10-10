class Solution:
    def numDecodings(self, s: str) -> int:
        KB = { len(s) : 1 }                     # KB = { 5:1 }     
        
        def dfs(i):
            if i in KB:
                return KB[i]
            if s[i] == "0":
                return 0

            finding = dfs(i+1)
            # print(finding)

            if i+1 < len(s) and ( s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456") ):
                finding += dfs(i+2)
                # print(finding)
            
            KB[i] = finding
            # print(finding)
            return finding
        
        return dfs(0)


"""
string == 13542
building stack:                 popping stack                 

dfs(5) -> 5 in KB -> return 1    
dfs(4) -> finding = dfs(5)      finding = 1, KB = {5:1, 4:1}, return 1
dfs(3) -> finding = dfs(4)      finding = 1, 
dfs(2) -> finding = dfs(3)
dfs(1) -> finding = dfs(2)
dfs(0) -> finding = dfs(1)

"""

def fibonacci(i):
    if i < 1:
        return 0
    if i == 1:
        return 1
    return fibonacci(i-1) + fibonacci(i-2)
    

# 0, 1, 2, 3, 5, 8, 13, 21, 34

def main():
    solution = Solution()
    string = "13542"
    # print(solution.numDecodings(string))
    print(fibonacci(9))



if __name__ == "__main__":
    main()