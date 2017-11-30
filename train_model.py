import os
import pyAudioAnalysis
from pyAudioAnalysis import audioTrainTest as aT

def train_model():
    global root_folder
    root_folder = '/Users/gundeepsingh/Dropbox/notebook/sounds/recorded/large/'
    folders = (os.path.join(root_folder,f) for f in os.listdir(root_folder)
                  if (os.path.isdir(os.path.join(root_folder,f)) and not f.startswith('.')
                     and not f.startswith('hawker')))
    print('folders = %s'%str(folders))
    aT.featureAndTrain(folders, 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "knn", "mark1", True)

global root_folder
train_model()
