# complete-python-bootcamp

![Office Image](/images/Office.png) 

The goal of this project is to practice in Python. This project is fully based on Udemy course - https://www.udemy.com/share/101W943@ou0TY4LT3hD7s0PhiQma2x3uMOIZLKQ0fQguLqATb2NVewIeiP8SXFUX1yk4sF5C/
It may also contain some additional lines of code just for practice purpose

## installation

### Install python

Ensure you have Python 3.11 or later installed on your system. If you do not have Python installed, or if your version is older than 3.11, follow the steps below to download and install the latest version:

1. Download Python:

Visit the official Python downloads page to download Python 3.11 or later for your operating system (Windows, macOS, Linux/UNIX).

2. Run the Installer:

Windows: Run the downloaded executable. Ensure to check the box that says "Add Python 3.11 to PATH" before clicking "Install Now".
macOS: Open the downloaded .pkg file and follow the installation instructions.
Linux/UNIX: You might be able to install Python using your distribution's package manager. For example, on Ubuntu, you could use sudo apt-get install python3.11. Otherwise, follow the instructions provided on the download page for compiling and installing from source.

### Verify Installation

After installation, verify that Python has been installed correctly and is added to your system's PATH by opening a terminal (Command Prompt or PowerShell on Windows, Terminal on macOS and Linux/UNIX) and running:

"python --version" or "python3 --version"

![Python version command Image](/images/Python_version_command.png) 

### Additional Notes
Windows Users: If Python was not added to your PATH during installation, you can do so manually via System Properties > Advanced > Environment Variables, or reinstall Python and ensure to check the "Add Python to PATH" option.

macOS and Linux/UNIX Users: If python points to an earlier version, try using python3 to run Python 3.11 or later. You may also want to check your shell's configuration files (e.g., .bashrc, .zshrc) for existing Python aliases or PATH modifications.

With Python installed and configured, you're ready to set up your project's environment and install its dependencies.

## Pipenv installation and configuration
Pipenv is a dependency manager for Python projects which we use to manage the project's dependencies and to create a virtual environment. Follow these steps to set up your environment with Pipenv.

### Prerequisites
Ensure you have Python and pip installed on your system. Pipenv requires Python 3.x.

### Install Pipenv
If you haven't installed Pipenv yet, install it globally using pip. This ensures that you can use Pipenv from any directory in your system.
"pip install pipenv"

### Installing Project Dependencies
Once Pipenv is installed, navigate to the project's root directory (where the Pipfile is located) and install the project dependencies as follows:
"pipenv install"

This command reads the Pipfile, installs the required dependencies, and creates a Pipfile.lock which is used to produce deterministic builds. The Pipfile.lock ensures that the same versions of the dependencies are installed on every machine the project runs on.

### Activating the Virtual Environment
To activate the project's virtual environment, use the pipenv shell command. This ensures that you are using the project-specific versions of Python and installed packages, isolated from your global Python environment.
"pipenv shell"

### Exiting the Virtual Environment
When you're done working on the project, you can exit the virtual environment by simply typing:
"exit" or by pressing Ctrl+D in most terminal emulators.

## Run python

### Run from CMD

1. Navigate to file location you want to run 
2. Run the command "python <file_name>.py"

![run_python_from_cmd Image](/images/run_python_from_cmd.png) 
