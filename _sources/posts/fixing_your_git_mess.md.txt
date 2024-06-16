# Fixing your git mess
```{post} 2021-08-27
:author: Adam R. Jensen
:tags: open science, gsoc
```

On a day-to-day basis I use GitHub Desktop due to its nice graphical interface and that my git skills are close to zero. Every now and then, I screw things sufficiently up that I don't know how to fix it and sometimes I don't even know how I ended up there. At this point, I really just want to go back in time to when my code was working - which is the topic of this blog post.

Unfortunately, GitHub Desktop cannot help you here and you need to open up a Git Bash terminal and run a few commands. Without further ado, this [stackoverflow answer](https://stackoverflow.com/a/21718540/8558146) describes very well my preferred way out of trouble. The method lets you revert your repository back to the state of a previous commit (e.g., 0766c053) in a safe way:

```
git revert --no-commit 0766c053..HEAD
git commit
```

Before using `git commit`, you can inspect that your code is indeed in the state that you expect. From this point on, you can even use GitHub Desktop to commit the reversion changes. Note that by using the `--no-commit` flag, all changes can be committed in one commit, keeping your commit history clean.

There are many alternative methods to achieving the same outcome, e.g., undoing previous commits, however, many of the alternatives erases the history and makes irreversible changes, why such methods are generally not recommended.
