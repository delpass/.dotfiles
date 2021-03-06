#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from subprocess import check_call as c

home = os.getenv("HOME") + os.sep
backup_files = [
    '.vimrc',
    '.vim',
    '.tmux.conf',
    '.zshrc',
    '.zsh',
    '.i3',
    '.gitconfig',
]
commands = [
    'git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim'
]


def install():
    if os.path.islink(home + '.vimrc'):
       print "already installed, please use: git pull for update"
       return
    # rename old config files if exists
    for f in backup_files:
	f = home + f
        if os.path.exists(f):
            print "{} renamed".format(f)
            os.rename(f, f + '.old')
    # create symbolic links
    for f in backup_files:
        c('ln -s {0}.dotfiles{2}{1} {0}{1}'.format(home, f, os.sep) , shell=True)

    # run commands
    for cmd in commands:
        print cmd
        c(cmd, shell=True)

    print u'''
    please run in vim :PluginInstall
    Install complete
    Install packages: sudo apt-get install vim tmux zsh i3
    '''


if __name__ == '__main__':
    install()
