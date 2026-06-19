class BrowserHistory:

    def __init__(self, homepage: str):
        self.logs: list[str] = []
        self.current = 0
        self.logs.append(homepage)

    def visit(self, url: str) -> None:
        self.logs = self.logs[:self.current + 1]
        self.logs.append(url)
        self.current += 1

    def back(self, steps: int) -> str:
        self.current = self.current - steps
        if self.current < 0:
            self.current = 0
        return self.logs[self.current]

    def forward(self, steps: int) -> str:
        self.current = self.current + steps
        if self.current >= len(self.logs):
            self.current = len(self.logs) - 1
        return self.logs[self.current]


to_visit = [
    ["leetcode.com"],
    ["google.com"],
    ["facebook.com"],
    ["youtube.com"],
    [1],
    [1],
    [1],
    ["linkedin.com"],
    [2],
    [2],
    [7]]


instrcutions = [
    "BrowserHistory",
    "visit",
    "visit",
    "visit",
    "back",
    "back",
    "forward",
    "visit",
    "forward",
    "back",
    "back"]

obj = None
res = []

for ins, args in zip(instrcutions, to_visit):

    if ins == "BrowserHistory":
        obj = BrowserHistory(args[0])
        res.append(None)

    elif ins == "visit":
        obj.visit(args[0])
        res.append(None)

    elif ins == "back":
        res.append(obj.back(args[0]))

    elif ins == "forward":
        res.append(obj.forward(args[0]))

print(res)
