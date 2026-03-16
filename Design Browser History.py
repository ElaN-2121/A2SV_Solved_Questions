class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]   # store for all visited pages
        self.curr = 0 # shows the current page

    def visit(self, url: str) -> None:
        self.history = self.history[:self.curr + 1]
        self.history.append(url)
        self.curr += 1
        
    def back(self, steps: int) -> str:
        # move back but not beyond 0
        self.curr = max(0, self.curr - steps)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        # move forward but not beyond last page
        self.curr = min(len(self.history) - 1, self.curr + steps)
        return self.history[self.curr]

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
