import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import tensorflow as tf
from tensorflow import keras
from keras import models
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import seaborn as sn


def fodase(r):
    res = r*201
    return res