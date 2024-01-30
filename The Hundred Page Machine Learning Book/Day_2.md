## Day_2: 

### How Supervised Learning Works:
FlowChart Version:
> Use darkmode for viewing comments inside flowchart.

![SuperVised Learning Algo](https://i.postimg.cc/KjGzyFT6/Supervised-Learning-drawio-1.png)  

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

<p style="text-align: center;">Equation of hyperplane:</p>
<p align="center">
  <img src="https://latex.codecogs.com/svg.image?&space;wx-b=0{\color{DarkGreen}}" alt="wx-b=0">
</p>

