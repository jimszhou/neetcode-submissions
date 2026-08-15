class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        def plus_one(value, index):
            res = list(value)
            if res[index] == '9':
                res[index] = '0'
            else:
                res[index] = str(int(res[index]) + 1)
            return ''.join(res)
        
        def minus_one(value, index):
            res = list(value)
            if res[index] == '0':
                res[index] = '9'
            else:
                res[index] = str(int(res[index]) - 1)
            return ''.join(res)
        
        q = []
        visited = set()
        dead = set(deadends)

        q.append('0000')
        visited.add('0000')

        steps = 0

        while q:
            # need to spread by layer
            size = len(q)

            for i in range(size):

                cur = q.pop(0)

                # check valid
                if cur in dead:
                    continue

                # check match
                if cur == target:
                    return steps
                
                # BFS:
                for j in range(4):
                    up = plus_one(cur, j)
                    down = minus_one(cur, j)
                    if up not in visited:
                        q.append(up)
                        visited.add(up)
                    if down not in visited:
                        q.append(down)
                        visited.add(down)
            

            # add steps
            steps += 1
        return -1

