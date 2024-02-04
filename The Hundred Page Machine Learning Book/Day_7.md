# Day_7

## Estimation:
To estimate the value of population parameter, we can use info from the sample in the form of <u>Estimator</u>.

### Estimator:
Rule for calculating an estimate of a given quantity based on observed data.

#### Types of Estimators:
* Point Estimator 
* Interval Estimator

  * **Point Estimator:** Based on sample data, _single number_ is calculated to estimate the population parameter.

  * **Interval Estimator:** Based on sample data, _two numbers_ are calculated to _**form an interval**_ within which the population parameter is expected to lie.

> <u>Inorder to select the best estimator</u>, we need to know how the estimator behaves in repeated <u>sample distribution.</u><br> ie., Sampling distribution provides info that can be used to select the best estimator.

### Unbiased Estimator:

In scenarios where the exact probability distribution ![](https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7D%28f_x%29%7D) of a random variable ![](https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7DX%7D) is unknown, the author introduces the concept of unbiased estimators. Utilizing a sample ![](https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7D%28S_x%29%7D) drawn from the mysterious distribution, represented as ![](https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7D%5C%7Bx_i%5C%7D_%7Bi%3D1%7D%5EN%7D), these estimators are employed to approximate key statistics, such as the expectation. An estimator ![](https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7D%5Ctheta%20%5Chat%20%28S_x%29%7D) is considered unbiased if, on average across all conceivable samples from X, it accurately reflects the true parameter ![](https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7D%5Ctheta%7D). Essentially, this implies that repeated calculations of the unbiased estimator using different samples would, on average, converge to the genuine value of the parameter.

> _Want to learn more on **Unbiasedness and Criterions of Good Estimators?**_ [_Click Here_](./Unbiasedness%20and%20Criterions%20of%20Good%20Estimator.pdf)


## Baye's Rule:
Fundamental concept in probability theory that provides a way to _update the probability of hypothesis_ based on _new evidence_.
> **Conditional Probabilty** ![](https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7DP%28X%3Dx%20%7C%20Y%3Dy%29%7D) is the probabilty of random variable ![](https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7DX%7D) to have a specific value ![](https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7Dx%7D) given that another random variable ![](https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7DY%7D) has specific value of ![](https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7Dy%7D).

_**Formula:**_
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7DP%28X%3Dx%7CY%3Dy%29%20%3D%20%5Cfrac%7BP%28Y%3Dy%7CX%3Dx%29%5Ccdot%20P%28X%3Dx%29%7D%7BP%28Y%3Dy%29%7D%7D" alt="??"><br>
</p>

> Bayes' Theorem is most commonly used in machine learning applications such as _spam detection, medical diagnosis, document classification, and personalized recommendations_. It finds practical utility in tasks involving probability assessment, updating beliefs based on new evidence, and making predictions in the presence of uncertainty.