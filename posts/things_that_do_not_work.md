# Things that don't work with this blog setup
```{post} 1994-06-28
:author: Adam R. Jensen
```

This blog is made using ablog and [the Sphinx PyData Theme](https://pydata-sphinx-theme.readthedocs.io/).

However, there are a few things that are not possible, which I expected should be:

E.g., quote blocks do not render in the Sphinx PyData Theme. A quote section in `myst` can be done by starting the line with a >, however, it simply renders as:

> This is supposed to be a quote

The lack of styling for block quotes is describing in this [issue](https://github.com/pydata/pydata-sphinx-theme/issues/252).

Another thing that do not work is strikethrough using, which normally is achieved using the tilde (~) symbol. This is due to strike through not being supported by MyST, though there currently is a [feature request open](https://github.com/executablebooks/jupyter-book/issues/726).
