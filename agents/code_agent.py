import os
import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description="Code Agent MVP")
    parser.add_argument("--mode", choices=["dry-run"], required=True)
    args = parser.parse_args()

    issue_title = os.getenv("ISSUE_TITLE")
    issue_body = os.getenv("ISSUE_BODY")
    issue_number = os.getenv("ISSUE_NUMBER")
    repo = os.getenv("REPO_FULL_NAME")

    print("=== Code Agent started ===")
    print(f"Repo: {repo}")
    print(f"Issue #{issue_number}")
    print(f"Title: {issue_title}")
    print("Body:")
    print(issue_body)
    print("=== Code Agent finished ===")

    sys.exit(0)


if __name__ == "__main__":
    main()
