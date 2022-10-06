# Exercise 10 - Understanding Commits

1. Look at your commit log

        git log --oneline

2. Choose a commit hash

3. See what type of object that hash names

        git cat-file -t <hash>
        $ git cat-file -t 4531699
commit


4. Examine the contents of that commit closely

        git cat-file -p <hash>


5. Find the parent's hash in the commit log

6. Look at the contents of the tree

        git cat-file -p <hash>

7. Examine the contents of one of the blobs

8. What type of object does the parent hash represent?

        git cat-file -t <hash>
        parent 216f1e70b3bc60a4a13a37fdc61cb71171cfa861

9. Examine the contents of the parent and its tree
tree 875cfbfb158c4e0afc5c6bc5443a0ff90e6b4cbc
10. Do the trees you looked at have any matching hashes listed?
does not seem to have any matches
