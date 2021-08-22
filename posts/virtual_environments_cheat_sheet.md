# Virtual environments cheat sheet
```{post} 2021-07-19
:author: Adam R. Jensen
:tags: open science, gsoc
```

This tutorial will be on the topic of conda environments, though the general workflow is similar for other types of virtual environments.

    conda create -n env_name python=3.7

where "env_name" is the chosen name for the new environment and 3.7 is the chosen Python version.

Once, you have a virtual environment you first need to activate the specific environment (note it's possible to have many environments, so this is where you choose which one you want to use). This can be done using the following command:

    conda activate env_name

Once you get comfortable with virtual environments, you'll probably end up having a number of different ones for different projects. Here's how you can get a list of all of your virtual environments:

    conda env list

Once your list of environments has become to long, you'll probably want to remove the environments you no longer use. To remove a virtual environment, simply open an Anaconda promt and type:

    conda env remove -n env_name

Often times we create a new virtual environment to work on a specific package or repository. Now to work with that package, we need to install the packages on which it depends on. Often times a list of the necessary packages are specified in a text file called 'requirements.txt'. Coveniently enough we call install all these dependecies to our new virtual environments with the following command:

    conda install --file requirements.txt

When typing in this command, it's important to be in the directory where the file is located.

Alternatively you can also use pip to install packages in your conda environment:

    pip install -r requirements.txt

You can of course still install a single package like you normally would by:

    conda install package_name

