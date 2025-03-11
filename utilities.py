import numpy as np

# converts string into an array.
def make_array(dataset):
    this_array = []
    this_list = []

    # If a string, split the lines. 
    if (type(dataset) == str):
        this_list = dataset.splitlines()

    # Leave alone if dataset is already an array.
    elif (type(dataset) == list):
        this_list = dataset

    # split each character.
    for i in this_list:
        this_array.append(list(i))

    return this_array
    


# transposes an array.
def transpose_array(array):
    return np.asarray(array).transpose()



# converts array into a string.
def array_to_string(array):

    this_string = ''

    for i in range(len(array)):
        
        if i !=len(array)-1:
            this_string = this_string + ''.join(array[i].tolist()) + '\n'
        else:
            this_string = this_string + ''.join(array[i].tolist())
        
    return this_string