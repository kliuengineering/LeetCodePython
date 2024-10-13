import re


class Solution:
    def countValidWords(self, sentence: str) -> int:
        """
        
        Given:
            sentence: str

        Find:
            # of valid words: int

        Rules:
            sentence:
                1) a-z
                2) 0-9
                3) -
                4) !
                5) .
                6) ,
                7) \space
                8) 

            word:
                1) a-z
                2) -        : must be surrounded by a-z
                3) !
                4) .
                5) .
                6) ,
        
        """
        
        array = sentence.split()
        for itr in array:
            itr = itr.strip()

        pattern = r"([a-z]+((-)?[a-z]+)?)?(\!|\.|,|\s)?"

        rc = 0
        for itr in array:
            match = re.fullmatch(pattern, itr, re.VERBOSE)
            if match:
                rc += 1

        return rc



def main():
    solution = Solution()
    solution.countValidWords("what is      this?")


if __name__ == "__main__":
    main()