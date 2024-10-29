# type: ignore

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = Deque([])

        for e in path.split("/"):
            if e == "":
                continue
        
            if e == "..":
                if stack:
                    stack.pop()
            elif e == ".":
                continue
            else:
                stack.append(e)

        return "/" + "/".join(stack)
