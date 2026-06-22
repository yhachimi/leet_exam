
def topological_sort(pkgs: dict[str, list[str]]) -> list[str]:
    result: list[str] = []
    visited: set[str] = set()
    visiting = set()

    def dfs(pkg: str):
        if pkg in visited:
            return True

        if pkg in visiting:
            return False

        if pkg not in pkgs.keys():
            return True

        visiting.add(pkg)

        for dep in sorted(pkgs.get(pkg, [])):
            if not dfs(dep):
                return False

        visited.add(pkg)
        result.append(pkg)
        visiting.remove(pkg)
        return True
    for pkg in pkgs.keys():
        pkgs[pkg] = [dep for dep in pkgs[pkg] if dep in pkgs]

    for pkg in sorted(pkgs.keys(), key=lambda k: (len(pkgs[k]), k)):
        if not dfs(pkg):
            return []

    return result


depend_pkg = {
    "a": ["c", "d", "k", "b"],
    "e": ["c", "a"],
    "c": ["d"],
    "g": ["n", "k"],
}


print(topological_sort(depend_pkg))
