#py.py

import requests
import os

def get_repo_owner_type():
    GITHUB_REPOSITORY = os.getenv('GITHUB_REPOSITORY')
    url = f"https://api.github.com/repos/{GITHUB_REPOSITORY}"
    headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {os.getenv('GH_TOKEN')}",
            "X-GitHub-Api-Version": "2022-11-28"
        }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        repo_info = response.json()
        owner_type = repo_info['owner']['type']
        return owner_type
    else:
        print(f"Error: {response.status_code} - {response.json()}")
        return None

# Example usage

owner_type = get_repo_owner_type()
if owner_type:
    print(f"The repository '{owner}/{repo}' is owned by a {owner_type}.")
