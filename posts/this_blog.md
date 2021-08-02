# A quick guide to making this blog


## MyST-NB
This is what allows Jupyter Notebooks to be converted in blog posts. The parser is built ontop of [MyST-parser](https://myst-parser.readthedocs.io/en/latest/) which is a markdown for the Markedly Structured Text documents (a powerful and Sphinx compatible flavor of Markdown).


:: {Hint}
In the conf.py file you only need to include `myst-nb` as this automatically actives the `myst-parser`.
:::

MyST-NB conveniently let's you [hide code cells](https://myst-nb.readthedocs.io/en/latest/use/hiding.html). If you would like to add panels in a grid-layout or drop downs then check out [sphinx-panels](https://sphinx-panels.readthedocs.io/en/stable/) extension.

Note that `nbsphinx´ is older alternative package for parsing `.ipynb` files. The reason for mentioning this is that this package should not be added as an extension together with `myst-nb` as they would be conflicting.

## Jupyter Notebooks

[Link](https://jupyterbook.org/file-types/myst-notebooks.html)

