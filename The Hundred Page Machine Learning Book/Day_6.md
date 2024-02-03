# Day_6

## Notations Continued:

7. **Max and argMax:**<br>
For set of values ![](https://latex.codecogs.com/svg.image?{\color{Gray}A=\{a_{1},a_{2},\dots,a_{n}\}}) ,
> ![](https://latex.codecogs.com/svg.image?{\color{Gray}Max_{a\epsilon%20A}f(a)}) -> returns highest value of `f(a)` for all elements of `set A`.

> ![](https://latex.codecogs.com/svg.image?{\color{Gray}argMax_{a\epsilon%20A}f(a)}) -> returns element of `set A` that maximizes `f(a)`.

`Similar for Min and argMin`

8. **Assignment Operator:**<br>
Explanation through example:
<p align="center">
  <img src="https://latex.codecogs.com/svg.image?{\color{Gray}a\leftarrow%20f(x)}" alt="??"><br>
</p>

> Here, `a` gets the value which is the result of `f(x)`

<p align="center">
  <img src="https://latex.codecogs.com/svg.image?{\color{Gray}a\leftarrow\[a_{1},a_{2}\]}" alt="??"><br>
</p>

> Similarly, the vector variable `a` gets 2D vector value ![](https://latex.codecogs.com/svg.image?{\color{Gray}[a_{1},a_{2}\]}).

9. **Derivative and Gradient:**<br>
A derivative ![](https://latex.codecogs.com/svg.image?{\color{Gray}f^{%27}})  of a function ![](https://latex.codecogs.com/svg.image?{\color{Gray}f}) is a function or value that <u>describes how fast the function grows or decreases.</u><br>
Gradient is the generalization of derivative of functions that take several inputs _(or one input in form of vector or some complex structures)_.<br>
> ie., for function defined with vectors ![](https://latex.codecogs.com/svg.image?{\color{Gray}f\([x^{(1)},x^{(2)}])})  is ![](https://latex.codecogs.com/svg.image?{\color{Gray}\[\frac{\partial%20f}{\partial%20x^{(1)}},\frac{\partial%20f}{\partial%20x^{(2)}}]}).

10. **Random Variable:**<br>
* Written usually as an italic capital letter.<br>
ie., _X_ : as an example.

* Random Variable '_X_ ' is a variable whose possible values are numerical outcome of random phenomenon.

#### Types of Random Variable:
1. Discrete Random Variable
2. Continuous Random Variable

### Discrete Random Variable
Takes **<u>countable</u>** number of distinct values.<br>
Uses PMF (Probability Mass Function).

#### PMF:
List of probabilities i.e, ![](https://latex.codecogs.com/svg.image?{\color{Gray}P(X=a),P(X=b)}) and so on. 

> The probability of `each pmf > 0` and `summation_of_pmfs = 1`

#### Expectation of a Discrete Random Variable:
**If:**<br> _X_ -> discrete random variable,<br>
then _X_ can be written as: ![](https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7D%5C%7Bx_%7Bi%7D%5C%7D_%7Bi%3D1%7D%5E%7Bk%7D%7D)<br>
So, the expectation of _X_ represented by: ![](https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7D%5Cmathbb%7BE%7D%5BX%5D%7D) is defined as:
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7D%5Cmathbb%7BE%7D%5BX%5D%20%5Coverset%7B%5Cunderset%7B%5Cmathrm%7Bdef%7D%7D%7B%7D%7D%7B%3D%7D%5Csum_%7Bi%3D1%7D%5E%7Bk%7D%5Bx_%7Bi%7D%5Ccdot%20P%28X%3D%20x_%7Bi%7D%29%5D%7D" alt="??"><br>
</p>

> Note: Expectation is also termed as mean.<br> ie., ![](https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7D%5Cmathbb%7BE%7D%5BX%5D%3D%20%5Cmu%20%7D)

### Continuous Random Variable
Has **<u>♾️ number</u>** of possible values.<br>
Since the values are infinite, lists of probabilities can't be used. So, Probability density function (Pdf) is used.

#### Probability Density Function (Pdf):
Function with `non-negative co-domain` and `area under curve = 1`

#### Expectation of Continuous Random Variable:
Similar to that of discrete:<br> 

>**Changes:** summation changes to integration and Pmf to Pdf.
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7D%5Cmathbb%7BE%7D%5BX%5D%3D%20%5Cmu%20%3D%20%5Cint_%7B-%5Cinfty%20%7D%5E%7B%20&plus;%5Cinfty%7D%20x%20%5Ccdot%20f%28x%29dx%7D" alt="??"><br>
</p>

> where, ![](https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7Df%28x%29dx%7D) is Pdf.
<p align="center">
  <img src="https://i.postimg.cc/brY2SS49/Colorful-Success-Circle-Steps-Diagram.png" alt="??" width= "450px"><br>
</p>

#### Standard Deviation of Random Variables:
> Denoted by ![](https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7D%5Csigma%7D).
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7D%5Csigma%20%5Coverset%7B%5Cunderset%7B%5Cmathrm%7Bdef%7D%7D%7B%7D%7D%7B%3D%7D%20%5Csqrt%7B%5Cmathbb%7BE%7D%5B%28X-%5Cmu%29%5E2%5D%7D%7D" alt="??"><br>
</p>

> where, ![](https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7D%5Cmathbb%7BE%7D%5BX%5D%3D%20%5Cmu%20%7D) 

#### Variance:
Square of standard deviation. Denoted by ![](https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7D%20%5Csigma%5E2%7D).

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7D%20%5Csigma%5E2%20%3D%20Var%28X%29%20%3D%20%5Cmathbb%7BE%7D%28X%5E2%29%20-%20%5Cmu%20%5E2%7D" alt="??"><br>
</p>

_For Discrete:_
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7D%20%5Csigma%5E2%20%3D%20%5Csum%20P%5Ccdot%20x%5E2%20-%20%5Cmu%20%5E2%7D" alt="??"><br>
</p>

_For Continuous:_
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BGray%7D%20%5Csigma%5E2%20%3D%20%5Cint_%7B-%5Cinfty%7D%5E%7B&plus;%5Cinfty%7D%20x%5E2%5Ccdot%20f%28x%29%20dx-%20%5Cmu%5E2%7D" alt="??"><br>
</p>







