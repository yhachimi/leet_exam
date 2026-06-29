
def package_dependency_resolver(pkgs: dict[str, list[str]]) -> list[str]:
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



