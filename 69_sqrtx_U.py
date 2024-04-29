# this consists of both brute force and elegant solutions

class Solution:
    def __init__(self, x:int):
        self.x = x

    def BruteForce(self) -> int:
        y:int = 0
        while ( (y+1) ** 2 < self.x ):
            y = y+1
        return y

    def BinarySearch(self) -> int:
        endpoint_left = 0
        endpoint_right = self.x

        while ( endpoint_left <= endpoint_right ):
            midpoint = endpoint_left + ( (endpoint_right - endpoint_left) // 2 )

            if ( self.x < midpoint ** 2 ):
                endpoint_right = midpoint - 1

            elif ( self.x > midpoint ** 2 ):
                endpoint_left = midpoint + 1

            else:
                return midpoint

        return endpoint_right

def main():
    var:int = 85016
    print("BruteForce -> ", Solution(var).BruteForce())
    print("BinarySearch -> ", Solution(var).BinarySearch())

main()

