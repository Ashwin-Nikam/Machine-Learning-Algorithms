#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    error_list = []

    ### your code goes here
    for i in range(len(predictions)):
        prediction = predictions[i][0]
        net_worth = net_worths[i][0]
        error = net_worth - prediction
        error_list.append(error)

    error_list.sort()
    size = len(predictions)
    n = 0.9 * size
    x = size - n
    error_list = error_list[:int(x)]
    
    for i in range(len(predictions)):
        prediction = predictions[i][0]
        net_worth = net_worths[i][0]
        age = ages[i][0]
        error = net_worth - prediction
        if error not in error_list:
            my_tuple = (age, net_worth, error)
            cleaned_data.append(my_tuple)
    
    return cleaned_data

