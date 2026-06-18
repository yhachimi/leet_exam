
def topological_sort(pkgs: dict[str, list[str]]) -> list[str]:
    result: list[str] = []
    visited: set[str] = set()

    def dfs(pkg: str):
        if pkg in visited:
            return

        visited.add(pkg)

        for dep in sorted(pkgs.get(pkg, [])):
            dfs(dep)

        result.append(pkg)

    for pkg in pkgs.keys():
        dfs(pkg)

    return result


depend_pkg: dict[str, list[str]] = {}
depend_pkg["a"] = ["c", "d", "k"]
depend_pkg["e"] = ["c", "a"]
depend_pkg["c"] = ["d"]
depend_pkg["g"] = ["n", "k"]


print(topological_sort(depend_pkg))
