<!--
title: Machine Learning & Data Science (XDays)
author: Firoj Paudel
Last_Updated: 2024-01-29
-->

# ML_Notes:

## Day_1: 
Starting to learn **The Hundred Page Machine Learning Book** _By Andry Burkov_ 

> Summary note of what I read today: 

### **What is ML?**
Process of solving practical problem by: 
  - Gathering dataset
  - And algorithmically bulding a statistical model based in dataset.

### Types of Learning: 
   1. Supervised Learning
   2. Unsupervised learning
   3. Semi- supervised Learning 
   4. Reinforcement Learning 

   ### Supervised Learning:
   - In Supervised Learning, _dataset is collection of labeled examples {x,y}._
     - where, x -> feature vector and y -> label

     #### Feature Vector: 
     A vector in which each dimension j = 1,2, ...,D contains the element somehow.
     > Meaning: If x of one dimension say "d" has data related to a particular category then for iterations N, the datas are related to same category.  
   - y -> label :: can be element belonging to finite set _**classes, real number, or complex structures like matrices, vector, tree or graph.**_

   ##### Goal: 
   To produce a **model** that takes a featured vector x as a input and outputs info that allows deducing the label for this feature vector. 
  

  > **Note**: In Supervised Learning, algo is trained on the dataset that is already "labelled" with correct answers. 
              _Algo learns from these labelled examples_ to generalize patterns and relationships and make _predictions of unseen data._

  ### Unsupervised Learning: 
   - Here, dataset is collection of unbiased examples {x}. Where, x -> feature vector

   ##### Goal:
   To create a model that takes feature vector as input and **transform** it **into the value** that can be used to solve the problem. 

  > **Note**: Unlike supervised learning, there are _no correct answers or labelled outputs_ to guide the learning proccess
  Instead, the _algo explores the data to discover similarities, differences, outliers_ and so on. It gives overall idea about the data 

  **Examples** of unsupervised learning: **Clustering** and **Dimensionality Reduction**

  > **Clustering**: _Grouping similar datsets together bases on their characteristics._

  > **Dimensionality Reduction**: Reducing the number of features/ variables in the dataset. 
  **Reason**-> High Dimensional data are **computationally expensive** and may suffer from _'noise'_.

  ### Semi- Supervised Learning: 
  - Contains _**both labelled and unlabelled**_ examples. Usually quantity of _unlabelled examples is higher_. 

  ##### Goal:
  Similar to that of Supervised learning. 

  **Except,** We add more unlabelled examples to gain the "goal". 
  And this might seem counter-intuitive and doing this might seem to add more uncertainity

  **But**: adding unlabelled examples also mean you add _more info about the problem_ and _Algo could leverage the additional info_. 

  ### Reinforcement Learning:
  > Note: Below, "agent" refers to the algo itself (_not person_).

  - Type of Machine Learning where an "agent" learns to make decisions interacting with the environment. The "agent" receives feedback in form of _rewards or penalties_ based on actions. 

  > Similar to learning by doing.

  ##### Goal:
  To learn **"Policy"** that maximizes cumulative rewards over time.

  > **Policy**: a function that _takes feature vector as input_ and _outputs an optimal action_ to execute that state.
  >> **So what makes the action optimal?** If the action maximizes the expected average reward. 




