# Git-RDM

Git-RDM is a Research Data Management (RDM) plugin for the [Git](https://git-scm.com/) version control system.

Much like the standard Git commands, Git-RDM allows users to add/rm files in a 'publication staging area'. When ready, users publish these staged files to a repository hosting service; currently only [Figshare]() and [Zenodo]() are supported.

## Commands



# Dependencies

Git-RDM mostly relies on the standard Python modules. However, two extra modules are needed:

* [GitPython], to access the Git repository's information.
* [PyRDM](https://pyrdm.readthedocs.io), to handle the publishing of files.

Both of these dependencies can be installed via `pip` using

```
sudo pip install -r requirements.txt
```

# Installing



# Contact

Please send any questions or comments about Git-RDM via email to [Christian Jacobs](http://christianjacobs.uk) at <christian@christianjacobs.uk>. Any bugs should be reported via the project's [issue tracker](http://github.com/ctjacobs/git-rdm/issues).
