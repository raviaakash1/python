import requests
import re

# === CONFIG ===
GITHUB_TOKEN = "your_personal_access_token"
REPO_OWNER = "your_org_or_username"
REPO_NAME = "your_repo_name"
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

# === VALIDATION RULE ===
def is_valid_commit(message):
    # Example rule: commit must start with JIRA ticket
    return re.match(r"^JIRA-\d+: .+", message) is not None

# === FETCH OPEN PRs ===
def get_open_prs():
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/pulls?state=open"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

# === FETCH COMMITS FOR A PR ===
def get_commits_for_pr(pr_number):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/pulls/{pr_number}/commits"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

# === MAIN VALIDATION LOGIC ===
def validate_prs():
    prs = get_open_prs()
    for pr in prs:
        pr_number = pr["number"]
        pr_title = pr["title"]
        print(f"\n🔍 PR #{pr_number}: {pr_title}")

        commits = get_commits_for_pr(pr_number)
        for commit in commits:
            message = commit["commit"]["message"]
            sha = commit["sha"]
            if is_valid_commit(message):
                print(f"✅ {sha[:7]}: Valid commit message")
            else:
                print(f"❌ {sha[:7]}: Invalid commit message → '{message}'")

if __name__ == "__main__":
    validate_prs()