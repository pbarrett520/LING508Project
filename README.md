# Chinese Character Pronunciations Helper

### What's the point?
The program is very simple. It takes a single Chinese character and one of eight prespecified 
Chinese dialect names as input, and give the character's pronunciation in the specified dialect
as the output. See the file `documentation.md`in the `docs` directory for more info about how to run the 
program.

### What's up with the data set?
The data set can be found in `pronunciations.txt` in the `data` folder. Information for each
character was scraped from the source Wikitionary.com in order ascending order according to the charaters
unicode value. What you see in the text file is the data of characters that did not fail in 
the process of webscraping. Truth be told, this text file needs to be replaced with a csv,
to make the data more machine-readable. So if you are wondering why the characters in the data
are there and not others, that's why.

### To-do List

- Implement a controlled vocabulary for dialect inputs using enums
- Overhaul how data is collected and stored. There should be a separate `.sql`file for the
data to live in, so one can actually see how the SQL database itself is structured without having to use the SQL CLI.
Also, should look into if there are alternatives to webscraping to collect my data. 
- Configure this to run in a Docker container.
- Make the UI look pretty.

