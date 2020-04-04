# CheckFileForCopiesSize

Reads CSV files and checks a predefined field for a value greater than 70.

In case of an error, an error message is returned and otherwise a success message.

# Example FileName
In this example the filenames ms_pd1_*******  and ms_pd5_******** the stars are variable name conversion.
One way to make new files available for reading is to create a new FileList class and use it in the Runner script.

# Example to run
python src/run.py /directory/path/fileFolderToRead/