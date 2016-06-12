# Git-RDM

Git-RDM is a Research Data Management (RDM) plugin for the [Git](https://git-scm.com/) version control system.

Much like the standard Git commands, Git-RDM allows users to add/rm files in a 'publication staging area'. When ready, users publish these staged files to a repository hosting service; currently only [Figshare](https://figshare.com/) and [Zenodo](http://zenodo.org/) are supported.

# Dependencies

Git-RDM mostly relies on the standard Python modules and, of course, Git. However, two extra modules are needed:

* [GitPython](https://gitpython.readthedocs.io), to access the Git repository's information.
* [PyRDM](https://pyrdm.readthedocs.io), to handle the publishing of files.

Both of these dependencies can be installed via `pip` using

```
sudo pip install -r requirements.txt
```

# Installing

A system-wide installation can be achieved by running

```
sudo python setup.py install
```

Once Git-RDM is installed, Git will automatically detect the plugin. The 'rdm' subcommands (described in the usage section below) can then be used; run `git rdm -h` at the command line to see a list of these:

```
christian@elevate ~/git-rdm $ git rdm -h
usage: git-rdm [-h] [-d] {init,add,rm,ls,publish,show} ...

positional arguments:
  {init,add,rm,ls,publish,show}
                        The subcommand of 'git rdm'.
    init                Initialise the .rdm control directory and publication
                        database.
    add                 Add a file to the publishing staging area.
    rm                  Remove a file from the publishing staging area.
    ls                  List the published files, and files staged for
                        publishing.
    publish             Publish the files in the publishing staging area.
    show                Show details about a particular publication.

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Enable debugging.
```

## Usage

The Git-RDM plugin comes with several subcommands. The following subsections demonstrate, with examples, how to use each of them. 

### git rdm init



### git rdm add

### git rdm rm

### git rdm ls

### git rdm publish

### git rdm show


# Contact

Please send any questions or comments about Git-RDM via email to [Christian Jacobs](http://christianjacobs.uk) at <christian@christianjacobs.uk>. Any bugs should be reported via the project's [issue tracker](http://github.com/ctjacobs/git-rdm/issues).
