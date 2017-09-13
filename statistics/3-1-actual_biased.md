[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> We need to get the clean DataFrame of the NSFG data. The `nsfg` module from the ThinkStats repository provides us with a function.
>> ```python
>> import first
>> import nsfg
>> import thinkplot
>> import thinkstats2
>>
>> r = nsfg.ReadFemResp()
>> ```
>> To get the actual distribution for number of children under 18 in a household, we can call the `Pmf` function provided using the `numkdhh` variable.
>> ```python
>> actual_pmf = thinkstats2.Pmf(r.numkdhh, label='numkdhh')
>> ```
>> The baised distribution can be easily calculated. For each size of children in each household, the probability is multiplied by the number of children who would observe this sized household.
>> ```python
>> def bias_pmf(pmf, label):
>>     new_pmf = pmf.Copy(label=label)
>>
>>     for x, p in pmf.Items():
>>         new_pmf.Mult(x, x)
>>
>>     new_pmf.Normalize()
>>     return new_pmf
>>
>> biased_pmf = bias_pmf(actual_pmf, label='biased')
>> ```
>> Plotting both pmf graphs.
>> ```python
>> thinkplot.PrePlot(2)
>> thinkplot.Pmfs([actual_pmf, biased_pmf])
>> thinkplot.Config(xlabel='Number of children', ylabel='Pmf')
>> thinkplot.Show()
>> ```
>> ![graph](https://github.com/ZachHeick/dsp/blob/master/statistics/3_1_graph.png)
>> Calculating means.
>> ```python
>> pmf_mean = actual_pmf.Mean()
>> biased_pmf_mean = biased_pmf.Mean()
>> print(pmf_mean, biased_pmf_mean)
>> ```
>> The actual distribution mean is 
