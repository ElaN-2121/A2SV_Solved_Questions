from typing import List

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        in_block = False
        current_line = []

        for line in source:
            i = 0
            if not in_block:
                current_line = []

            while i < len(line):
                # Start of block comment
                if not in_block and i + 1 < len(line) and line[i:i+2] == "/*":
                    in_block = True
                    i += 2

                # End of block comment
                elif in_block and i + 1 < len(line) and line[i:i+2] == "*/":
                    in_block = False
                    i += 2

                # Start of line comment
                elif not in_block and i + 1 < len(line) and line[i:i+2] == "//":
                    break

                # Normal character
                elif not in_block:
                    current_line.append(line[i])
                    i += 1

                # Inside block comment
                else:
                    i += 1

            # Only add non-empty lines when not inside block comment
            if not in_block and current_line:
                result.append("".join(current_line))

        return result
