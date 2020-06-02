# Food-Ingredients-Recognition
   


### Problem Statement

Food recognition is an emerging topic in the field of computer vision and the interest in this area is justified by the rise in popularity of food diary applications.
As a stakeholder, I want to build a integrated system, which has the capability to recognise ingredients and recomend recipes based on the recognised items, for this reason, I want to build a very accurate image recognition algorithm.
Therefore, I tackle the problem of food ingredients recognition as a multi-class learning problem. I propose a method for adapting a highly performing state of the art CNN in order to act as a multi-class predictor for learning food ingredients in terms of their nature.
I plan to create a model that is able to give, given a picture, a prediction of its group of ingredients..

The models were trained and validated using a set of approximately 5,530 images of 63 food ingredients primarily obtained from a combination of sources, divided by 3 main groups Meat, Grains and Fruits/Vegetables.
These three groups represent the main part of the food pyramid and are essential for the most part of the recipes.

In future, the baseline model will be expanded upon in order to achieve a greater level of accuracy and the classification model will be focus on classifying each ingredient on its own representation instead of by group.



![](./Data/screen.png)



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
   



### Modelling

In order to carry out the modelling, I split the final dataset into 3 subsets. Train (3587 images), Validation(471 images) and Test (544 images).
Baseline model consists of four convolution blocks with a max pool layer in each of them. There's a fully connected layer with 8 units on top of it that is activated by a relu activation function and three units activated by a softmax activation function.
For the second model, I take a new approach, because the baseline model shows a good performing, I want to see if it is possible with more agumentation arguments get even better results.
For the third model and I based my approach on the previous models results. This time, the model won't have augmentation, except the rescale, and use more epochs since the first model showed an increased performance over the time. Therefore, I want to see if it is possible to extrapolate the baseline model's accuracy with a bigger range of epochs.


### Evaluation

After analising the three models, the model that shows better performance is the baseline model, more stable, high accuracy and low overfitting.
To evaluate the winning model, I used Average precision because gives the average precision at all such possible thresholds and Precision-Recall metric. In this project, is an useful measure of success of prediction because the classes are imbalanced and I am not aiming any specific decision threshold.
Wiht an average precison of 0.65 and presicion-recall of class 0 = 0.83 / class 1 = 1 / class 2 = 0.25, I considered the created model good enough  to be integrated in a future recomendation system.

### Contact Info

For any queries or additional information, please email napd.65@gmail.com


### References

-  SerpWow: [here](https://serpwow.com/)
-  Google Images: [here](https://www.google.com/imghp?hl=en)
-  Multi-Class Classification Tutorial with the Keras Deep Learning Library: [here](https://machinelearningmastery.com/multi-class-classification-tutorial-keras-deep-learning-library/)
-  Food Ingredients Recognition Through Multi-label Learning: [here](https://link.springer.com/chapter/10.1007/978-3-319-70742-6_37)
-  Mobile Food Recognition with an Extreme Deep Tree:[here](https://dl.acm.org/doi/10.1145/2967413.2967428)


### Image Disclaimer

All pictures copyright to their respective owner(s). I do not claim ownership of any of the pictures displayed on this project unless stated otherwise. I do not knowingly intend or attempt to offend or violate any copyright or intellectual property rights of any entity. Some images used on this project are taken from the web and believed to be in the public domain.