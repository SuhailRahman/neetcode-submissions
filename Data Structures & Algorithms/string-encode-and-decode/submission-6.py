class Solution:

    def encode(self, strs: List[str]) -> str:
        res_str = ""
        for st in strs:
            res_str += str(len(st)) + "/" + st
        # print(res_str)
        return res_str

    def decode(self, s: str) -> List[str]:
        res_list = []
        i = 0
        str_len = ""
        while i < len(s):
            if s[i] != '/':
                str_len += s[i]
                i += 1
            else: 
                # print(str_len)
                j = int(str_len)
                i += 1
                res_list.append(s[i:i+j])
                i = i+j
                str_len = ""
            # print(str_len, res_list)
        return res_list

            
