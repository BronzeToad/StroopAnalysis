# Statistical Analysis – The Stroop Effect

In a Stroop test, participants are presented with a list of words, with each word displayed in a color of ink. The participant’s task is to say out loud the color of the ink in which the word is printed. The task has two conditions: a congruent words condition, and an incongruent words condition.

In the congruent words condition, the words being displayed are color words whose names match the colors in which they are printed. In the incongruent words condition, the words displayed are color words whose names do not match the colors in which they are printed. In each case, we measure the time it takes to name the ink colors in equally sized lists.

Experimental findings have shown that when participants are asked to name the color of the word their response has a higher rate of error, and takes longer, when the name of the color does not match the color of the ink. This effect is known as the Stroop effect – the delay in reaction time between congruent and incongruent stimuli. [\[1\]][1] <br> <br>

- You can try the Stroop test out for yourself here: [Interactive Stroop Test][2]
- The rest of this page explores Stroop test data that can be found here: [Stroop Test Dataset][3] <br> <br>

### Independent Variable
The variable in an experiment that is changed: for a Stroop effect experiment, the independent variable is – the colors in which the words are printed. [\[4\]][4] <br> <br>

### Dependent Variable
The variable in an experiment that is measured: for a Stroop effect experiment, the dependent variable is – the time it takes each participant to identify the colors for all the words provided. [\[4\]][4] <br> <br>

### Alternative Hypothesis
The outcome a researcher is anticipating: for a Stroop effect experiment, the alternative hypothesis is – for the sample population, the average response time under the congruent words condition is less than the average response time under the incongruent words condition. <br> <br>

### Null Hypothesis
The opposite of the alternative hypothesis: for a Stroop effect experiment, the null hypothesis is – the difference between the mean response times for the sample populations is not statistically significant when comparing those under the incongruent words condition and those under the congruent words condition. <br> <br>

### Statistical Test
For this dataset, we do not know the population standard deviation, and the sample size is less than 30; this means we cannot use a z-test. [\[5\]][5]

A good test to use for this project is a paired sample t-test. However, several assumptions must be met in order for paired sample t-test results to be trusted. [\[6\]][6]
- The observations are independent
- The data needs to be continuous when measured on a ratio or interval scale
- The data should be roughly normally distributed. 
  - The paired sample t-test is quite robust to violations of this assumption, and the test results can be considered valid so long as there isn’t a major violation of normality. <br> <br> <br> <br>


## Descriptive Statistics

---
<br>

The first step before we can analyze the dataset is to import the sample dataset into Python. We’ll read the data using the pandas library. After that, we can print the data frame to get an idea of how the data is structured.

~~~python
# import data and take a look
import pandas as pd

df = pd.read_csv('stroopData.csv')
print(df)
~~~

|      | Congruent | Incongruent |
| ---: | --------: | ----------: |
|    0 |    12.079 |      19.278 |
|    1 |    16.791 |      18.741 |
|    2 |     9.564 |      21.214 |
|    3 |     8.630 |      15.687 |
|    4 |    14.669 |      22.803 |
|    5 |    12.238 |      20.878 |
|    6 |    14.692 |      24.572 |
|    7 |     8.987 |      17.394 |
|    8 |     9.401 |      20.762 |
|    9 |    14.480 |      26.282 |
|   10 |    22.328 |      24.524 |
|   11 |    15.298 |      18.644 |
|   12 |    15.073 |      17.510 |
|   13 |    16.929 |      20.330 |
|   14 |    18.200 |      35.255 |
|   15 |    12.130 |      22.158 |
|   16 |    18.495 |      25.139 |
|   17 |    10.639 |      20.429 |
|   18 |    11.344 |      17.425 |
|   19 |    12.369 |      34.288 |
|   20 |    12.944 |      23.894 |
|   21 |    14.233 |      17.960 |
|   22 |    19.710 |      22.058 |
|   23 |    16.004 |      21.157 |

<br> <br>

Next, we’ll print some high-level descriptive statistics.

~~~python
# get summary statistics
df[['Congruent', 'Incongruent']].describe()
~~~

![Stroop Summary Statistics](summary_stats.png)

<br><br>


## Visualizing Distributions

---
<br>

Often, the best way to discover patterns is to visually compare distributions. However, we first need to reshape the data into a format more conducive to creating visualizations in Python.

~~~python
# clean data frame prior to analysis

# convert index into participant id
df.reset_index(level=0, inplace=True)
df['ParticipantID'] = df['index'] + 1
del df['index']

# reshape data frame into long format
stroop_df = pd.melt(df, \
    id_vars = 'ParticipantID', \
    value_vars = ['Congruent', 'Incongruent'], \
    var_name = 'ConditionType', \
    value_name = 'ResponseTime')

print(stroop_df)
~~~

|      | ParticipantID | ConditionType | ResponseTime |
| ---: | ------------: | :------------ | -----------: |
|    0 |             1 | Congruent     |       12.079 |
|    1 |             2 | Congruent     |       16.791 |
|    2 |             3 | Congruent     |        9.564 |
|    3 |             4 | Congruent     |        8.630 |
|    4 |             5 | Congruent     |       14.669 |
|    5 |             6 | Congruent     |       12.238 |
|    6 |             7 | Congruent     |       14.692 |
|    7 |             8 | Congruent     |        8.987 |
|    8 |             9 | Congruent     |        9.401 |
|    9 |            10 | Congruent     |       14.480 |
|   10 |            11 | Congruent     |       22.328 |
|   11 |            12 | Congruent     |       15.298 |
|   12 |            13 | Congruent     |       15.073 |
|   13 |            14 | Congruent     |       16.929 |
|   14 |            15 | Congruent     |       18.200 |
|   15 |            16 | Congruent     |       12.130 |
|   16 |            17 | Congruent     |       18.495 |
|   17 |            18 | Congruent     |       10.639 |
|   18 |            19 | Congruent     |       11.344 |
|   19 |            20 | Congruent     |       12.369 |
|   20 |            21 | Congruent     |       12.944 |
|   21 |            22 | Congruent     |       14.233 |
|   22 |            23 | Congruent     |       19.710 |
|   23 |            24 | Congruent     |       16.004 |
|   24 |             1 | Incongruent   |       19.278 |
|   25 |             2 | Incongruent   |       18.741 |
|   26 |             3 | Incongruent   |       21.214 |
|   27 |             4 | Incongruent   |       15.687 |
|   28 |             5 | Incongruent   |       22.803 |
|   29 |             6 | Incongruent   |       20.878 |
|   30 |             7 | Incongruent   |       24.572 |
|   31 |             8 | Incongruent   |       17.394 |
|   32 |             9 | Incongruent   |       20.762 |
|   33 |            10 | Incongruent   |       26.282 |
|   34 |            11 | Incongruent   |       24.524 |
|   35 |            12 | Incongruent   |       18.644 |
|   36 |            13 | Incongruent   |       17.510 |
|   37 |            14 | Incongruent   |       20.330 |
|   38 |            15 | Incongruent   |       35.255 |
|   39 |            16 | Incongruent   |       22.158 |
|   40 |            17 | Incongruent   |       25.139 |
|   41 |            18 | Incongruent   |       20.429 |
|   42 |            19 | Incongruent   |       17.425 |
|   43 |            20 | Incongruent   |       34.288 |
|   44 |            21 | Incongruent   |       23.894 |
|   45 |            22 | Incongruent   |       17.960 |
|   46 |            23 | Incongruent   |       22.058 |
|   47 |            24 | Incongruent   |       21.157 |

<br> <br>

Now that our data is ready to go, we can import the Python library used to create all the visualizations in this article: seaborn.

~~~python
# import visualization library
import seaborn as sns
~~~

<br> <br>

### Box Plot & Swarm Plot
First, we’re going to create a box plot and swarm plot; then stack them on top of one another. This visualization allows us to easily spot any outliers.

~~~python
# box plot with swarm to check for outliers

sns.boxplot(data = stroop_df, \
    x = 'ConditionType', \
    y = 'ResponseTime')

sns.swarmplot(data = stroop_df, \
    x = 'ConditionType', \
    y = 'ResponseTime', \
    color = '.25')
~~~

![Box Plot with Swarm](plot_box_swarm.png)

<br>

If we take a look at this plot, we can see that the congruent response times do not have any outliers, but the incongruent response times have a few. <br> <br> <br>

### Histograms
Next, we create a histogram for both the congruent and incongruent response times. Histograms are helpful when analyzing the underlying frequency distribution of a set of continuous data. [\[7\]][7]

~~~python
# histogram

sns.displot(stroop_df, \
    x = 'ResponseTime', \
    col = 'ConditionType', \
    multiple = 'dodge')
~~~

![Histograms](plot_histo.png)

<br>

The histograms reveal that the response time is greater for those data points recorded under incongruent conditions when compared to those recorded under congruent conditions. <br> <br> <br>

### Empirical Cumulative Distributions
Another option for visualizing distributions is performed by charting the empirical cumulative distribution function (ECDF). This plot represents a monotonically increasing line through each datapoint such that the height of the line represents the proportion of observations with a smaller value. This plot has a distinct advantage over a histogram – it directly represents each datapoint. This means there is no bin size to consider. [\[8\]][8]

~~~python
# empirical cumulative distributions

sns.displot(stroop_df, \
    x = 'ResponseTime', \
    hue = 'ConditionType', \
    kind = 'ecdf', \
    palette = 'Accent')
~~~

![Empirical Cumulative Distributions](plot_ecdf.png)

<br>

The ECDF plot suggests that the incongruent condition adversely affects the participant response times. <br> <br> <br>

### Kernel Density Estimations
Our previous attempts at visualizing this data have done a good job comparing the distributions of our different response times, but only if we understand how to read and interpret box plots, swarm plots, histograms, and ECDF plots. 

In order to create a visualization that is quickly and easily understood by the average reader, we turn to the kernel density estimation (KDE) plot. Using KDE plots has several advantages: 
- They allow for simple comparisons between subsets
- Important features of the data are easy to discern (bimodality, central tendency, skew, etc.) [\[8\]][8]

~~~python
# kernel density estimation

sns.displot(stroop_df, \
    x = 'ResponseTime', \
    hue = 'ConditionType', \
    kind = 'kde', \
    fill = True, \
    palette = 'Accent')
~~~

![Kernel Density Estimation](plot_kde.png)

<br>

When comparing the two subsets of data for the congruent and incongruent conditions visualized on our KDE plot, it’s clear that dataset for the incongruent condition is shifted to the right; further reinforcing our idea that participant response times under the incongruent condition (*purple*) are slower than those under the congruent condition (*green*). <br> <br> <br> <br>


## Statistical Analysis 

---
<br>

In the previous section we observed some interesting trends, but now we need to perform some statistical analysis to determine whether we can reject our null hypothesis. Specifically, we want to establish that the difference between mean response times of participants under congruent conditions and incongruent conditions is greater than zero. We do this by rejecting our null hypothesis – the difference between mean response times for the sample populations is not a result of the change between congruent conditions and incongruent conditions. 

For the reasons outlined above, we have decided to utilize the paired sample t-test for this analysis.  We will select a confidence interval of 99%, meaning we reject the null hypothesis if the p-value is less than 0.01. To perform this test, and to calculate our t-distribution and p-value, we will utilize the stats Python package.

~~~python
# paired sample t-test
from scipy import stats

t_val, p_val = stats.ttest_rel(df.Incongruent, df.Congruent)
print("t-distribution = %g" % t_val)
print("p-value = %g" % p_val)

adj_p_val = p_val / 2
print("adjusted p-value = %g" % adj_p_val)
~~~

> t-distribution = 8.02071 <br>
> p-value = 4.103e-08

<br>
This function returns a two-tailed p-value, but our alternative hypothesis is one-tailed; this means we need to adjust the p-value by dividing it by two before comparing it to our selected confidence interval. [9] <br> <br>

~~~python
# adjusted p-value

adj_p_val = p_val / 2
print("adjusted p-value = %g" % adj_p_val)
~~~

> adjusted p-value = 2.0515e-08

<br>
Our adjusted p-value is 2.0515e-08 which is less than the alpha value of 0.01 we determined above. Therefore, the null hypothesis can be rejected, and our alternative hypothesis can be accepted. <br> <br> <br> <br>


## Discussion 

---
<br>

The Stroop test dataset provided evidence that the participants could correctly identify the color of the ink in which the word is printed faster when the colors matched the word (congruent conditions). Through statistical inference we have demonstrated with 99% confidence that this evidence shows a significant effect that can be generalize to the larger population. <br> <br>

Although our statistical analysis confirms the existence of a real effect – as opposed to random chance – it does not provide any explanation for *why* this occurs. <br> <br>

The objective of the Stroop test is to identify the color in which the words are printed. The results suggest that participants read the word before determining the color despite knowing that the word and its meaning are irrelevant to the exercise. <br> <br> 

There are two cognitive processes at play: 
  1. Reading and interpreting the text of the word
  2. Identifying the color in which the word is printed. <br> <br> 

The Stroop test and these data indicate that the reading process inhibits the color-identifying process and causes a delay in the time it takes to determine the color of ink used. <br> <br>

It would be interesting to explore a few variations to this experiment in the future. What happens when the colors are written in a language the reader is not familiar with? What about if the words are gibberish or upside-down? <br> <br> <br>


## References

---
<br>

[1]: https://en.wikipedia.org/wiki/Stroop_effect "Wikipedia - Stroop Effect"
[2]: https://faculty.washington.edu/chudler/java/ready.html "Interactive Stroop Test"
[3]: https://drive.google.com/file/d/0B9Yf01UaIbUgQXpYb2NhZ29yX1U/ "Stroop Test Dataset"
[4]: https://www.verywellmind.com/what-is-the-stroop-effect-2795832 "The Stroop Effect: Naming a Color but Not the Word"
[5]: https://www.analyticsvidhya.com/blog/2020/06/statistics-analytics-hypothesis-testing-z-test-t-test/ "Statistics for Analytics and Data Science: Hypothesis Testing and Z-Test vs. T-Test"
[6]: https://pythonfordatascienceorg.wordpress.com/paired-samples-t-test-python/ "Python for Data Science - Paired Sample t-test"
[7]: https://statistics.laerd.com/statistical-guides/understanding-histograms.php "Laerd Statistics - Understanding Histograms"
[8]: https://seaborn.pydata.org/tutorial/distributions.html "Seaborn - Visualizing distributions of data"
[9]: https://stats.idre.ucla.edu/other/mult-pkg/faq/general/faq-what-are-the-differences-between-one-tailed-and-two-tailed-tests/ "UCLA - What are the differences between one-tailed and two-tailed tests?"


[\[1\] Wikipedia - Stroop Effect][1]

[\[2\] Interactive Stroop Test][2]

[\[3\] Stroop Test Dataset][3]

[\[4\] The Stroop Effect: Naming a Color but Not the Word][4]

[\[5\] Statistics for Analytics and Data Science: Hypothesis Testing and Z-Test vs. T-Test][5]

[\[6\] Python for Data Science - Paired Sample t-test][6]

[\[7\] Laerd Statistics - Understanding Histograms][7]

[\[8\] Seaborn - Visualizing distributions of data][8]

[\[9\] UCLA - What are the differences between one-tailed and two-tailed tests?][9]
