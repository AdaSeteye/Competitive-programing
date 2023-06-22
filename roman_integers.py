class Solution:
    def romanToInt(self, s: str) -> int:
        newStr = s.replace("IV", "+4").replace("IX", "+9").replace("XL", "+40").replace("XC", "+90").replace("CD", "+400").replace("CM", "+900").replace("I", "+1").replace("V", "+5").replace("X", "+10").replace("L", "+50").replace("C", "+100").replace("D", "+500").replace("M", "+1000")

        return eval(newStr)
