# art-of-questions
Repository containing required resources for our workshop titled: The Art of Questions, creating a QA system using semantic search and LLMs

There are two flavours of this workshop. Choose the Python approach, if you want more features and a vibrant ecosystem. Or choose the Java approach, if you are more comfortable with Java. Both languages work for this workshop.

Python is this repository, you can find the java edition here:
[TODO: LINK TO JAVA](https://github.com)

## Setup the repository
First setup your python environment, all the code is tested with Python 3.11.* but we expect the code to work with >3.8.1. We advise using python virtual environment or a tool like conda. If you are not familiar with virtual environments, this link should get you all up to speed.
[Creating and using virtual environments with Python](https://realpython.com/python-virtual-environments-a-primer/)

If you have done it before, but always forget the exact commands, you can find them below.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt

# When you are done
deactivate
```

And for windows the following commands should do the trick

```Powershell
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt

deactivcate
```
We are integrating with a number of other tools and services. Therefore we need some API keys. You need to create a file with the name _.env_. The repository contains a template for the file _template-env_. After creating the file, you do not need all the API keys yet, you can run the python notebook _environment_check.ipynb_ that verifies correct _.env_ file.

Working with Python notebooks has become a lot easier with the integration into PyCharm and VS Code. Both have out-of-the-box support for running notebooks. You need to install Jupyter into the environment. Usually your IDE will ask by itself if you want to install it.

[PyCharm documentation for running notebooks](https://www.jetbrains.com/help/pycharm/jupyter-notebook-support.html#editor)

[Visual Studio Code documentation for running notebooks](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)

Now run the environment_check notebook, and follow the steps in the notebook to setup your environment.

If you know the services you want to use, you can obtain those API keys. If you are not sure, you can register those keys later on.

## Overview of what you are going to do
![Overview of the Application for the workshop](docs/solution-overview.drawio.png)

Before the workshop we push 4 assignments. Each assignment contains a number of TODOs. Your task is to fix/implement the TODOs.

