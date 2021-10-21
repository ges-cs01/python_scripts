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

This will generate a translatoe.csv. Very handy to load it in Google Sheets and swiftly translate multiple words using the function [=GOOGLETRANSLATE(cell; "source_lang"; "target_lang")](https://support.google.com/docs/answer/3093331?hl=en) and the [fill handle](https://support.microsoft.com/en-us/office/copy-a-formula-by-dragging-the-fill-handle-in-excel-for-mac-dd928259-622b-473f-9a33-83aa1a63e218) tool of a cell that automatically extend formulas.
