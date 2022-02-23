# A quick guide to making this blog

This blog is made using [ablog](https://ablog.readthedocs.io) and [the Sphinx PyData Theme](https://pydata-sphinx-theme.readthedocs.io/).

## MyST-NB
This is what allows Jupyter Notebooks to be converted in blog posts. The parser is built ontop of [MyST-parser](https://myst-parser.readthedocs.io/en/latest/) which is a markdown for the Markedly Structured Text documents (a powerful and Sphinx compatible flavor of Markdown).


:: {Hint}
In the conf.py file you only need to include `myst-nb` as this automatically actives the `myst-parser`.
:::

MyST-NB conveniently let's you [hide code cells](https://myst-nb.readthedocs.io/en/latest/use/hiding.html). If you would like to add panels in a grid-layout or drop downs then check out [sphinx-panels](https://sphinx-panels.readthedocs.io/en/stable/) extension.

Note that `nbsphinx´ is older alternative package for parsing `.ipynb` files. The reason for mentioning this is that this package should not be added as an extension together with `myst-nb` as they would be conflicting.

## Jupyter Notebooks

[Link](https://jupyterbook.org/file-types/myst-notebooks.html)



## Things that don't work with this blog setup

There are a few things that are not possible, which I expected should be:

For example, the Sphinx PyData theme does not support:
* Block quotes, which usually can be starting a line with ">". The lack of styling for block quotes is describing in this [issue](https://github.com/pydata/pydata-sphinx-theme/issues/252).
* Vertical scrolling in Jupyter Notebook cells, e.g., a long table..

Another thing that do not work is strikethrough using, which normally is achieved using the tilde (~) symbol. This is due to strike through not being supported by MyST, though there currently is a [feature request open](https://github.com/executablebooks/jupyter-book/issues/726).

