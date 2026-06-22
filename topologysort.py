
def topological_sort(pkgs: dict[str, list[str]]) -> list[str]:
    result: list[str] = []
    visited: set[str] = set()
    visiting = set()
    filtred = {
        pkg: [dep for dep in deps if dep in pkgs]
        for pkg, deps in pkgs.items()

    }

    def dfs(pkg: str):
        if pkg in visited:
            return True

        if pkg in visiting:
            return False

        visiting.add(pkg)

        for dep in sorted(filtred.get(pkg, [])):
            if not dfs(dep):
                return False

        visiting.remove(pkg)
        visited.add(pkg)
        result.append(pkg)
        return True

    for pkg in sorted(filtred.keys(), key=lambda k: (len(filtred[k]), k)):
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
