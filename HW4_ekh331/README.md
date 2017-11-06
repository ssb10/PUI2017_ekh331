# Homework 4

Aside from group work required for assignment 2, this homework was completed individually. Partners for part 2 were Jon Kastelan and Andrew Nell. 

## Assignment 1

I reviewed the Homework 3 part 2 of a classmate. I consulted the flowchart used in the slides for PUI session 4 to choose a statistical test. The markdown file with the review can be found at https://github.com/ekh331/PUI2017_ekh331/blob/master/HW4_ekh331/CitibikeReview_ekh331.md 
or in the pull request to the original student's repository.

## Assignment 2

### I worked together with Jon Kastelan and Andrew Nell on this part of the homework. We worked on our own for the most part, but discussed our findings together and debated each other for each study.

| **Statistical Analyses	|  IV(s)  |  IV type(s) |  DV(s)  |  DV type(s)  |  Control Var | Control Var type  | Question to be Answered | _H0_ | alpha | Link to Paper **| 
|:----------:|:----------|:------------|:-------------|:-------------|:------------|:------------- |:------------------|:----:|:-------:|:-------| 
|Multiple Regression|2, year and PDSI| Interval, Continous ordinal |1, NVDI| Continuous |n/a|n/a|Does climate wetness from PDSI affect the NVDI of China?|Climate wetness via PDSI per year has no effect on NVDI|0.05|(http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0126044)|
Chi-squared	| 1, Gender | Nominal | 1, Visual stress color choice| categorical | age | continuous | 	Does gender affect visual stress color overlay preference? | There is no statistically significant difference between gender and visual stress color overlay choice | 0.04 | (http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0163326) |
Logistic Regression	| 7, age, bmi, waist circ, history of antihypertensive drug treatment, high blood sugar, physical activity, fruit/healthy consumptions | continuous ordinal, ordinal | 1, diabetes incidence| ordinal | gender, year of cohort | categorical | 	Can a risk factor model evaluate risk for and predict diabetes incidence? | Variables don't have significant predictive power to evaluate risk for diabetes incidence| 0.05 |(http://care.diabetesjournals.org/content/26/3/725?26/3/725) |
  ||||||||| 
  
  # FBB why did you look for a paper not on PLOS one? I specifically indicated to look for papers on plos one. the statistical significance you state for the Log Reg 0.05 I cannnot find in the paper. Plos One is rigorous about these things and would likely not acceot a paper that does not explicitly state the significance ahead of time
  
  ## Assignment 3
  
For this assignment, the z-test and chi-square test were computed based on examples in professor Bianco's provided skeleton notebook. The results of the tests were compared to standard tables, where the null hypothesis could then be rejected or fail to be rejected.

## Assignment 4

A function was written for this assignment to perform the operations for questions one and two within this part of the homework. 
The input required is simply the problem number, which is either 1 or 2, corresponding to:<br>
  1: Test whether trip durations of bikers is different during day vs night
  2: Test whether age of bikers is different for Manhattan vs Brooklyn
  <p>
  Each problem tests whether the distribution of feature_of_interest (duration or age) is 
  different for type_1 vs type_2 (day vs night, or Manhattan vs Brooklyn)
  <p>
 In order to account for the geographical differences between Manhattan and Brooklyn for the second question in this part, a line was drawn between two coordinate points that served as a decision boundary above which rides would count as Manhattan-origin and below which rides would count as Brooklyn-origin.
