# repo-helper.py
from github import Github
import argparse


token = 'inserttokenhere'      # Create a PAT here: https://github.com/settings/tokens


# Creates argument parser
parser = argparse.ArgumentParser(
    description='Required: "-t"\nOptional: "-d"\nAdditional Flags: "--private", "--init"'
)

# Adding arguments to parser
parser.add_argument('-t', help='Title of the repo.', required=True)
parser.add_argument('-d', help='Description of the repo(not required).', default='', required=False)
parser.add_argument('--private', action='store_true', default=False, help='This flag sets repo to private.')
parser.add_argument('--init', action='store_true', default=False, help='This flag initiates the repo on creation.')
args = parser.parse_args()


# Creating PyGithub object
g = Github(token)
user = g.get_user()

# Creating the new repo
try:
    repo = user.create_repo(args.t, description=args.d, private=args.private, auto_init=args.init)
    print(f'Done!\nGit url: {repo.git_url}')
except Exception as exc:
    print(f'Encountered an error while trying to create a new repo: {args.t}\nError: {exc}')
    quit(1)
