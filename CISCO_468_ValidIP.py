import re

class Solution:
    def ValidateIPv4(self, queryIP: str) -> bool:
        pattern = r"""^
                ((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]?|0)\.){3}
                (25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]?|0)
                $"""
        if re.match( pattern, queryIP, flags=re.VERBOSE ):
            return True
        else:
            return False
        
    def ValidateIPv6(self, queryIP: str) -> bool:
        pattern = r"""
                    ^
                    ([0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4}
                    $
                    """
        if re.match(  pattern, queryIP, flags=re.VERBOSE ):
            return True
        else:
            return False

    def validIPAddress(self, queryIP: str) -> str:
        rc = "Neither"

        flag_IPv4 = self.ValidateIPv4(queryIP)
        flag_IPv6 = self.ValidateIPv6(queryIP)
        
        if flag_IPv4:
            rc = "IPv4"
        if flag_IPv6:
            rc = "IPv6"

        return rc



def main():
    stringA = "172.16.254.1"
    stringB = "2001:0db8:85a3:0:0:8A2E:0370:7334"
    stringC = "256.256.256.256"

    solution = Solution()
    print( solution.validIPAddress(stringA) )


if __name__ == "__main__":
    main()