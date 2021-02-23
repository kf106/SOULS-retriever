# Pyenv setup scripts
(Tested on Ubuntu 20.04.2)

You have a problem with deploying your Python program so other people can use it. "I know," you think, "I'll use a virtual environment." Now you have two problems.<sup>**†**</sup>

I've put this stuff here because I use it for pretty much every Python program I write. Or rather, I clone this repository and rename it for each new project. Perhaps you'll find it useful too.

## The problem
I love Python the programming language, but I hate the "scaffolding" around it. It is bizarre that you can learn to write simple programs in a few hours, but it takes weeks or even months of experience to deploy your scripts in a manner that allows others to use them. Programs fail to run because you've written yours in Python 3.x and the default interpreter is Python 2.x. You forget that you installed some packages, so others get error messages that they can't import function foo from module bar, or other error messages.

The community has kindly proposed solution after solution for this, each of which is more complicated than the next. Virtualenv, venv, pyvenv, pyenv, or even packing the whole thing in a Docker container. Each is going to involve an afternoon of reading, and a day of debugging before you understand what is going on. Except Docker, which will take you a week.
## Some bash scripts to the rescue
This repository contains the setup that I use these days. There's an `install.sh` script that installs any Linux libraries that are needed (it has to be run using `sudo`), which then calls a `pyenv.sh` that installs pyenv, sets up a local environment for the checked-out repository, and installs the required Python packages listed in `requirements.txt`.

The program is then run using `run.sh`. In this example it spins up a simple Flask webserver.

Let's go through that again.

The instructions you provide:
1. Clone the repo,
2. Run `sudo install.sh` once,
3. Use `run.sh` from then on to run the program.

What you do beforehand:
1. Edit `install.sh` to contain the Linux packages your program needs,
2. Edit  `pyenv.sh` to contain the Python packages your program needs that can't be installed from `requirements.txt`
3. Make sure `requirements.txt` contains the rest of the Pip packages (instructions in the comments of `pyenv.sh`)
4. Edit the last line of `run.sh` to execute the command you would use at the command line to run your program. 

This setup doesn't mess up people's `.bashrc` file, and ensures they are using exactly the same Python interpreter version and package versions you are.
 
## Footnotes
<sup>**†**</sup>I'm paraphrasing Jamie Zawinski there.
