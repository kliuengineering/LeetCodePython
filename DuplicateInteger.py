from typing import List


class SolutionDictionary:
    def hasDuplicate(self, nums:List[int]) -> bool:

        MAX = len(nums)
        KB = {}
        rc = False

        for i in range(0, MAX):
            key = nums[i]
            if key in KB:
                rc = True
                break
            else:
                KB[key] = 1

        return rc


def main():     
    MyList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    MySolutionDict = SolutionDictionary()
    print(MySolutionDict.hasDuplicate(MyList))

if __name__ == "__main__":
    main()
