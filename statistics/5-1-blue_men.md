[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> Define `mu` and `sigma` for males and use `scipy.stats` to create the normal distribution.
>> ```python
>> import scipy.stats
>>
>> mu = 178
>> sigma = 7.7
>> norm_dist = scipy.stats.norm(mu, sigma)
>> ```
>> We want to find the percentage of males between 5'10'' and 6'1''. Using the normal distribution, we can find the cdf values for each height and the difference will be our answer.
>> ```python
>> low = norm_dist.cdf(177.8)
>> high = norm_dist.cdf(185.42)
>> print(high-low)
>> ```
>> Our exact answer is 0.34274683731, about 34%.
