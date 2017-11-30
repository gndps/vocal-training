from pyAudioAnalysis import audioTrainTest as aT
import sys

def classify(file_path):
  aT.fileClassification(file_path, "mark1","knn")

classify(sys.argv[0])
