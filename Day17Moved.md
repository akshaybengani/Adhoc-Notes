# Day 17
Today we have studied about git and git branching and then installed jupyter in Ubuntu and now learning supervised learning
## Supervised Machine Learning
*   
*   We need a DataSet for training
*   Then we give this data to system for training for learning purpose
*   Then the training model is ready for QnA.
*   Then we give a new question related to the training model.
*   Example
    *   When we see a dog for the first time, someone introduce us that this object is a dog. Similarly when we see another breed of a dog or an animal we can identify that which animal it is.
*   The actual object is called as ```label```
*   The attributes | Features | Characterstics of an object are ```features``` for computer.
*   So we have to give both label and its features to the system for training purpose.
*   Model Data
    *   Apple
        *   Texture : Smooth
        *   Weight  : 100-120 Grams
    *   Orange
        *   Texture : Bumpy
        *   Weight  : 120-140 Grams
```py
# Here Smoooth is for apple and Bumpy is for Orange
features=[[100,"Smooth"],[120,"Smooth"],[130,"Bumpy"],[150,"Bumpy"]]

label = ['apple','apple','orange','orange']
```
*   Now we need an algorithm for training purpose.
*   Supervised Machine Learning
    *   Classifier This means when we need to distinguish between features and attributes or basically classifying data<br>
    Data Classifiers techniques for Supervised Learning
        *   KNN
        *   SVM
        *   Decision Tree
        *   Naive Bagos
        *   Random Foresh
        *   Lion
        *   Me
    *   Regression will discuss later for this.
*   In python there is a liberary called scikit which contains all the above classifiers. It is a framework containing all the classifiers written in python.
*   Since by default we dont have ```scikit-learn``` installed so we have to install it with pip3
```
pip3 install scikit-learn
```
