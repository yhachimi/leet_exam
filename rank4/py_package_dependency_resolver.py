from collections import deque

def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    pq = deque()
    keyys = set()
    val = set()
    res = []
    degree = {}
    
    for k, v in packages.items():
        for el in v:
            if k == el:
                return []
            if k in val and el in keyys:
                return []
            keyys.add(k)
            val.add(el)
    degree = {k: len(v) for k, v in packages.items()}
    for k in degree.keys():
        if degree[k] == 0:
            pq.appendleft(k)
    pq = sorted(pq)
    pq = deque(pq)
    if not list(pq):
        return []
    while pq:
        node = pq.popleft()
        res.append(node)
        for k, v in packages.items():
            if node in v:
                v.pop(v.index(node))
                if len(v) == 0:
                    pq.append(k)
                else:
                    for el in v:
                        if el not in packages.keys():
                            pq.append(k)

    return res

