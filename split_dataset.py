import os
import random

path_large = '/Users/gundeepsingh/Dropbox/notebook/sounds/whistles/large'
path_small = '/Users/gundeepsingh/Dropbox/notebook/sounds/whistles/small'
split_ratio = 0.1

for folder in (fl for fl in os.listdir(path_large) if not fl.startswith('.')) :

  # choose random indices to create test data
  files = os.listdir(os.path.join(path_large,folder))
  random_indices = random.sample(range(0,len(files)),int(split_ratio*len(files)))

  # move files from large to small
  for rndm in random_indices:
      old_file_path = os.path.join(path_large, folder, files[rndm])
      new_file_path = os.path.join(path_small, folder, files[rndm])
      os.rename(old_file_path, new_file_path)
