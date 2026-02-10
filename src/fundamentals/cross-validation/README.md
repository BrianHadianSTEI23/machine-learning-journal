# Cross Validation
Cross validation is a method to check what algorithm is the best for the current data by applying it into the data
and then testing the model by using the test data for determining if the model got it right. For each algorithm, it
is counted for how many sample that got right and wrong. Those algorithm which has the most rights will be chosen for 
further use in the model

# Motivation
Given a data, how do we check what method will works best with the data?

# Limitation
None

# Types of Cross validation
## N-Fold cross validation  

### Algorithm
1. Data is split into N blocks and for N times, 
2. N - 1 blocks is chosen as training data and the leftout block will be chosen as test data.
3. Every iteration, the leftout block will be chosen again such that it is not the block that has been used as test data.  
  
## Leave one out validation
### Algorithm
1. Every sample (N) - 1 is run through the algorithm and one is chosen as test datum. 
2. This will be done N times with every iteration, the leftout datum will be chosen again such that it is not the datum that has been used as test datum.

# Sources
- https://www.youtube.com/watch?v=fSytzGwwBVw&list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF&index=2
- https://www.w3schools.com/python/python_file_open.asp
- https://www.geeksforgeeks.org/python/pandas-how-to-shuffle-a-dataframe-rows/
- https://stackoverflow.com/questions/13411544/delete-a-column-from-a-pandas-dataframe 
