# aman
A simple tool to manager shell aliases

#### INSTALLATION

1. clone the repo: `git clone git@github.com:HmzAli/aman.git`
2. cd into the repo `cd aman` and run `python setup.py install`
3. After the installation is completed, add the following line to the profile of your default shell (e.g. `bashrc`/ `zshrc`)

```shell
source $HOME/.aman/aliases
```
4. Open a new shell session and type `aman` to verify installation

#### USAGE

To add an alias:
```shell
aman <alias>=<command>
```

For more commands, type `--help`.

##### NOTE:
After adding an alias, you will need to create a new shell session for it to be activated.
