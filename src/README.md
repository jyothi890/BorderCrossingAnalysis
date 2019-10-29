# Approach

The code is divided into 3 files for better readability



- border_crossing_analysis.py

This is the starting script for the analysis. The input parameters are validated before the call to analysis function. Once the input parameters are validated, a call to report function is made. The report function, makes a call to analysis_metrics.py script were  total no of crossings and running monthly average metrics are calculated.

- analysis_metrics.py

This script holds the functions that perform metrics on the given data.This script internally calls analysis_utils.py script to parse the date column.

- analysis_utils.py

This script holds the functions that perform repetitive utility actions on the given data.

By dividing code into these 3 scripts allows the scalability of the code. For example, new metric functionalities could be added to analysis_metrics.py and utility functionalities could be added to analysis_utils.py.

# Development Process

-  Wrote a temporary procedure to print the first data row using python csv library.
-  Identified that date column need to be modified in order to calculate total no of crossings and running monthly average.
Developed the time_of_bordercrossing to extract the year and month.
-  Tried out various design structure for nested dictionary that could serve the purpose to sum no of crossings for a month for a combination of border and measure
- Once design of nested dictionary and total no of crossing was captured appropriately  I moved on to calculate the running monthly average.
- Realized that a supporting nested dictionary is needed to hold cumulative totals upto the month in consideration and list data structure is needed to hold running monthly average calculated as calculation is done from starting (lowest) month .
- The final list holds running monthly average in ascending order which was reverse before writing to the output file.
