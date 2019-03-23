class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        list_temp_char = ""
        list_val = 0
        for ind in range(len(s)):
            list_sub = s[ind:len(s)]
            if list_val > len(list_sub):
                continue
            for list_char in list_sub:  
                if list_char not in list_temp_char:
                    # print ("if:",list_char)
                    list_temp_char+=list_char
                    # print ("listchar_append:",list_temp_char)
                else:
                    # print ("else:",list_char)
                    # print ("listcahrtemp",list_temp_char)
                    break
            if len(list_temp_char)>list_val:
                list_val = len(list_temp_char)
            # list_val.append(len(list_temp_char))
                
            list_temp_char = ""
        # print (list_val)
        if list_val>0:
            return list_val
        else:
            return 0

def stringToString(input):
    import json

    return json.loads(input)

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            s = stringToString(line);
            
            ret = Solution().lengthOfLongestSubstring(s)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
