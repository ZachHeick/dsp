[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> Import modules and generate 1000 random numbers between 0 and 1.
>> ```python
>> import thinkstats2
>> import thinkplot
>> import numpy as np
>> import matplotlib as plt
>>
>> nums = np.random.random(1000)
>> ```
>> Creating and plotting Pmf.
>> ```python
>> nums_pmf = thinkstats2.Pmf(nums, label='Pmf')
>> thinkplot.Pmf(nums_pmf)
>> thinkplot.Config(xlabel='Random Number', ylabel='Pmf')
>> thinkplot.Show()
>> ```
>> ![Pmf Graph](://github.com/ZachHeick/dsp/blob/master/statistics/4_2_pmf.png)
>>
>> Creating and plotting Cdf.
>> ```python
>> nums_cdf = thinkstats2.Cdf(nums, label='Cdf')
>> thinkplot.Cdf(nums_cdf)
>> thinkplot.Config(xlabel='Random Number', ylabel='Cdf')
>> thinkplot.Show()
>> ```
>> ![Cdf Graph](https://github.com/ZachHeick/dsp/blob/master/statistics/4_2_cdf.png)
>>
>> The distribution is uniform because the Cdf graph is linear. This means each number has about the same percentile rank.
