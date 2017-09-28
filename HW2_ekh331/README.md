# PUI 2017 Homework 2

Author: Emily Hansen

This homework assignment was completed individually. Libraries imported and utilized for the assignment are
all part of the Python Standard Library or are otherwise widely used, including:
<p>
<b>argparse</b> for parsing command-line arguments in order to successfully implement command line arguments for grading; <br>
<b>json</b> for handling data obtained for MTA server queries;<br>
<b>urllib2</b> for opening the MTA query URL; <br>
<b>pandas</b> for converting data structures in assignment 3; <br>
<b>os</b> for handling operating system interfaces; and<br>
<b>matplotlib</b> for plotting the assignment 3 dataframe.
<p>
The assignments contained in this directory are as follows:
<p>
<b>show_bus_locations</b>: Assignment 1. In order to complete the assignment, a JSON
file from the MTA was obtained via API key access and parsed to locate the number of
active buses, bus line, and bus latitude and longitude coordinates. The primary lesson
learned was how to navigate the mass of data in such a queried JSON file, having to 
search within dictionaries of dictionaries and lists and producing a real-time 
bus-tracking output.
<p>
<b>get_bus_info</b>: Assignment 2. Similar to Assignment 1, a JSON file from the MTA
was obtained via API key access and parsed to provide information on the upcoming 
stops for all buses of a given MTA line. Attention to file format was emphasized
by requiring the conversion of the output text to a CSV file containing the latitude, 
longitude, upcoming stop name, and status for every bus in a given bus line. It was 
discovered that although the csv module was initially intended to be used, built-in 
Python functions such as open() as f and f.write() to take the text output, parsed
from the JSON file, and allow it to be written as a file with a .csv extension.
<p>
<b>HW2_3</b>: Assignment 3. This assignment increased familiarity with pandas, a 
data analysis library. The environment variable DFDATA was used in the compute 
environment to access a CSV file in the CUSP data catalog. The chosen file was 
converted into a pandas dataframe and manipulated, truncated to show a short 
display of two columns with numerical values, which were then plotted against each 
other as a scatterplot. The numerical columns happened to be latitude and longitude,
which resulted in a scatterplot of relative locations.
