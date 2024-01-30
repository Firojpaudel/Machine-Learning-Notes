## Day_2: 

### How Supervised Learning Works:
Pictorial Version:


![SuperVised Learning Algo](https://i.postimg.cc/3JZnHv5x/Colorful-Success-Circle-Steps-Diagram.png)  

#### Example Case:
**Problem**: Spam Detection.<br>
  *Let's assume we have gathered emails (say 10,000), each with label: **"Spam" and "Not_Spam"***. Now, we have to convert each message into feature vector. Converting messages into feature vector solely depends on Analyst experience.<br>
  Now we have machine-readable input data, but the output's still human-readable. Some learnig algos require transforming labels into numbers. For example: in above case, labels could be <u>**0 : for Not_Spam**</u> and <u>**1: for Spam mails**</u>.<br>
  Now at this point we have dataset and algo, so we are ready to apply algo to the dataset to get model. 


  > **Note:** On Further reading, author uses SVM(Support Vector Machine) algorithm to represent Supervised Learning where <u>+1 : Spam and -1: Not_Spam</u>

### Supervised Vector Machine Algo (SVM):
In SVM, every feature vector is a point in <u>_high dimensional space_</u>.

- The Algo puts all feature vectors in the dimensional plot and draws an <u>_imaginary hyperplane_</u> that seperates examples with +ve and -ve labels. 
 - In ML, this boundary which separates different classes is called **decision boundary**. 

<p style="text-align: center; "><b>Equation of hyperplane:</b></p>
<p align="center">
  <img src="https://latex.codecogs.com/svg.image?{\color{Gray}wx-b=0}" alt="wx-b=0">
</p>

where, `w` -> real-valued vector whose dimensionality is same as input feature vector `x`

Then, the predicted label for some input feature vector `x` is given as:
 <p align="center">
  <img src="https://latex.codecogs.com/svg.image?{\color{Gray}y=sign(wx-b)}" alt="sign(wx-b)=y">
</p>

> sign: mathematical operator for deciding the values +1/ -1 

#### Goal: 
To leverage the dataset and find optial values `w*` and `b*` for parameters `w` and `b`. Once the algo identifies them, model `f(x)` is defined as: 
 <p align="center">
  <img src="https://latex.codecogs.com/svg.image?{\color{Gray}f(x)=sign(w^*x-b^*)}" alt="sign(w*x-b*)=f(x)">
</p>


So, back to previous example: In order to detect a mail as spam or not, following steps take place:
- Converting message to feature vector `x`. 
- Multiply it with `w*` and subtract `b*` from it. 
  - Output: +1 =`spam`; -1 =`non_spam`

> **How does the machine find `w*` and `b*`? <br>**
_Machine solves optimization problem._

> **_Note_:**<br>
Width of angled hyperplane >>>  Width of linear hyperplane. So, angled hyperplane is used.<br>
This concept is also called as **Maximal Margin Hyperplane** and provides the maximal accurate prediction. 

