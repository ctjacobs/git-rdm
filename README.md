# Git-RDM

Git-RDM is a Research Data Management (RDM) plugin for the [Git](https://git-scm.com/) version control system.

Much like the standard Git commands, Git-RDM allows users to add/remove data files within a 'publication staging area'. When ready, users can readily publish these staged files to an online data repository service such as Figshare and Zenodo via the command line. Details of the files and their associated publication(s) are then recorded in a local database, including the specific Git revision (in the form of a SHA-1 hash) and the DOI, such that a full history of data publication is maintained.

## Dependencies

Git-RDM mostly relies on the standard Python modules and, of course, Git. However, two extra modules are needed:

* [GitPython](https://gitpython.readthedocs.io), to access the Git repository's information.
* [PyRDM](https://pyrdm.readthedocs.io), to handle the publishing of files.

Both of these dependencies can be installed via `pip` using

```
sudo pip install -r requirements.txt
```

## Installing

A system-wide installation can be achieved by running

```
sudo python setup.py install
```

Once Git-RDM is installed, Git should automatically detect the plugin and recognise the `rdm` command; for example, run `git rdm -h` to list the RDM-related subcommands described in the Usage section below.

## Usage

The Git-RDM plugin comes with several subcommands. The following subsections demonstrate, with examples, how to use each of them. 

### git rdm init

In order to start using Git-RDM, the command `git rdm init` must first be run within the Git repository containing the data files to be published. This creates a new directory called `.rdm` containing a database file `publications.db`. All data publication details are stored within this file. Note that this command is similar to `git init` which initialises a new Git repository and creates the `.git` control directory. As an example, consider the `test` directory below, containing files `test1.txt`, `test2.txt` and `test3.png`:

```

```

### git rdm add

Once the RDM database has been initialised, data files may be added to the 'publication staging area' using `git rdm add` as follows:

```
```

The file being added for publication must first have been committed within the Git repository, otherwise Git-RDM will refuse to add it.

### git rdm rm

Files can also be removed from the publication staging area using `git rdm rm`:

```
```

### git rdm ls

In order to keep track of which data files have been published, 

Users can choose to list each file, followed by any DOIs associated with it (by default),

```
```

or choose to list the DOIs first and the files associated with it afterwards,

```
```

### git rdm publish


Note that only [Figshare](https://figshare.com/) and [Zenodo](http://zenodo.org/) are currently supported, but support for new services can be readily added by extending the [PyRDM library](https://pyrdm.readthedocs.io).

### git rdm show

The full publication record maintained by the data repository service can be shown using `git rdm show`. For example, for the publication whose Figshare publication ID is ?????? and DOI is `????`, we have

```
```

## License
???????????

## Contact

Please send any questions or comments about Git-RDM via email to [Christian Jacobs](http://christianjacobs.uk) at <christian@christianjacobs.uk>. Any bugs should be reported using the project's [issue tracker](http://github.com/ctjacobs/git-rdm/issues). Contributions are welcome and should be made via a pull request.
