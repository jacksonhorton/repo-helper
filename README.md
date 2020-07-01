# repo-helper.py
A super easy-to-use CLI to help you when creating new repositories!
# Requirements:
1. PyGithub
``pip3 install argparse``
2. argparse
``pip3 install PyGithub``
## Github PAT(Personal Access Token)
You will have to create a PAT at https://github.com/settings/tokens for this to work. Then set the token variable to your PAT:

``token = 'inserttokenhere'``

# Usage
*repo-helper* is used completely from the terminal/command line.
The most basic usage is:

``python3 repo-helper.py -t 'repo-name'``

To add a description:

``python3 repo-helper.py -t 'repo-name' -d 'sample description'``

You can also make it private by adding the flag ``--private`` or initiate the repo(which adds the readme.md automatically) with ``--init``.

If it is created successfully, it will return the git url in the terminal and say 'Done!'.

# Downloading
To use *repo-helper*, clone the repo or download the .zip and open it on your desktop(or wherever). **This is not a module**.
