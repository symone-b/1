# Exercise 8 - Viewing changes before committing

1. Ensure your working directory is clean

2. Add text to any one of your files

3. Delete different text from another of your files

4. Look at `git status`

5. View all the changes you've made

        git diff

6. Does the following command return anything?

        git diff --staged
        No, it returned nothing.


7. Add one of your changed files to the index

        git commit add <changed file>

8. What do these commands show?

        git diff
        $ git diff
diff --git a/vegitables.txt b/vegitables.txt
index 84ae2d2..6e691e2 100644
--- a/vegitables.txt
+++ b/vegitables.txt
@@ -3,5 +3,4 @@ lettuce
 orange
 apple
 cucumber
-potato
-spinach
\ No newline at end of file
+potato
\ No newline at end of file

        git diff --staged
        $ git diff --staged
diff --git a/fruits.txt b/fruits.txt
index a1e551a..0470a48 100644
--- a/fruits.txt
+++ b/fruits.txt
@@ -5,4 +5,5 @@ pear
 blueberry
 strawberry
 pineapple
-kiwi
\ No newline at end of file
+kiwi
+grape
\ No newline at end of file

9. Add the other changed file to the index

        git commit add <other changed file>

10. What do these commands show?

        git diff
        git diff --staged
        $ git diff --staged
diff --git a/fruits.txt b/fruits.txt
index a1e551a..0470a48 100644
--- a/fruits.txt
+++ b/fruits.txt
@@ -5,4 +5,5 @@ pear
 blueberry
 strawberry
 pineapple
-kiwi
\ No newline at end of file
+kiwi
+grape
\ No newline at end of file
diff --git a/vegitables.txt b/vegitables.txt
index 84ae2d2..6e691e2 100644
--- a/vegitables.txt
+++ b/vegitables.txt
@@ -3,5 +3,4 @@ lettuce
 orange
 apple
 cucumber
-potato
-spinach

11. Commit the changes

12. Check that your working directory is clean

13. Create a new file named `clothing.txt`

14. Does the new untracked file show up in git diff?

        git diff
nothing shows up in git diff
15. Add and commit the new file
