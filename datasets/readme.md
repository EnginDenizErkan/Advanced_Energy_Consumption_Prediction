# This folder is dedicated towards saving the generated datasets for this project.

Installation

1. # Give path of block_0 and  weather_hourly_darksky CSV files. (Second code block)

example;

    energy_data = pd.read_csv("C:\\Users\\Furkan\\Desktop\\DS502_Project\\block_0.csv")

    weather_data = pd.read_csv("C:\\Users\\Furkan\\Desktop\\DS502_Project\\weather_hourly_darksky.csv")


2. # Give path to export train, test and validation datasets as CSV (Last code block)

example;

    X_train_sorted.to_excel('C:\\Users\\Furkan\\Desktop\\X_train.xlsx', index=True)

    X_val_sorted.to_excel('C:\\Users\\Furkan\\Desktop\\X_val.xlsx', index=True)

    X_test_sorted.to_excel('C:\\Users\\Furkan\\Desktop\\X_test.xlsx', index=True)



After reading the CSV files block_0 and weather_hourly_darksky, this code performs the necessary data merging operations. The data is then split into 70% training, 20% testing, and 10% validation sets, and the outputs are saved to the specified file path. The random state is set to 123 in the split part because it is desired to keep the data consistent across different runs. The shuffle parameter is set to true to ensure a randomized arrangement of the training, testing, and validation sets.
