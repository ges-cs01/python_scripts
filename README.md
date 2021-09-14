# python_scripts
Saving some useful small stuff.

## walk.py
List all files in the directory and subdirectories with their respective sizes. Very useful to __pipe it with grep__ and find a file that you don't remember the entire name nor where it is exactly located. To change the directory you're searching just change the argument in the os.walk("your/dir/here")

Usage:     
  
    python3 walk.py 
    
And yes, to a more direct list of files you can always use this one line command in Unix:
   
    find "$PWD" -type f



