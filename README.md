# Crack-Caesar

This is a program that will find and return the shift that a .txt file has been encoded with (Caesar Cipher)

To use this program, move the .txt file you want to crack into the same directory as crackcaesar.py (or be prepared to type the full directory path into the terminal!)

Open up a command prompt / terminal / equivalent and navigate the directory containing your file(s) and crackcaesar.py

This program uses commandline arguments to function, I'd recommend first looking at what commands are available.

To do this, enter python substitution.py -h into your terminal - this will display all the commands.

The first and only required command is -i "my_file".txt where "my_file" is the name of the file you wish to crack.

There is also a -n command which limits the number of characters the program will read.

Finally, you can also load in your own dictionary of words using the -d command. See english words.dict for formatting.

An example line in a windows command prompt would be as follows:

python crackcaesar.py –i “100-0-20.txt” –n 1000 

will search for the shift in 100-0-20.txt by reading the first 1000 characters in the file, in this case, the shift returned should be 20.
