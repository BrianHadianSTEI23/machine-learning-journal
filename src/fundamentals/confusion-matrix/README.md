# Confusion Matrix
Confusion matrix is a matrix used for determining which algorithm to use based on how many prediction is right and
how many prediction is wrong. Based on those how many those are, a formula to check the accuracy of algorithm may
be used to quantify how 'right' an algorithm is. 

# Motivation
Given a categorical dataset, how do you determine the best algorithm for prediction?

# Limitation
Only works for categorical task.

# Algorithm
1. Given a set of algorithm for prediction, for each algorithm, do prediction for the test data
2. For a given prediction column, make a matrix out of the distinct values from that particular column which 
classified into true positive (prediction and actual data is both right), true negatives (prediction and actual are both wrong),
false negatives (prediction predicts false, but is actually true) or false positives (prediction predicts true, but is
actually false)
3. Compare the prediction and the actual data and classify each sample into true positive, true negatives, false negatives, 
or false positives (it may expand if the distinct values of the predicted column has > 2 distinct values)
4. Calculate the accuracy for each algorithm using cross validation and pick one that has the minimum 'falses'

# Example
We want to assign team members to project tasks. Each task requires certain skills, and each team member has different skill levels. The cross matrix helps visualize and decide who is best suited for each task.  
Confusion Matrix:
| **Task / Member** | **Alice** | **Bob**   | **Charlie** | **Diana** |
| ----------------- | --------- | --------- | ----------- | --------- |
| **Data Analysis** | ✅ High    | ⚠️ Medium | ❌ None      | ✅ High    |
| **UI Design**     | ⚠️ Medium | ❌ None    | ✅ High      | ✅ High    |
| **Backend Dev**   | ❌ None    | ✅ High    | ⚠️ Medium   | ⚠️ Medium |
| **Testing**       | ✅ High    | ✅ High    | ❌ None      | ⚠️ Medium |

# Sources
- https://www.youtube.com/watch?v=Kdsp6soqA7o&list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF&index=3