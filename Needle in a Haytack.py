import sys
from collections import Counter

input = sys.stdin.readline

def can_form_subsequence(freq_t, s):
    used = Counter()

    j = 0
    for i in range(len(s)):
        c = s[i]
        used[c] += 1
        if used[c] > freq_t[c]:
            return False
    return True


def solve():
    T = int(input())
    for _ in range(T):
        s = input().strip()
        t = input().strip()

        freq_t = Counter(t)
        freq_s = Counter(s)

        possible = True
        for c in freq_s:
            if freq_s[c] > freq_t[c]:
                possible = False
                break

        if not possible:
            print("Impossible")
            continue
        
        remaining = freq_t.copy()

        result = []
        s_ptr = 0
        n = len(t)

        # We build answer greedily
        # At each step pick smallest valid character
        for _ in range(n):
            for ch in map(chr, range(ord('a'), ord('z') + 1)):
                if remaining[ch] == 0:
                    continue

                # try placing ch
                remaining[ch] -= 1
                temp = Counter()

                # simulate whether s is still possible
                ok = True
                j = 0
                for i in range(len(s)):
                    temp[s[i]] += 1
                    if temp[s[i]] > remaining[s[i]] + (1 if s_ptr < len(s) and s[s_ptr] == s[i] else 0):
                        ok = False
                        break

                if ok:
                    result.append(ch)

                    # update subsequence pointer if needed
                    if s_ptr < len(s) and ch == s[s_ptr]:
                        s_ptr += 1

                    break

                remaining[ch] += 1

        print("".join(result))


if __name__ == "__main__":
    solve()
