import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Data 1 - Student's Performance (Gender)
data = pd.read_csv("C:\\Users\\User\\Desktop\\Coding\\Student_Performance_on_an_Entrance_Examination.csv.csv")
gender = np.array(data['Gender'])

gender, c_count = np.unique(gender, return_counts=True)
plt.bar(gender, c_count, color=('violet', 'blue'))
plt.title("Student's Gender")
plt.show()

#Data 2 - Caste
caste = np.array(data['Caste'])

caste, c_count = np.unique(caste, return_counts=True)
plt.barh(caste, c_count, color=('gray', 'orange', 'cyan', 'red'))
plt.title("Different Caste Type")
plt.show()

#Data 3 - coaching
coaching = np.array(data['coaching'])

coaching, c_count = np.unique(coaching, return_counts=True)
plt.bar(coaching, c_count, color=('lime', 'gray', 'green'))
plt.title("Coaching Type")
plt.show()

#Data 4 - Class_ten_education
class_ten_education = np.array(data['Class_ten_education'])

class_ten_education, c_count = np.unique(class_ten_education, return_counts=True)
plt.barh(class_ten_education, c_count, color=('blue', 'gray', 'brown'))
plt.title("Class Ten Education")
plt.show()

#Data 5 - twelve_education
twelve_education = np.array(data['twelve_education'])

twelve_education, c_count = np.unique(twelve_education, return_counts=True)
plt.bar(twelve_education, c_count, color=('red', 'cyan', 'gray'))
plt.title("Twelve Education")
plt.show()

#Data 6 - medium
medium = np.array(data['medium'])

medium, c_count = np.unique(medium, return_counts=True)
plt.barh(medium, c_count, color=('orange', 'red', 'gray'))
plt.title("Medium Instructions on Class XII")
plt.show()

#Data 7 - Class_X_Percentage
class_x_p = np.array(data['Class_X_Percentage'])

class_x_p, c_count = np.unique(class_x_p, return_counts=True)
plt.bar(class_x_p, c_count, color=('brown', 'yellow', 'green', 'lime'))
plt.title("Class X Percentage")
plt.show()

#Data 8 - Class_XII_Percentage
class_xii_p = np.array(data['Class_XII_Percentage'])

class_xii_p, c_count = np.unique(class_xii_p, return_counts=True)
plt.bar(class_xii_p, c_count, color=('brown', 'yellow', 'green', 'lime'))
plt.title("Class XII Percentage")
plt.show()

#Data 9 - Father_occupation
father = np.array(data['Father_occupation'])

father, c_count = np.unique(father, return_counts=True)
plt.barh(father, c_count)
plt.title("Father's occupation")
plt.show()

#Data 10 - Mother_occupation
mother = np.array(data['Mother_occupation'])

mother, c_count = np.unique(mother, return_counts=True)
plt.barh(mother, c_count, color=('pink'))
plt.title("Mother's occupation")
plt.show()

#Data 11 - Time
time = np.array(data['time'])

time, c_count = np.unique(time, return_counts=True)
plt.bar(time, c_count)
plt.show()

#Data 12 -Performance
performance = np.array(data['Performance'])

performance, c_count = np.unique(performance, return_counts=True)
plt.bar(performance, c_count, color=('brown', 'yellow', 'green', 'lime'))
plt.title("Candidate's Performance")
plt.show()
