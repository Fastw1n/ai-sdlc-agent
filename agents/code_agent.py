import os
from github import Github

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("GITHUB_REPOSITORY")
ISSUE_NUMBER = int(os.getenv("ISSUE_NUMBER"))

g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)

issue = repo.get_issue(number=ISSUE_NUMBER)

branch_name = f"agent/issue-{ISSUE_NUMBER}"
base = repo.get_branch("main")

repo.create_git_ref(
    ref=f"refs/heads/{branch_name}",
    sha=base.commit.sha
)

readme = repo.get_contents("README.md", ref=branch_name)
new_content = readme.decoded_content.decode() + f"\n\nHandled issue #{ISSUE_NUMBER}"

repo.update_file(
    path="README.md",
    message=f"Handle issue #{ISSUE_NUMBER}",
    content=new_content,
    sha=readme.sha,
    branch=branch_name
)

repo.create_pull(
    title=f"Auto PR for issue #{ISSUE_NUMBER}",
    body=issue.body or "",
    head=branch_name,
    base="main"
)

print("PR created")
