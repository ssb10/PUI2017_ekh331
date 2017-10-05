## Homework 3, PUI 2017
## Author: Emily Hansen


### The assignments in this lab were completed individually. Skeleton code for assignment one was provided by @fedhere for student use. @fedhere also provided an example of the process for assignment 2 of this homework, which was referenced during the assignment. Standard python libraries were used (such as numpy, pandas, matplotlib, etc)

The homework had three parts:

In part one of the homework, 100 samples, each with a size ranging from 10 to 2000, were generated via random seed (for reproducibility) with the same population mean. Each of five distribution types were used to distribute these samples, resulting in 500 samples distributed across 5 distributions. 
The sample mean was plotted against the sample size for each distribution. The result was that the larger the sample size, the closer the sample mean was to the population mean (as can be seen in figures), supporting the law of large numbers. 

I personally developed a function to do this part of the homework so that redundant code was spared as much as possible.

Part one skeleton code: https://github.com/fedhere/PUI2017_fb55/blob/master/HW3_fb55/Assignment1.ipynb


In part two of the homework, a data-driven environment was set up with CitiBike data. A null and alternative hypothesis were established. I thought that perhaps "customers" took longer trip durations on average than "subscribers", who were possibly taking shorter trips commuting to work or school.
The data were downloaded and converted into a pandas dataframe, which was truncated and then analyzed to reveal average trip duration by user type.

Part two example referenced: https://github.com/fedhere/PUI2017_fb55/blob/master/HW3_fb55/citibikes_gender.ipynb

In part three of the homework, we were to continue a lab that was started in class the week before. Given a mean and standard deviation of commute time for and old bus route, could we say with confidence whether a new bus route was faster on average?
A null hypothesis and alternative hypothesis were developed, the former being that the new bus commute time was, on average, greater than or equal to the average old bus route's commute time.
The alternative hypothesis stated that the new bus commute time was, on average, less than that of the old bus commute time. Alpha was set to be 0.05.
A random normal distribution of 100 points was generated with a mean of 36 and standard deviation of 6 to represent the old bus commute times.
The new bus times were downloaded from the Internet as a .txt file and manipulated.
The z statistic was calculated to be greater than alpha, meaning that the new bus commute time, on average, was significantly shorter than that of the old bus route.
