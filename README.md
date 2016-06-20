# Git-RDM

Git-RDM is a Research Data Management (RDM) plugin for the [Git](https://git-scm.com/) version control system. It interfaces Git with data hosting services to manage the curation of version controlled files using persistent, citable repositories. This facilitates the sharing of research outputs and encourages a more open workflow within the research community.

Much like the standard Git commands, Git-RDM allows users to add/remove files within a 'publication staging area'. When ready, users can readily publish these staged files to a data repository hosted either by Figshare or Zenodo via the command line. Details of the files and their associated publication(s) are then recorded in a local SQLite database, including the specific Git revision (in the form of a SHA-1 hash), publication date/time, and the DOI, such that a full history of data publication is maintained.

## Dependencies

Git-RDM mostly relies on the standard Python modules and, of course, Git. However, two extra modules are needed:

* [GitPython](https://gitpython.readthedocs.io), to access the Git repository's information.
* [PyRDM](https://github.com/pyrdm/pyrdm), to handle the publishing of files.

Both of these dependencies can be installed via `pip` using

```
sudo pip install -r requirements.txt
```

Alternatively, users can install Git-RDM and its dependencies with [Conda](http://conda.pydata.org/); see the details in the next section.

Note that once PyRDM is installed, you will need to setup Figshare/Zenodo authentication tokens and copy them into the PyRDM configuration file in order to publish your data. See the [PyRDM documentation](https://pyrdm.readthedocs.io/en/latest/getting_started.html) for instructions on how to do this.

## Installing

Git-RDM can either be installed from source, or via Conda packages; see the appropriate sub-section for more details. Once Git-RDM is installed, Git should automatically detect the plugin and recognise the `rdm` command; for example, run `git rdm -h` to list the RDM-related subcommands described in the Usage section below.

### From source

After downloading or cloning this software using

```
git clone https://github.com/ctjacobs/git-rdm.git
```

a system-wide installation can be achieved by navigating to the git-rdm directory

```
cd git-rdm
```

and running

```
sudo python setup.py install
```

Alternatively, a local user installation can be achieved using

```
python setup.py install --prefix=/path/to/custom/install/directory
```

and adding `/path/to/custom/install/directory/bin` to the `PATH` environment variable:

```
export PATH=$PATH:/path/to/custom/install/directory/bin
```

### Conda package

Conda users can install the Git-RDM package and its dependencies using

```
conda install -c ctjacobs -c pypi -c auto -c ioos -c conda-forge git-rdm
```

## Usage

The Git-RDM plugin comes with several subcommands. The following subsections demonstrate, with examples, how to use each of them. 

### git rdm init

In order to start using Git-RDM, the command `git rdm init` must first be run within the Git repository containing the data files to be published. This creates a new directory called `.rdm` containing a database file `publications.db`. All data publication details are stored within this file. Note that this command is similar to `git init` which initialises a new Git repository and creates the `.git` control directory. As an example, consider the `test` directory below, containing files `test1.txt`, `test2.txt` and `test3.png`:

```
~/test $ git rdm init
~/test $ ls -lrta
total 68
drwx------ 60 christian christian 20480 Jun 12 23:39 ..
-rw-r--r--  1 christian christian     5 Jun 12 23:39 test1.txt
-rw-r--r--  1 christian christian     5 Jun 12 23:39 test2.txt
-rw-r--r--  1 christian christian     5 Jun 12 23:39 test3.png
drwxr-xr-x  7 christian christian  4096 Jun 12 23:40 .git
drwxr-xr-x  4 christian christian  4096 Jun 12 23:40 .
drwxr-xr-x  2 christian christian  4096 Jun 12 23:40 .rdm
```

### git rdm add

Once the RDM database has been initialised, data files may be added to the 'publication staging area' using `git rdm add` as follows:

```
~/test $ git rdm add test*
~/test $ git rdm ls
git-rdm INFO: Files staged for publishing:
git-rdm INFO: 	/home/christian/test/test1.txt
git-rdm INFO: 	/home/christian/test/test3.png
git-rdm INFO: 	/home/christian/test/test2.txt
```

The file being added for publication must first have been committed within the Git repository, otherwise Git-RDM will refuse to add it.

### git rdm rm

Files can also be removed from the publication staging area using `git rdm rm`:

```
~/test $ git rdm rm test*
```

### git rdm publish

Once all the files are ready to be published, the `git rdm publish` command can be used to publish the files to a data repository hosted by a particular service. The hosting service must be specified as an argument, and can be either `figshare` or `zenodo`. Support for new services can be readily added by extending the [PyRDM library](https://pyrdm.readthedocs.io). Some basic publication information is obtained from the user, for example the title, description, and keyword metadata. PyRDM then interfaces with the hosting service and publishes the data files:

```
~/test $ git rdm publish figshare
Private publication? (y/n): y
git-rdm INFO: Publishing as a private repository...
Title: Test Article
Description: Testing 
Tags/keywords (in list format ["a", "b", "c"]): ["hello", "world"]
pyrdm.figshare INFO: Testing Figshare authentication...
pyrdm.figshare DEBUG: Server returned response 200
pyrdm.figshare INFO: Authentication test successful.

pyrdm.publisher INFO: Publishing data...
pyrdm.publisher INFO: Creating new fileset...
pyrdm.publisher INFO: Adding category...
pyrdm.publisher INFO: Fileset created with ID: 3428222 and DOI: 10.6084/m9.figshare.3428222
pyrdm.publisher DEBUG: The following files have been marked for uploading: ['/home/christian/test/test1.txt', '/home/christian/test/test3.png', '/home/christian/test/test2.txt']
pyrdm.publisher INFO: Uploading /home/christian/test/test1.txt...
pyrdm.publisher INFO: Uploading /home/christian/test/test3.png...
pyrdm.publisher INFO: Uploading /home/christian/test/test2.txt...
pyrdm.publisher INFO: All files successfully uploaded.
```

The publication information is stored in the local database, and can be viewed using `git rdm ls`. Note that Git-RDM currently publishes the files using the current `HEAD` revision of the Git repository, and not the revision at which the files were first added using `git rdm add`.

### git rdm ls

`git rdm ls` is used to list and keep track of which data files have been published, and which files are still in the staging area. Users can choose to list each file, followed by any DOIs associated with it (by default) as follows:

```
~/test $ git rdm ls
git-rdm INFO: Published files:
git-rdm INFO: 	/home/christian/test/test1.txt
git-rdm INFO: 		10.6084/m9.figshare.3428222 (2016-06-13 @ 00:29:03, revision '1eeccabba810b8c91eef82e692713fdb05ca4a32')
git-rdm INFO: 	/home/christian/test/test2.txt
git-rdm INFO: 		10.6084/m9.figshare.3428222 (2016-06-13 @ 00:29:03, revision '1eeccabba810b8c91eef82e692713fdb05ca4a32')
git-rdm INFO: 	/home/christian/test/test3.png
git-rdm INFO: 		10.6084/m9.figshare.3428222 (2016-06-13 @ 00:29:03, revision '1eeccabba810b8c91eef82e692713fdb05ca4a32')
```

Users can also choose to list the DOIs first and the files associated with it afterwards:

```
~/test $ git rdm ls --by-doi
git-rdm INFO: Published files:
git-rdm INFO: 	10.6084/m9.figshare.3428222
git-rdm INFO: 		/home/christian/test/test1.txt (2016-06-13 @ 00:29:03, revision '1eeccabba810b8c91eef82e692713fdb05ca4a32')
git-rdm INFO: 		/home/christian/test/test3.png (2016-06-13 @ 00:29:03, revision '1eeccabba810b8c91eef82e692713fdb05ca4a32')
git-rdm INFO: 		/home/christian/test/test2.txt (2016-06-13 @ 00:29:03, revision '1eeccabba810b8c91eef82e692713fdb05ca4a32')
```

To check the raw, unformatted contents of the entire publications database, use the `--raw` flag:

```
~/test $ git rdm ls --raw
git-rdm INFO: Database dump:
git-rdm INFO: id, path, date, time, sha, pid, doi
git-rdm INFO: 13, /home/christian/test/test1.txt, 2016-06-13, 00:29:03.016951, 1eeccabba810b8c91eef82e692713fdb05ca4a32, 3428222, 10.6084/m9.figshare.3428222
git-rdm INFO: 14, /home/christian/test/test3.png, 2016-06-13, 00:29:03.016951, 1eeccabba810b8c91eef82e692713fdb05ca4a32, 3428222, 10.6084/m9.figshare.3428222
git-rdm INFO: 15, /home/christian/test/test2.txt, 2016-06-13, 00:29:03.016951, 1eeccabba810b8c91eef82e692713fdb05ca4a32, 3428222, 10.6084/m9.figshare.3428222
```

### git rdm show

The full publication record maintained by the data repository service can be shown using `git rdm show`. It expects two arguments: the name of the hosting service (`figshare` or `zenodo`) and the publication ID. For example, for the publication whose Figshare publication ID is 3428222 (and DOI is `10.6084/m9.figshare.3428222`), the (truncated) output is:

```
~/test $ git rdm show figshare 3428222
pyrdm.figshare INFO: Testing Figshare authentication...
pyrdm.figshare DEBUG: Server returned response 200
pyrdm.figshare INFO: Authentication test successful.

git-rdm INFO: {
    "authors": [
        {
            "full_name": "Christian T. Jacobs",
            "id": 554577,
            "is_active": true,
            "orcid_id": "0000-0002-0034-4650",
            "url_name": "Christian_T_Jacobs"
        }
    ],
    "categories": [
        {
            "id": 2,
            "title": "Uncategorized"
        }
    ],
    "citation": "Jacobs, Christian T. (): Test Article. figshare.\n 10.6084/m9.figshare.3428222\n Retrieved: 23 32, Jun 12, 2016 (GMT)",
    "confidential_reason": "",
    "created_date": "2016-06-12T23:28:54Z",
    "custom_fields": [],
    "defined_type": 4,
    "description": "Testing",
    "doi": "10.6084/m9.figshare.3428222",
```

## License
This software is released under the MIT license. See the file called `LICENSE` for more information.

## Citing

If you use Git-RDM during the course of your research, please consider citing the following paper:

* C. T. Jacobs, A. Avdis (2016). Git-RDM: A research data management plugin for the Git version control system. *Journal of Open Source Software*, 29. DOI: [10.21105/joss.00029](http://dx.doi.org/10.21105/joss.00029)

## Contact
Please send any questions or comments about Git-RDM via email to [Christian Jacobs](http://christianjacobs.uk) at <christian@christianjacobs.uk>.

Any bugs should be reported using the project's [issue tracker](http://github.com/ctjacobs/git-rdm/issues). If possible, please run Git-RDM with debugging enabled using the `-d` flag after `git rdm` (e.g. `git rdm -d publish figshare`) and provide the full output.

Contributions are welcome and should be made via a pull request.
