# python_scripts
Saving some useful small stuff.

## walk.py
List all files in the directory and subdirectories with their respective sizes. Very useful to __pipe it with grep__ and find a file that you don't remember the entire name nor where it is exactly located. To change the directory you're searching just change the argument in the os.walk("your/dir/here")

Usage:     
  
    python3 walk.py 
    
And yes, to a more direct list of files you can always use this one line command in Unix:
   
    find "$PWD" -type f

## translatoe.py
From a file.txt generate a file.csv that contains a list and a counter of the words used in the .txt

Usage:

    python3 translatoe.py file.txt

This will generate a translatoe.csv. Very useful to load it in Google Sheets and use it as follows:

[![link to youtube video on how to translate multiple words with google sheets.](http://img.youtube.com/vi/AoHqkGm2G0U/0.jpg)](http://www.youtube.com/watch?v=AoHqkGm2G0U "How to translate multiple words with Google Sheets")
