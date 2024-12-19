import collections
from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = collections.defaultdict(set)
        email_to_name = {}

        # Build the graph and map emails to their names
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                email_to_name[email] = name  # Map each email to its name
                graph[account[1]].add(email)
                graph[email].add(account[1])

        res = []
        visited = set()

        # Traverse the graph to find connected components
        for email in graph:
            if email not in visited:
                stack = [email]
                visited.add(email)
                local_res = []

                while stack:
                    node = stack.pop()
                    local_res.append(node)
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            stack.append(neighbor)

                # Append the result for this connected component
                res.append([email_to_name[email]] + sorted(local_res))

        return res