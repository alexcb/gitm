def get_repos(config, tag):
    return config['tags'][tag] if tag else config['repos']
