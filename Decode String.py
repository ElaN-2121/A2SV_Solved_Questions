class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        current_str = ""
        current_num = 0

        for ch in s:
            if ch.isdigit():
                current_num = current_num * 10 + int(ch)
            elif ch == "[":
                stack.append((current_str, current_num))
                current_num = 0
                current_str = ""
            elif ch =="]":
                prev_str, _num = stack.pop()
                current_str = prev_str + current_str * _num
            else:
                current_str += ch
        return current_str
