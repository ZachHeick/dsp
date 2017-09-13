[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> We need to get the DataFrames for first babies and the others. To do this we can use `first.MakeFrames()` from the ThinkStats repository.
>> ```python
>> import first
>> import thinkstats2
>>
>> live, firsts, others = first.MakeFrames()
>> ```
>> Now that we have our DataFrames, we can calculate the `totalwgt_lb` mean for first babies and others.
>> ```python
>> firsts_mean = firsts.totalwgt_lb.mean()
>> others_mean = others.totalwgt_lb.mean()
>> print(firsts_mean, others_mean)
>> ```
>> On average, first babies are lighter than the others. First babies have a mean weight of 7.2011 lbs and others have a mean weight of 7.3258 lbs. Another way to measure the difference in means is to calculate Cohen's *d*. This variable is calculated by taking the difference in means of each group over the pooled standard deviation. The `thinkstats2` module provides a function to do this.
>> ```python
>> d = thinkstats2.CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
>> print(d)
>> ```
>> We get a *d* value of -0.0887, slightly larger than the difference for pregnancy length, 0.0288, which was calculated in a previos textbook example. 
