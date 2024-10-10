Vital Tracking Database
I wrote this program to keep track of my vitals and store them in a local database.

Description
Currently it takes in daily vital readings and can display a specific date or dates upon request. It allows for one user
and the created database is stored in the same folder as the program.

Installing
The program should run if you have Python 3.12+ installed. The .py file should be placed in its own folder as the first
time it is run it will create a .db file into that folder. If multiple users would like to use the program just create a
new folder and copy the file into the new folder. When run it will produce a new database in that folder.


Using the Program

Input
⦁	Date: FORMAT MUST BE    MM/DD/YYYY
⦁	Weight:                 999.9
⦁	Body Fat:               99.9
⦁	Blood Sugar:            999
⦁	Pulse:                  999
⦁	Blood Pressure:         999/999

Most inputs can use your preferred formatting but these are the suggested formats to fit the columns.  In order for the
program to function properly dates MUST be entered as MM/DD/YYYY. Use 'SUBMIT' for current days vitals only. To submit
vitals for any other day OR to update the current date's vitals use 'UPDATE'.

Viewing Vitals
⦁   Add single date: The first box is automatically populated with the current date. If you would like to view a
                     different date just change it using the MM/DD/YY format. When you have desired date click
                     'Single Date' and it will be added to the table. You can add single dates multiple times to the
                     table.

⦁   Multiple Dates:  Multiple dates can be added to the table using 'Multiple Dates'. Use the first input box to enter
                     the earliest date and the second input box for the end of the range. Multiple sets of date ranges
                     can be added to the table.

⦁   CLEAR:           CLEAR will clear ALL data from the display table.

Author
Jon Jarrett
github.com/JonJarrett


Version History
⦁	1.0 
	Initial version with Input and View tabs