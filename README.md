DOCUMENTATION
=============

GIT tutorial on github:
http://schacon.github.com/git/gittutorial.html

GIT "cheat sheet"
http://jonas.nitro.dk/git/quick-reference.html

GIT for those who are used to centralized SCMs:
http://media.pragprog.com/titles/tsgit/chap-005-extract.html

HOWTO
=====

To get a copy of the repo:
``` sh
git clone http://your-username@scm.trinitydesktop.org/scm/git/<repository name>
```

To exclude items:
	Create a file `.gitignore`

To add to the git repository (easiest and most efficient way):
``` sh
git add .
```
(this will add everything in the folder (excluding stuff from `.gitignore`). It is intentionally a period because `*` will make git stop on already committed files.)

To commit to the git repository (this does not send to the remote server!):
``` sh
git commit -a
```
(no need to do any git mv or git rm or any of that with the -a option.)

To pull recent commits from the remote git repository:
``` sh
git pull
```
(do this before pushing so that you don't collide with other's commits.)

To push to the remote git repository:
``` sh
git push origin master
```
(the 'origin master' part is optional after the first time.)

To branch (be careful! This is different from SVN.):
``` sh
git branch <name>
```
(don't know what branch you're on? run "git branch" to see and list.)

To switch branches:
``` sh
git checkout <branch name>
```

To tag a commit (like for releasing a tarball):
``` sh
git tag -a <version> -m <message>
```
(ps: this will make webgit generate a tarball with this tag.
easy releases anyone?)

To tag a commit WITH GPG verification (secure release anyone?):
``` sh
git tag -s <version> -m <message>
```



NOTE
====
GIT cannot store empty directories due to a intentional design limitation.

Therefore, this command should be run prior to any commits to ensure your empty directories stick around:

``` sh
find . -type d -empty -exec touch {}/.gitignore \;
````

This will add a `.gitignore` to every empty directory.

WORKFLOW
========


``` sh
git clone http://your-username@scm.trinitydesktop.org/scm/git/<repository>
```

<make your changes, test, etc>

``` sh
cd <repository checkout directory>
find . -type d -empty -exec touch {}/.gitignore \;
git add .
git commit -a
git pull
git push
```

