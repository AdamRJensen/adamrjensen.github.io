# Virtual environments cheat sheet
```{post} 2021-07-19
:author: Adam R. Jensen
:tags: open science, gsoc
```

This cheat sheet will cover the basics of conda environments, though the general workflow is similar for other types of virtual environments.

Creating a virtual conda environment is quite easy. Simply open up an anaconda prompt and run the following command:

    conda create -n env_name python=3.7

where "env_name" is the chosen name for the new environment and 3.7 is the desired Python version.

Once you have created a virtual environment, you need to activate the specific environment (note it's possible to have many environments, so this is where you choose which one you want to use). This can be done using the following command:

    conda activate env_name

When you realize how helpful virtual environments can be, you’ll probably end up having several different ones for different projects. Here's how you can get a list of all of your virtual environments:

    conda env list

Eventually, you'll probably end up with a long list of environments, many of which have become obsolete as projects have ended. At this point, you'll probably want to remove the environments you no longer use. To remove a virtual environment, simply open an Anaconda prompt and type:

    conda remove --name env_name --all

Often times we create a new virtual environment to work on a specific package or repository. Now to work with that package, we need to install the packages on which it depends on. Often times a list of the necessary packages are specified in a text file called 'requirements.txt'. Conveniently enough, we can install all these dependencies to our new virtual environments with the following command:

    conda install --file requirements.txt

It's important to be in the directory where the requirements.txt file is located when you run this command.

Alternatively, you can also use pip to install packages in your conda environment:

    pip install -r requirements.txt

You can, of course, still install a single package like you usually would by:

    conda install package_name

or

    pip install package_name

And last, you can also install an environment using a conda environment.yml file:

    conda env create -f environment.yml

A good intro guide to virtual environments can be found at [astropy](https://docs.astropy.org/en/latest/development/workflow/virtual_pythons.html).
