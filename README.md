# scripts
Scripts to ease my daily work

## Aliases
In order to use the scripts from the command line, edit the .bashrc and append the following lines:
* Add the path to the repo to $PATH

    `export PATH="~/<path_to_repo>/scripts/ros_scripts:$PATH"`

* Set an alias for each of them:

    `alias cm="catkin_make.sh"`
    
## Usage    
Now, you're ready to use your awesome scripts! 

* Just type in the console: `cm` or `cm <pkg_name>`