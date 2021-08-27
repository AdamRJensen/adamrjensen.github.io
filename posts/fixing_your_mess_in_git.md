# Fixing your mess in git
```{post} 2021-08-27
:author: Adam R. Jensen
:tags: open science, gsoc
```

On a day to day basis I use GitHub Desktop due to it's nice graphical interface and that my git skills are close to zero. Every now and then I screw things sufficiently up that I don't know how to fix it and sometimes I don't even know how I ended up there. At this point, I really just want to go back in time to when my code was working - and this exactly the topic of this blog post.

My favorite way out of trouble is described in this [stackoverflow answer](https://stackoverflow.com/a/21718540/8558146). The method lets you revert everything back to the state of a previous commit in a safe way:

```
git revert --no-commit 0766c053..HEAD
git commit
```

Before using `git commit`, you can inspect that your code is indeed in the state that you expect. From this point on, you can even use GitHub Desktop to commit the reversion changes. Note that by using the `--no-commit` flag, all changes can be committed in one commit, keeping your commit history clean.

There are a lot of alternative methods to achieving the same outcome, however, e.g., undoing previous commits, though this erases the history and makes irreversible changes, which such methods are generally not recommended.
