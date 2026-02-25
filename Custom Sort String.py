class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_map = {ch: i for i, ch in enumerate(order)}
        return "".join(sorted(s, key=lambda ch: order_map.get(ch, len(order))))
