# Day_4:

## Notations and Definitions:

### Back to basics of Data Structures:

1. **Scalars:**<br> They are simple numerical values _(magnitude)_. Eg. 15, -3.124 etc.

> Variables that take scalars are denoted by **<u>_italic letters_</u>** such as _x_ or _a_

2. **Vectors:**<br> 
* Order list of scalar vectors aka. attributes. <br>
* Can be visualized as an arrow that points to _some direction or multidimensinal space_. 

> Denoted by <u>**bold letters**</u> such as **x** or **w**. 

##### Note: 
Attribute of a vector `x` can be denoted as:
<p align="center">
  <img src="https://latex.codecogs.com/svg.image?{\color{Gray}x^{(j)}}" alt="x^(j)">
</p>

> where j -> dimension of vector

>> **Note:** <br>This notation should not be confused with power. ie., 
for a power 'n' to the indexed attribute ![](https://latex.codecogs.com/svg.image?{\color{Gray}x^{(j)}}), we can represent it as: 
![](https://latex.codecogs.com/svg.image?{\color{Gray}(x^{(j)})^n}) and not ![](https://latex.codecogs.com/svg.image?{\color{Gray}x^{(nj)}}).


A variable can have two or more indices like ![](https://latex.codecogs.com/svg.image?{\color{Gray}x_{i}^{(j)}}) or ![](https://latex.codecogs.com/svg.image?{\color{Gray}x_{i,j}^{(k)}}).

3. **Matrix:**<br> It is an rectangular array of numbers arranged in rows and columns. 

> Denoted by bold capital letters like **W** and **A**.

4. **Set:**<br> Unordered collection of unique elements.

5. **Capital Sigma Notation:**<br> The summation over collection ![](https://latex.codecogs.com/svg.image?{\color{Gray}X=\{x_{1},x_{2},x_{3},\dots,x_{n}\}}) or attributes of a vector ![](https://latex.codecogs.com/svg.image?{\color{Gray}\textbf{x}=\[x^{(1)},x^{(2)},x^{(3)},\dots,x^{(m-1)},x^{(m)}\]}) is defined as:

<p align="center">
  <img src="https://latex.codecogs.com/svg.image?{\color{Gray}\sum_{i=1}^{n}xi\overset{\underset{\mathrm{def}}{}}{=}x_{1}+x_{2}+x_{3}+x_{4}+\dots+x_{n}}" alt="??"><br>
  OR<br>
  <img src="https://latex.codecogs.com/svg.image?{\color{Gray}\sum_{j=1}^{m}x^{(j)}\overset{\underset{\mathrm{def}}{}}{=}x^{(1)}+x^{(2)}+x^{(3)}+x^{(4)}+\dots+x^{(m)}}" alt="??">
</p>

> ![](https://latex.codecogs.com/svg.image?{\color{Gray}\overset{\underset{\mathrm{def}}{}}{=}}) refers to **"is defined as"**
