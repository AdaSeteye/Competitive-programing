class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def helper(s, address, octets):
            if octets == 4:
                if s == "":
                    return ans.append(".".join(address))
                return
            
            for i in range(1, min(4, len(s) + 1)):
                if i > 1 and s[0] == '0':
                    break
                
                octet = int(s[:i])
                if 0 <= octet and octet <= 255:
                    address.append(str(octet))
                    helper(s[i:], address, octets + 1)
                    address.pop()
        helper(s, [], 0)
        return ans
