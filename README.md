# Food-Ingredients-Recognition



## Table of Contents


   1. Problem Statement
   2. Future Improvements
   3. Repository Navigation
   4. Technologies and Libraries Used
   5. Modelin
   6. Evaluation
   7. References
   



### Problem Statement

There are several cooking apps or websites available today, that are used to find recipes based on some keyword, like name of the food ingredient or type of cuisine, etc. These apps are mindful of the needs and interests of their users, but they fail at identifying their user's constraints, i.e., limited number of food ingredients. In such cases, users find themselves shopping for ingredients or they decide to substitute the missing ingredient with something else. To help users avoid such adjustments, image recognition can be employed to identify food ingredients that are already available at their disposal and recommend them recipes based on those ingredients.


Food recognition is an emerging topic in the field of computer vision. The recent interest of the research community in this area is justified by the rise in popularity of food diary applications.
As a stakeholder, I want to build a integrated system, where it can recognises ingredients and therefore has the capacity to recomend recipes based on the recognised food.

I tackle the problem of food ingredients recognition as a multi-class learning problem. I propose a method for adapting a highly performing state of the art CNN in order to act as a multi-class predictor for learning food ingredients in terms of their nature.
I prove that my model is able to give, given a picture, predict its group of ingredients..

-----Furthermore, I prove that a model trained with a high variability of recipes and ingredients is able to generalise better on new data.--------

As a  future work I want to create a recomend system able to recommend recipes based on the recognised ingredients and for that I will need an accurate image recognition system..


![] (Data/screen.png)

### Solution

Currently the system is a web application that performs image recognition on the uploaded images and recommends recipes juthat contains the recognized ingredients. We built a convolutional neural network model for image recognition to identify five categories of food ingredients and achieved, 62.9% accuracy rate. The recommendation system uses the labels of the identified images to display a list of recipes that contains most of the identified ingredients.

As such, the plan is to construct deep learning model (convolutional neural network) to classify food ingredients images by three groups 



###  Repository Navigation

   * Notebooks
   
     * Data Understanding / Modeling.ipynb

     * Webscrapping.ipynb

   * Data
     
     * Data_CSV

     * Ingredients
       
       * Fruits & Vegetables
       * Grains
       * Meat

     * Split_Sets
       
       * train
       * test
       * validation

   
   * Presentation: Folder with the project's presentation
   
     * presentation.pdf
   
   * README.md
   

### Technologies and Libraries Used
-   Python
-   Pandas
-   Numpy
-   Matplotlib
-   Scikit-learn
-   Skimage
-   Cv2
-   Os
-   Keras
-   Tensorflow
-   Urllib
-   Pil
-   Requests
-   BeautifulSoup


### Modelling

In order to carry out the modelling, I split the final dataset into 3 subsets. Train (3587 images), Validation(471 images) and Test (544 images).


### Evaluation

Following the additional economic data for Portugal and Eurozone, our model performance increased to 90.5%. Using hyperparameter tuning with Sci-Kit learn's GridSearchCV function, we were able to increase the performance to 92.8%. As it stands, our best performing model is the Logisitic Regression model using GridSearchCV.

### References

-  SerpWow: [here](https://serpwow.com/)
-  Google Images: [here](https://www.google.com/imghp?hl=en)
-  Multi-Class Classification Tutorial with the Keras Deep Learning Library: [here](https://machinelearningmastery.com/multi-class-classification-tutorial-keras-deep-learning-library/)
-  Food Ingredients Recognition Through Multi-label Learning: [here](https://link.springer.com/chapter/10.1007/978-3-319-70742-6_37)
-  Mobile Food Recognition with an Extreme Deep Tree:[here](https://dl.acm.org/doi/10.1145/2967413.2967428)