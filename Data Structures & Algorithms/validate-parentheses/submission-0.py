class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # create a hashMap using closing brackets as key values
        closeToOpen = { ")" : "(", "}" : "{", "]" : "[" }

        for c in s:
            # if c is a key in our hashmap, it's a closing bracket
            if c in closeToOpen:
                # if the stack is empty, we can end, as this is a closing bracket and cannot be first
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False