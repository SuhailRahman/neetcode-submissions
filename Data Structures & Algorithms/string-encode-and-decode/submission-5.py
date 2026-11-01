class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""

        for string in strs:
            encodedString += str(len(string)) + '#' + string
        print(encodedString)
        return encodedString

    def decode(self, s: str) -> List[str]:
        decodedStringList = []
        totalLength = len(s)
        index = 0
        while(index < totalLength):
            j = index
            while(s[j] != '#'):
                j += 1
            offset = int(s[index: j])
            decodedStringList.append(s[j+1 : (j+1+offset)])
            index = j+1+offset
        return decodedStringList
