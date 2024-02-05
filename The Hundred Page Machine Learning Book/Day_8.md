# Day_8

## Parameter Estimation:
<p align="center">
  <img src="https://i.postimg.cc/1361DPWm/Colorful-Success-Circle-Steps-Diagram-1.png" alt="??" width="200px"><br>
</p><br>

It estimates the parameter of a given function values that best define the distribution (![](https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7DX%7D)).

The Gaussian function _(aka. Normal distribution)_ could be a good example.
> Gaussian function:
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7Df_%7B%5Ctheta%7D%28x%29%20%3D%20%5Cfrac%7B1%7D%7B%5Csigma%20%5Csqrt%7B2%5Cpi%7D%7D%20e%5E%7B-1/2%20%28%5Cfrac%7Bx-%5Cmu%7D%7B%5Csigma%7D%29%5E2%7D%7D" alt="??"><br>
</p>

> where, ![](https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7D%5Ctheta%20%5Coverset%7B%5Cunderset%7B%5Cmathrm%7Bdef%7D%7D%7B%7D%7D%7B%3D%7D%20%5B%5Cmu%2C%5Csigma%5D%7D)

This model/ function has all property of pdf. Therefore can be used as a model of an unknown distribution of ![](https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7DX%7D).

We can update the values of parameters in vector ![](https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7D%5Ctheta%7D) from the data **using Bayes' Rule**. <br>
ie.,
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7DP%28%5Ctheta%20%3D%20%5Chat%7B%5Ctheta%7D%20%7C%20X%20%3D%20x%29%20%5Cleftarrow%20%5Cfrac%7BP%28X%20%3D%20x%20%7C%20%5Ctheta%20%3D%20%5Chat%7B%5Ctheta%7D%29%5Ccdot%20P%28%5Ctheta%20%3D%20%5Chat%7B%5Ctheta%7D%29%7D%7BP%28X%3Dx%29%7D%20%7D" alt="??"><br>
</p>

> PS: The term ![](https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7DP%28X%20%3D%20x%20%7C%20%5Ctheta%20%3D%20%5Chat%7B%5Ctheta%7D%20%29%20%7D) in Bayes' Rule is known as likelihood of a function. 

### Basics of Parameter Estimation:
* Maximum Likelihood Estimation (MLE)
* Maximum Posteriori Estimation (MAP)
* Bayesian Formulation

### Maximum Likelihood Estimaiton (MLE)
Method of estimating the parameters of an assumed probability distribution, given some observed data. <br>

It **attempts to find values that maximize the likelihood function, given the observation**. The resulting estimate hence is called as _maximum likelihood estimation_. 

Assume that we have <u>independent and identical random samples</u> ![](https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7DX%20%3D%20%5C%7Bx_%7B1%7D%2C%20x_%7B2%7D%2C%20%5Cdots%2C%20x_%7Bn%7D%5C%7D%7D) taken from probability distribution having pdf ![](https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7DP%28X%20%7C%20%5Ctheta%29%7D), which depends on unknown parameter ![](https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7D%5Ctheta%7D). 

### Steps:
1. Construct a likelihood function. 
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7DL%28%5Ctheta%20%7C%20x%29%20%3D%20P%20%28x_%7B1%7D%2C%20x_%7B2%7D%2C%20...%20x_%7Bn%7D%20%7C%20%5Ctheta%29%7D" alt="??"><br>
</p>
2. Use the property of iid random sample to break the joint pdf to the product of marginal pdf.
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7DP%28x_%7B1%7D%2C%20x_%7B2%7D%2C%20x_%7B3%7D%2C%20%5Cdots%20%2Cx_%7Bn%7D%20%7C%20%5Ctheta%29%3D%20%5Cprod_%7Bi%3D1%7D%5E%7Bn%7D%20P%28x_%7Bi%7D%20%7C%20%5Ctheta%29%7D" alt="??"><br><br>
  ie., 
  <img src= "https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7DL%28%5Ctheta%20%7C%20x%29%20%3D%20P%28x_%7B1%7D%20%7C%20%5Ctheta%29%20%5Ccdot%20P%28x_%7B1%7D%20%7C%20%5Ctheta%29%20%5Ccdot%20P%28x_%7B1%7D%20%7C%20%5Ctheta%29%5Cdots%20%5Ccdot%20P%28x_%7Bn%7D%20%7C%20%5Ctheta%29%20%7D" alt="??"><br>
</p>
3. (Since multiplication takes time) take a logarithm(usally natural log) to change the product to summation. 

> This does not change the optional estimator since logarithm is a monotonic function. 
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7DLL%28%5Ctheta%20%7C%20x%29%20%3D%20%5Csum_%7Bi%3D1%7D%5E%7Bi%3Dn%7D%20log%20P%28x_%7Bi%7D%3B%20%5Ctheta%29%7D" alt="??"><br><br>
</p>

where ![](https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7DLL%28%5Ctheta%20%7C%20x%29%20%7D) represents the log-likelihood function.

4. Differentiate the log-likelihood function with respect to ![](https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7D%5Ctheta%7D) and set it to "zero".
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7D%5Cfrac%7B%5Cpartial%20LL%20%28%5Ctheta%20%7C%20x%29%20%7D%7B%5Cpartial%20%5Ctheta%7D%20%3D%200%7D" alt="??"><br><br>
</p>

5. Finally, the estimator will only be a function of observed data.
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7D%5Chat%7B%5Ctheta%7D_%7Bml%7D%20%3D%20g%28x_%7B1%7D%2C%20x_%7B2%7D%2C%20%5Cdots%20%2C%20x_%7Bn%7D%29%7D" alt="??"><br><br>
</p>

> The arguement that maximizes the value of **MLE**: ![](https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7D%5Ctheta%5E*%20%3D%20%5Cbegin%7Bmatrix%7D%20arg%20max%20%5C%5C%20%5Ctheta%20%5C%5C%20%5Cend%7Bmatrix%7D%20%5Cprod_%7Bi%3D1%7D%5E%7BN%7D%20%28%5Ctheta%20%3D%20%5Chat%7B%5Ctheta%7D%20%7C%20X%20%3D%20x_%7Bi%7D%29%20%7D)

