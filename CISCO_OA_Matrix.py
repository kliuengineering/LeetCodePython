from typing import List


def SolutionLinear(num: int) -> List[str]:
    matrix = []
    n = num ** 2

    for i in range(n):
        if i%2 == 0:
            matrix.append("W")
        else:
            matrix.append("B")
    
    return matrix


def PrintLinear(num: int, matrix: List[str]) -> None:
    KB = []
    for i in range(0, num):
        temp = ""
        for j in range(0, num):
            temp += matrix[i*num + j] 
            temp += " "
        KB.append(temp)
    # print(KB)

    for itr in KB:
        print(itr)


def Solution2D(num: int) -> List[ List[str] ]:
    matrix = [ [i for i in range(num)] for j in range(num) ]
    print(matrix)


def main():
    num1 = 5
    num2 = 6
    
    matrix1 = SolutionLinear(num1)
    matrix2 = SolutionLinear(num2)

    PrintLinear(num1, matrix1)
    print("")
    PrintLinear(num2, matrix2)

    matrix3 = Solution2D(num1)


if __name__ == "__main__":
    main()