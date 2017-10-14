# Overview

## In this file, I will:
1. Verify that null and alternative hypothesis are formulated correctly;
2. Verify that the data supports the project
 "if the a data has the appropriate features (variables) to answer the question, and if the data was properly pre-processed to extract the needed values"
 
3. Choose an appropriate test to test the null hypothesis
4. Provide additional comments, suggestions, and a suggested appropriate statistical test with justification.

# 1. Hypothesis review
The idea to be investgated is the following:
"Older people are less likely than younger people to use citibikes overnight (19:00-5:00)"
This is an interesting question, and I think it will come down to what designates "older"  versus "younger" people.
The idea above is somewhat imprecise, leaving it open to multiple interpretations. One such interpretation is the null and alternative hypothesis provided in the assignment: <br>


The following null hypothesis and alternative hypothesis are described. <br>
Null: "The ratio of older people (>=40) biking at night over all older people biking during a day is _the same_ or _higher_  than the ratio of younger people (< 40) biking at night to all the younger people biking during a day"
<p>
Alternative: The ratio of younger people biking at night over the total number of younger people riding a bike during a 24 hour period is greater than the ratio of older people riding a bike at night over the number of older people who ride bikes in the 24 hour period.
<p>

One way to write the null hypothesis that should be considered is that instead of having the proportions in a kind of inequality 
(young proportion is less than or equal to old proportion), the proportions should be set as equal to each other,
since we know nothing about the proportions. The default assumption should be that they are equal instead of an inequality.

The student chose an alpha of 0.05, meaning that under the null hypothesis, the probability of obtaining a result as least as significant would be 5%. 

<p>

# 2. Data review

The idea of older people having a different probability than younger people of riding Citibikes at certain times of day 
requires the use of age data and time data. Since we only care about when someone is attempting
to use a bike, we can only consider the start time of the citibike trip.

This is accurately reflected in the data chosen. The data are also cleaned and processed to have
only relevant information (age and trip start date in datetime format). This is all that is needed.

<p>

# 3. Choosing a Statistical Test
<p>
The null hypothesis is that these ratios are equal. We need to come up with some statistic with a dstribution under the null hypothesis. Let's say the null hypothesis is true.
We look at old people riding bikes. Some are riding at night, some in the morning/day. There is a fraction for each. The same applies to young people. Since we only care about night riders, there is an "old people" Bernoulli distribution and a "young people" Bernoulli distribution of ridership (binary yes/no to answer the question "is the ride at night?" for young people and old people). 

In the end, we are dealing with categorical data. We are categorizing by "young" and "old" and then also by "day" or "night."

Since we have these categorical data, we can ask if the data match an expected ratio (as in the hypotheses). We should assume no a priori expectation, as the null hypothesis should assume equal ratios between groups. There are two variables, and both variables have two categories ("old/young" and "day/night"). So, the desired statistical test is the <b>chi-square test for association</b>.

# 4. Suggestions

This question, while interesting, has many similar applications by itself. If one goes through and writes the code to perform these tests, it would be very easy to also consider other personal factors regarding day and night ridership. For example, it could be suspected that women are also less likely to ride at night than men are. Controlling for other personal factors like sex would be an interesting addition to this project. In addition, it could be interesting to see where given populations are more or less likely to ride at night by incorporating geographic data.


