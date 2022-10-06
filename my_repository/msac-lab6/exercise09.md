# Exercise 9 - Viewing history

1. Make a commit with a multi line commit message
   (leaving an empty line after the first line)

2. View that commit in the log

        git log -1

3. View the full commit log

        git log

*If the log fills your whole terminal, press `q` to exit*

4. View a shortened version of the commit log

        git log --oneline

5. Pick a commit hash from the log

6. View the commit log from the chosen commit backward

        git log --oneline <commit_hash>

7. How much of the commit hash do you need to specify? Hint, run `git help log`
specify the hash you want and the hashes after that will follow
8. How can you show just the last three commit messages?
git log --reverse then which numbers you want to see the commit messaged of 

