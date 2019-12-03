import numpy as np
import matplotlib.pyplot as plt

from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels

cm = np.load('cm.npy')
print(cm)
plt.imshow(cm, cmap='binary')
plt.savefig("test.png")

