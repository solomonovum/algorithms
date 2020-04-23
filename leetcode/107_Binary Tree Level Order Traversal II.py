class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        run_queue, ready_queue, ret, level_values = [root], [], [], []

        while run_queue and run_queue[0]:
            level_values.append(run_queue[0].val)

            if run_queue[0].left:
                ready_queue.append(run_queue[0].left)

            if run_queue[0].right:
                ready_queue.append(run_queue[0].right)

            run_queue = run_queue[1:]

            if len(run_queue) is 0:
               run_queue = ready_queue.copy()
               ret.append(level_values.copy())
               level_values.clear()
               ready_queue.clear()

        return ret[::-1]
