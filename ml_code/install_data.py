import os
import kagglehub

# Install dependencies as needed
# pip install kagglehub[pandas-datasets]

# Authenticate with Kaggle API if necessary (make sure you have your Kaggle API key)
# kagglehub.set_credentials("username", "api_key")

# Define the directory where you want to save the datasets
dataset_dir = "../dataset/"
os.makedirs(dataset_dir, exist_ok=True)

# Download the datasets
dataset1 = kagglehub.dataset_download("jimohyusuf/blood-pressures") 
dataset2 = kagglehub.dataset_download("pavanbodanki/blood-press") # https://www.kaggle.com/datasets/pavanbodanki/blood-press/code
 
# Move the datasets to the specified directory
os.rename(dataset1, os.path.join(dataset_dir, os.path.basename(dataset1)))
os.rename(dataset2, os.path.join(dataset_dir, os.path.basename(dataset2)))