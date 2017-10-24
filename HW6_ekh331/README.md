# Homework 6
### ekh331

This assignment was completed indivudually.
<p>
In this assignment, data were downloaded and moved via PUIDATA and manipulated in the 
confines of a skeleton notebook provided.
<p>
Notably, geopandas was utilized to create geodataframes from a CSV and a shapefile of energy consumption and building sizes 
in Manhattan.
Once the dataframes were cleaned, exploratory scatter matrices were made from the 
data once converted to a numerical format.
From there, the relationship between various building attributes, such as 
number of units and square footage reported by multiple sources, was determined.<br>
<p>
The strength of a chosen independent variable was evaluated by plotting number of
building units against a function of energy consumption and vice versa. The resulting
plots were fitted with a best fit line and compared through the chi-squared statistic
to determine goodness of fit in a log space.
A second-degree polynomial model was then prepared and compared to the 
first-degree linear model.
The R-squared values for all models were poor (> 0.2), though it was slightly higher
in the second-degree polynomial.
<p>
Likelihood ratio analysis took place to compare the second degree polynomial model to
the first-degree one. The p-value was significantly less than the critical value
of 0.05, meaning that we can reject the null hypothesis that a first and second
degree polynomial model describe the same data in the same way.


