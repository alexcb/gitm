import os

def discover_git_repos(path):
    git_repos = []
    for root, dirs, files in os.walk(path):
        if '.git' in dirs:
            del dirs[:]
            git_repos.append(root)
        else:
            # dont recurse into hidden directories
            dirs[:] = [x for x in dirs if not x.startswith('.')]
    return git_repos
