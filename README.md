main.py contains a basic Python code for comparing the similarities / dissimilarities of facial fetween between two same / different images respectively with a probability scale of 0 to 1 where, if two images are of the same individual it will label as True otherwise as False.
If the probability lies below 0.5 it assumes the facial features of the two images resembles to the same person, else if it goes above 0.5, it conveys the images are clearly distinct.
project.py contains the project code for taking in the images from the Attendance2.folder and marking the attendance.
The camera used for capturing the faces is the web cam of my local machine.
The Attendance.csv file contains 2 columns Name, Time where once the camera captures a face succesfully, it will recognise the face and label and also give the time of the face it captured which will automatically get updated in the csv file.
It can capture multiple faces simultaneously.
