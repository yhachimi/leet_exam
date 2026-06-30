
def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    indegree = {pkg: 0 for  pkg in packages}
    graph = {pkg: [] for pkg in packages}


    for pkg, deps in packages.items():
        for dep in deps: 
            if dep == pkg:
                return []
            if dep not in packages:
                continue 
            graph[dep].append(pkg)
            indegree[pkg] += 1 
    heap = sorted([pkg for pkg in  packages if indegree[pkg] == 0])
    order = []
    while heap:
        pkg = heap.pop(0)
        order.append(pkg)
        for nxt in sorted(graph[pkg]): 
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                heap.append(nxt)


        heap.sort()


    if len(order) != len(packages):
        return []

    return  order



print(package_dependency_resolver({
    "A": [],
    "B": ["A"],
    "C": ["A", "B"]}))

print(package_dependency_resolver({
    "X": ["Y"],
    "Y": ["X"]
}))

print(package_dependency_resolver({}))

print(package_dependency_resolver({
    "web": [],
    "api": [],
    "frontend": ["web"],
    "backend": ["api"]
})
)
