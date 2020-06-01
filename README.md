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

![enter image description here](https://drive.google.com/open?id=1c6dMZ8iRXau2ZD1lVV2u3TdZljqrev04)



### Solution

Currently the system is a web application that performs image recognition on the uploaded images and recommends recipes that contains the recognized ingredients. We built a convolutional neural network model for image recognition to identify five categories of food ingredients and achieved, 62.9% accuracy rate. The recommendation system uses the labels of the identified images to display a list of recipes that contains most of the identified ingredients.



###  Repository  Navigation

   * Notebooks
   
     * Data Understanding / Modeling.ipynb
     * Webscrapping.ipynb

   * Data: All the CSV files can be found in the Data folder. 
     
     * apple.csv
     * asparagus.csv
     * aubergine.csv 
     * bacon.csv
     * beetroot.csv 
     * black_beans.csv
     * black_eyed_peas.csv
     * broccoli.csv
     * brussel_sprouts.csv
     * butternut_squash.csv
     * cabbage.csv
     * cannelloni.csv
     * carrot.csv
     * cauliflower.csv
     * chicken_breast.csv
     * chicken_whole.csv
     * chickpeas.csv
     * cucumber.csv
     * eggs_brown.csv
     * eggs_white.csv
     * fresh_pork_chop.csv
     * fresh_raw_beef.csv
     * green_pepper.csv
     * ground_beef.csv
     * lamb.csv
     * lasagne.csv
     * lentils.csv
     * lettuce.csv
     * mackerel.csv
     * mushrooms.csv
     * mussels.csv
     * onions.csv
     * oyster.csv
     * penne.csv
     * pork_belly.csv
     * pork_ribs.csv
     * ravioli.csv
     * red_beans.csv
     * red_pepper.csv
     * salmon.csv
     * sardines.csv
     * shrimps.csv
     * soybeans.csv
     * spaghetti.csv
     * sweet_potato.csv
     * tomato.csv
     * trout.csv
     * tuna.csv
     * white_potato.csv
     * white_rice.csv
     * zucchini.csv
   
   *  Split_Sets: Data set splitted in train, validation and test sets.
   
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