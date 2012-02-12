About
=====

Nduko is a variant of Sudoku in which the game takes place on an n*n grid.

An Nduko puzzle looks a little like this:

      n 
    <--->
    -----------------  X
    |   |   |   |   |  | 
    -----------------  |
    |   |   |   |   |  | 
    -----------------  n
    |   |   |   |   |  |
    -----------------  |
    |   |   |   |   |  |
    -----------------  X

The grid is divided into n*n subsections. Each subsection is itself divided into n*n sections. In the example above, n = 4

Todo
====

Pretty much everything except exact cover solving.

Hacking
=======
Nduko is written in Python. Most of the useful (non UI/IO) code is contained
in the python package `nduko`.

Nduko source code is maintained using the Git version control system and is
available at the following location:

    git://github.com/kragniz/nduko.git

You can download the source code from the Git repository by doing:

    $ git clone git://github.com/kragniz/nduko.git

Later, to take the new commits you just have to do:

    $ git pull

If you have any code you want in the master branch, create a pull request on
Github, or email the mail author with a patch.

License
=======

Nduko is released under the GNU General Public License (GPL) version 3 or
later, see the file "COPYING" for more information.
