# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > * show current working directory path : `pwd`
> > * creating a directory : `mkdir directory_name` 
> > * deleting a directory : `rm -r directory_name`
> > * creating a file using `touch` command : `touch file.txt`
> > * deleting a file : `rm file_name`
> > * renaming a file : `mv old_file_name new_file_name`
> > * listing hidden files : `ls -a`
> > * copying a file from one directory to another : `mv ~/d1/file.txt ~/d2/`
> > * repeat last command : `!!`
> > * show first 10 lines of file : `head file_name`

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > * Lists all files in a directory 
> > * Lists all files in a directory including hidden files 
> > * Displays the long format listing of files 
> > * Displays the long forat listing of files that include the file sizes with prefix 
> > * Displays the long format listing of files including hidden files with file sizes and prefixes 
> > * Displays newest files first based on timestamp 
> > * Displays the long format listing of files that are highlighted and include "/" at the end of each filename

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > * `ls -m`
> > * `ls -r` 
> > * `ls -u`
> > * `ls -1`
> > * `ls -n`

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > `xargs` takes filenames from standard out and uses them as arguments. `xargs` can also parallel process jobs.

 

