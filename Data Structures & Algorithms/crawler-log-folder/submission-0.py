class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        count=0
        for log in logs:
            if log=="../":
                if stack:
                    stack.pop()
            elif log=="./":
                continue
            else:
                stack.append(log)
        for i in range(len(stack)):
            stack.pop()
            count+=1
        return count
