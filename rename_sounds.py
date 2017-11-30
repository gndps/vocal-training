import os
import pyAudioAnalysis.audioVisualization as av

def rename_files():
    for f in os.listdir(folder):
      if f.startswith('.'):
        continue
      for file in os.listdir(os.path.join(folder,f)):
        if file.endswith('.wav'):
            old_file_name = os.path.join(folder,f,file)
            new_file_name = os.path.join(folder,f,(f + ' --- ' + file))
            print('renaming file - %s'%old_file_name)
            os.rename(old_file_name, new_file_name)

def bahar_kadho():
    for f in os.listdir(folder):
      if f.startswith('.'):
        continue
      for file in os.listdir(os.path.join(folder,f)):
        if file.endswith('.wav'):
            old_file_name = os.path.join(folder,f,file)
            new_file_name = os.path.join(folder,file)
            print('bahar kadhing - %s'%old_file_name)
            os.rename(old_file_name, new_file_name)

def visualize_audio(folder, dimReductionMethod, priorKnowledge = "none"):
    av.visualizeFeaturesFolder(folder, dimReductionMethod, priorKnowledge)


folder = '/Users/gundeepsingh/Dropbox/notebook/sounds/visualize'
print('Visualizing the audio...')
# visualize_audio(folder, 'pca')
visualize_audio(folder, 'lda')
# rename_files()
# bahar_kadho()
