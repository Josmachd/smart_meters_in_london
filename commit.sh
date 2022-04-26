#!/bin/bash
rm -rf __pycache__
rm -rf .idea
rm -rf *~

#commit_message="USER INPUT"
echo -n "Commit message: "
read commit_message
git add notebook.ipynb notebook_2.ipynb README.md commit.sh 
git commit -m"${commit_message}"
git push
echo $commit_message
