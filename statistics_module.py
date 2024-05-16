#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from dataset_module import get_Transaction_dataset

# Define a function named "get_the_average"
def get_the_average():
    # Call a function named "get_Transaction_dataset" and assign its return value to "data"
    data = get_Transaction_dataset()
    try:
    # Ask the user to enter an integer user_id 
        id = int(input("Enter the user_id: "))
    # If the input is not a valid integer, print an error message and return
    except ValueError:
        print("user_id must be a valid integer")
        return
    # Create an empty dictionary to store the average transaction amount of each user
    users_amounts = {}
    # Create an empty list to store all transaction amounts
    all_amounts = []
    # Loop through each user_id in the dataset
    for user_id in data:
        # Get the transactions associated with the current user_id
        transactions = data[user_id]
        # Create an empty list to store the transaction amounts of the current user
        amounts = []
        # Loop through each transaction for the current user
        for transaction in transactions.values():
        # Add the amount of the current transaction to the "amounts" list
            amounts.append(transaction["amount"])
        # Add the amount of the current transaction to the "all_amounts" list
            all_amounts.append(transaction["amount"])
        # If the current user has no transactions, assign a value of 0 to their average transaction amount
        if len(amounts) == 0:
            user_amounts[user_id] = 0
        # Calculate the average transaction amount for the current user
        else:
            
            average_amount = sum(amounts) / len(amounts)
        # Assign the average transaction amount to the current user in the "users_amounts" dictionary
            users_amounts[user_id] = average_amount
    
    try:
        # Try to get the average transaction amount for the user with the input id from the "users_amounts" dictionary
        average_user = users_amounts[id]
        # If the input id does not exist in the transaction dataset, print an error message and return
    except KeyError:
        print("User_id does not exist in the transaction data" % id)
        return
    # Calculate the average transaction amount for all users in the transaction dataset
    
    average_total = sum(all_amounts) / len(all_amounts)
    # Print the average transaction amount for all users
    print("Total Transaction Average of all users is: %f" % average_total)
    
    try:
    # Try to get the average transaction amount for the user with the input id from the "users_amounts" dictionary
        average_user = users_amounts[id]
    # If the input id does not exist in the transaction dataset, print an error message and return
    except KeyError:
        print("User_id does not exist in the transaction data" % id)
        return
    # If the user with the input id has no transactions, print an error message and return
    except ZeroDivisionError:
        print("User_id has no transactions" % id)
        return
    # Print the average transaction amount for the user with the input id
    
    print("The average transactions of user_id %s is %f" % (id, average_user))
    return


# (b) A function to return the mode of transactions of any user and that of all users.
from dataset_module import get_Transaction_dataset

def mode(values):
    # Initialize the mode variable to None
    mode = None
    # Initialize a frequency dictionary to keep track of how often each value appears
    freq_dict = {}
    #Iterate through each value in the input list
    for value in values:
        # If the value is already in the frequency dictionary, increment its count
        if value in freq_dict:
            freq_dict[value] += 1
        # Otherwise, add the value to the dictionary with a count of 1
        else:
            freq_dict[value] = 1
        # If the current value has a higher count than the current mode, update the mode variable
        if mode is None or freq_dict[value] > freq_dict[mode]:
            mode = value
    # If the most common value occurs only once, there is no mode, so return None
    if freq_dict[mode] == 1:
        return None
    # Otherwise, return the mode
    return mode

def get_the_mode():
    # Call a function named "get_Transaction_dataset" and assign its return value to "data"
    data = get_Transaction_dataset()
    try:
        # Try to get an integer user ID from the user
        id = int(input("Enter the user_id: "))
    # If the user enters a non-integer value, print an error message and return
    except ValueError:
        print("User ID must be a valid integer")
        return
    # Create an empty dictionary to keep track of the mode transaction amount for each user
    user_amounts = {}
    # Create an empty list to keep track of all transaction amounts
    all_amount = []
    # Iterate through each user in the transaction data
    for user_id in data:
        # Get the transactions for the current user
        transactions = data[user_id]
        # Create an empty list to keep track of transaction amounts for the current user
        amounts = []
        # Iterate through each transaction for the current user
        for transaction in transactions.values():
            # Append the transaction amount to the list of amounts for the current user
            amounts.append(transaction["amount"])
            # Append the transaction amount to the list of all amounts
            all_amount.append(transaction["amount"])
        # Calculate the mode transaction amount for the current user
        mode_amount = mode(amounts)
        # Add the mode transaction amount to the user_amounts dictionary
        user_amounts[user_id] = mode_amount
        
        # Try to get the mode transaction amount for the requested user_id
        try:
        mod_user = user_amounts[id]
        # If the user_id is not in the transaction data, print an error message and return
    except KeyError:
        print("User_id %s does not exist in the transaction data" % id)
        return
    # If the requested user_id has no mode transaction amount, print an error message and return
    except TypeError:
        print("User_id %s has no mode for transaction amounts" % id)
        return
    # Calculate the mode transaction amount for all users
    mod_total = mode(all_amount)
    print("Total Transaction mode is: %s" % (str(mod_total) if mod_total is not None else "N/A"))
    print("The mode of user %s is: %s" % (id, str(mod_user) if mod_user is not None else "N/A"))
    
    

# (c) A function that returns the median of all transactions of a user and that of all users
from dataset_module import get_Transaction_dataset

def median(values):
    # Sort the list of values in ascending order
    values.sort()
    # Calculate the length of the list of value
    length = len(values)
    # Check  the length of the list of values 
    if length % 2 == 0:
        # Calculate the index of the median element when the list length is zero
        med = length // 2
        # Calculate the median by taking the average of the two middle values
        median = (values[med - 1] + values[med]) / 2
    # Otherwise calculate the index of the median element when the list length is odd
    else:
        mid = length // 2
        # Retrieve the median element
        median = values[med]
    # Return the median value
    return median

def get_the_median():
    # Call a function named "get_Transaction_dataset" and assign its return value to "data"
    data = get_Transaction_dataset()
    try:
        # Prompt the user to enter an integer user_id
        id = int(input("Enter the user_id: "))
    except ValueError:
        # Print an error message if the user input is not a valid integer
        print("User_id must be a valid integer")
        
        return
    # Create an empty dictionary to store the median transaction amount for each user.
    users_amounts = {}
    #Create an empty list to store all transaction amounts
    all_amounts = []
    # Loop through each user in the data dictionary.
    for user_id in data:
        # Get the transactions for the current user
        transactions = data[user_id]
        # Create an empty list to store the transaction amounts for the current user.
        amounts = []
        # Loop through each transaction for the current user
        for transaction in transactions.values():
            # Get the transaction amount and append it to the list of amounts for the current user
            amounts.append(transaction["amount"])
            # Append the transaction amount to the list of all transaction amounts
            all_amounts.append(transaction["amount"])
        # Calculate the median transaction amount for the current user.
        median_amount = median(amounts)
        # Store the median transaction amount for the current user in the users_amounts dictionary.
        users_amounts[user_id] = median_amount
        
    # Try to get the median transaction amount for the specified user id.
    try:
        median_user = users_amounts[id]
    # If the specified user id does not exist in the data dictionary, print an error message and return.
    except KeyError:
        print("user_id %s does not exist in the transaction data" % id)
        return
    # Calculate the median transaction amount for all transactions.
    median_total = median(all_amounts)
    # Print the median transaction amount for all transactions and the median transaction amount for the specified user.
    print("The total Transaction median is: %f" % median_total)
    print("The median of user_id %s is %f" % (id, median_user))
    
     
from dataset_module import get_Transaction_dataset
 #Define a function that returns the interquartile range of transactions of a user and that of all users. 
def get_the_interquartile_range():
    # Try to get the user_id from user input and convert it to an integer.
    try:
    
        id = int(input("Enter the user_id: "))
    except ValueError:
        print("User_id should be an integer")
        return
    # Call a function named "get_Transaction_dataset" and assign its return value to "data"
    data = get_Transaction_dataset()
    # Create an empty dictionary to store the median transaction amount for each user.
    users_amounts = {}
    # Create an empty list to store all transaction amounts
    all_amounts = []
    # Loop through each user in the data dictionary
    for user_id in data:
        # Get the transactions for the current user.
        transactions = data[user_id]
        # Create an empty list to store the transaction amounts for the current user.
        amounts = []
        # Loop through each transaction for the current user.
        for transaction in transactions.values():
            # Get the transaction amount and append it to the list of amounts for the current user.
            amounts.append(transaction["amount"])
             # Append the transaction amount to the list of all transaction amounts.
            all_amounts.append(transaction["amount"])
        # Calculate the median transaction amount for the current user.
        median_amount = median(amounts)
        # Store the median transaction amount for the current user in the users_amounts dictionary.
        users_amounts[user_id] = median_amount
    # Sort the list of all transaction amounts.
    sorted_all_amounts = sorted(all_amounts)
    # Calculate the indices of the first and third quartiles.
    # Calculate the first and third quartiles and the interquartile range.
    n = len(sorted_all_amounts)
    q1_index = int((n+1)/4) - 1
    q1 = sorted_all_amounts[q1_index]
    q3_index = int(3*(n+1)/4) - 1
    q3 = sorted_all_amounts[q3_index]
    iqr = q3 - q1
    # Print the interquartile range for all transactions.
    print("Transaction interquartile range for all users is: %f" % iqr)
    # If the specified user id exists in the users_amounts dictionary, calculate the interquartile range for that user.
    if id in users_amounts:
        # Get the transactions for the specified user.
        user_transactions = data[id]
        # Create a list of the transaction amounts for the specified user.
        users_amounts = [transaction["amount"] for transaction in user_transactions.values()]
        # Sort the list of transaction amounts for the specified user.
        sorted_users_amounts = sorted(users_amounts)
        # Calculate the indices of the first and third quartiles for the specified user.
        # Calculate the first and third quartiles and the interquartile range for the specified user.
        n = len(sorted_users_amounts)
        q1_index = int((n+1)/4) - 1
        q1 = sorted_users_amounts[q1_index]
        q3_index = int(3*(n+1)/4) - 1
        q3 = sorted_users_amounts[q3_index]
        user_iqr = q3 - q1
        # Print the interquartile range for the specified user.
        print("Transaction interquartile range for user %s is: %f" % (id, user_iqr))
    else:
        print("User %s not found" % id)

        

# (e) A function that returns the location centroid of any user based on the transaction locations.         
from dataset_module import get_Transaction_dataset

def get_the_location_centroid():
    # Call a function named "get_Transaction_dataset" and assign its return value to "data"
    data = get_Transaction_dataset()
    try:
        # Ask the user to enter a user_id and convert it to an integer
        id = int(input('Enter the user_id: '))
        # Get the transactions for the given user_id
        user_transactions = data.get(id)
        # If user_transactions is None, print an error message and return
        if user_transactions is None:
            print("User_id %s not found" % id)
            return
        # Initialize empty lists for x and y coordinates
        x = []
        y = []
        # Iterate over the transactions for the user and append the x and y coordinates to their respective lists
        for transaction in user_transactions.values():
            x.append(transaction["x"])
            y.append(transaction["y"])
        # Calculate the centroid x and y coordinates by dividing the sum of all x and y coordinates by the number of transactions
        centroid_x = sum(x) / len(x)
        centroid_y = sum(y) / len(y)
        # Print the centroid x and y coordinates
        print("Centroid x: %f" % centroid_x)
        print("Centroid y: %f" % centroid_y)
    # If the user enters an invalid integer for the user_id, print an error message
    except ValueError:
        print("Please enter a valid integer for user_id.")
    # If there is any other error, print an error message
    except Exception:
        print("There is an error in calculating the centroid.")


        # (f) A function that returns the standard deviation of any specif user's transactions.     
from dataset_module import get_Transaction_dataset

def get_the_standard_deviation():
    try:
        # Call a function named "get_Transaction_dataset" and assign its return value to "data"
        data = get_Transaction_dataset()
        # Prompt user to enter a user_id as input and convert it to an integer
        id = int(input('Enter the user_id: '))
        # Get the transactions for the given user_id from the dataset
        user_transactions = data.get(id)
        # If user_transactions is None, print an error message and return from the function
        if user_transactions is None:
            print("User %s not found" % id)
            return
        # Create an empty list called "amounts" to hold transaction amounts
        amounts = []
        # Iterate through each transaction for the given user and append its amount to the amounts list
        for transaction in user_transactions.values():
            amounts.append(transaction["amount"])
        # Calculate the mean amount for the user
        mean_price = sum(amounts) / len(amounts)
        # Initialize the variance variable to 0
        variance = 0
        # Calculate the variance by summing the squared difference of each amount from the mean
        for amount in amounts:
            
            variance += (amount - mean_price) ** 2
        # Divide the variance by the number of amounts to get the variance
        variance /= len(amounts)
        # Calculate the standard deviation by taking the square root of the variance
        standard_deviation = variance ** 0.5
        # Print the standard deviation for the given user_id
        print("The standard deviation of amounts for user_id %s: %f" % (id, standard_deviation))
    # Catch a ValueError if the user_id input is not an integer and print an error message
    except ValueError:
        print("Error: the user_id is invalid. Please enter a valid integer user_id.")
    # Catch a ZeroDivisionError if the user has no transactions and print an error message
    except ZeroDivisionError:
        print("Error: user has not any transaction.")
    # Catch all other exceptions and print a generic error message
    except Exception:
        print("There is an error in calculating standard deviation:")
        
        # (g) A function that determines whether a transaction is fraudulent or not.
from dataset_module import get_Transaction_dataset

def checking_if_fraudulent():
    try:
        # Call a function named "get_Transaction_dataset" and assign its return value to "data"
        data = get_Transaction_dataset()
        # Prompt the user to enter the Transaction_id and convert it to an integer and assign it to "id"
        id = int(input('Enter the Transaction_id: '))
        # Initialize the variable "transaction" to None
        transaction = None
        # Iterate over the dictionary of transactions to find the transaction with the specified "id"
        for user_transactions in data.values():
            # If the transaction is not found, print an error message and return
            if id in user_transactions:
                transaction = user_transactions[id]
                break
        if transaction is None:
            print("Transaction %s not found" % id)
            return
        # Get the value of "checking_fraudulent" from the transaction
        checking_fraudulent = transaction.get("checking_fraudulent")
        # If "checking_fraudulent" is not found in the transaction, print an error message and return
        if checking_fraudulent is None:
            print("checking_fraudulent not found in transaction %s" % id)
            return
        # If "checking_fraudulent" is True, print a message indicating that the transaction is fraudulent along with the details of the transaction
        if checking_fraudulent:
            print("Transaction %s is fraudulent" % id)
            print("Details of transaction:")
            print(transaction)
        # If "checking_fraudulent" is False, print a message indicating that the transaction is not fraudulent
        else:
            print("Transaction %s is not fraudulent" % id)
    # If the user inputs an invalid value for "id", catch the ValueError exception and print an error message
    except ValueError:
        print("Invalid input: please enter a valid integer for Transaction_id")
    # If any other exception occurs, catch it and print an error message
    except:
        print("Sorry an error occurred")
        
        
        # (h) A function that returns the abnormal transaction of any given user. 
from dataset_module import get_Transaction_dataset

def get_the_abnormal_transaction():
    try:
        # Call a function named "get_Transaction_dataset" and assign its return value to "data"
        data = get_Transaction_dataset()
        # Get the user_id input from user
        id = int(input('Enter the user_id: '))
        # get transactions for the user ID
        user_transactions = data.get(id)
        # Check if the user_id exists in the datase
        if user_transactions is None:
            # if user ID not found, print message and return
            print("User %s not found" % id)
            return
        # Extract the amount data for each transaction and calculate the average and standard deviation
        amounts = [transaction["amount"] for transaction in user_transactions.values()]
        average_amount = sum(amounts) / len(amounts)
        std_dev = (sum((amount - average_amount) ** 2 for amount in amounts) / len(amounts)) ** 0.5
        # create an empty list for abnormal transactions
        abnormal_transactions = []
        # loop through each transaction
        for transaction_id, transaction in user_transactions.items():
            #  if the transaction amount is greater than 3 standard deviations from the average, it is considered abnormal
            if abs(transaction["amount"] - average_amount) > 3 * std_dev:
                # add the abnormal transaction to the list
                abnormal_transactions.append((transaction_id, transaction))
        # if there are abnormal transactions, print them
        if abnormal_transactions:
            print("Abnormal transactions for user %s:" % id)
            for transaction_id, transaction in abnormal_transactions:
                print("%s: %s" % (transaction_id, transaction))
        # if there are no abnormal transactions, print message
        else:
            print("There is no abnormal transactions for user %s" % id)
    # handle invalid user ID input
    except ValueError:
        print("Error: Invalid user_id entered.")
    # handle any other exceptions that may occur
    except Exception:
        print("There is an error while processing the data.")
    
# (j) A function that computes those frequencies of transactions at any given location. 
    
from dataset_module import get_Transaction_dataset

def get_the_location_frequency():
    try:
        # Call a function named "get_Transaction_dataset" and assign its return value to "data"
        data = get_Transaction_dataset()
        # Ask the user to enter the x and y coordinates of the location to be searched for
        x = float(input("Please enter the x: "))
        y = float(input("Please enter the y: "))
        # Assign the location coordinates as a tuple to the variable named "location"
        location = (x, y)
        # Initialize the variable named "total_frequency" as zero
        total_frequency = 0
        # Iterate through all user ids in the dataset
        for user_id in data:
            # Iterate through all transaction ids of the current user
            for transaction_id in data[user_id]:
                # Assign the transaction details to the variable named "transaction"
                transaction = data[user_id][transaction_id]
                # Check if the transaction location matches the searched location
                if (transaction["x"], transaction["y"]) == location:
                    #Increment the transaction frequency by 1
                    total_frequency += 1
        # Print the total frequency of transactions at the searched location
        print("The total transaction frequency at location ({}, {}) is: {}".format(x, y, total_frequency))
    # Handle the exceptions if any of the below errors occur during the execution of the code
    except ValueError:
        print("Error: Invalid x or y entered. Please enter valid values.")
    except ZeroDivisionError:
        print("Error: Division by zero heppened. Please check the values of input.")
    except TypeError:
        print("Error: Type not match . Please check the values of input.")
    except:
        print("There is an error while processing the data.")
        
        
        
        # (j) A function that computes z score of any user and all users        
    from dataset_module import get_Transaction_dataset

    def get_the_z_scores():
    try:
        # Call a function named "get_Transaction_dataset" and assign its return value to "data"
        data = get_Transaction_dataset()
         # Ask user to enter a user_id as an integer
        id = int(input('Please enter the user_id: '))
        # Create empty lists for all_transactions, user_z_scores, and all_z_scores
        all_transactions = []
        user_z_scores = []
        all_z_scores = []

        # Z score for a specific user
        user_transactions = data.get(id)
        if user_transactions:
            amounts = []
            # Append the amount of each transaction to "amounts" list
            for transaction in user_transactions.values():    
                amounts.append(transaction["amount"])
            # Calculate the mean and standard deviation of amounts and calculate z score for each transaction
            mean_amount = sum(amounts) / len(amounts)
            std_amount = (sum((amount - mean_amount) ** 2 for amount in amounts) / len(amounts)) ** 0.5
            for transaction in user_transactions.values():
                z_score = (transaction["amount"] - mean_amount) / std_amount
                # Append the z score of each transaction to "user_z_scores" list
                user_z_scores.append(z_score)
            print("Z scores for user {}:".format(id), user_z_scores)
        else:
            print("User {} not found".format(id))

        # Z score for all users
        for user_transactions in data.values():
            amounts = []
            for transaction in user_transactions.values(): 
                 # Append the amount of each transaction to "amounts" list
                amounts.append(transaction["amount"])
            # Calculate the mean and standard deviation of amounts and calculate z score for each transaction
            mean_amount = sum(amounts) / len(amounts)
            std_amount = (sum((amount - mean_amount) * 2 for amount in amounts) / len(amounts)) * 0.5
            for transaction in user_transactions.values():
                z_score = (transaction["amount"] - mean_amount) / std_amount
                # Append the z score of each transaction to "all_z_scores" list
                all_z_scores.append(z_score)
        print("\n Z scores for all users:", all_z_scores)

    except ValueError:
        print("Error: the user_id is invalid. Please enter a valid integer user_id.")
    except Exception as e:
        print("There is an error in calculating Z scores:", e)
        
        
    #nth percentile
    from dataset_module import get_Transaction_data_set

def percentile_Trans_transaction():
    # Call a function named "get_Transaction_dataset" and assign its return value to "data"
    data = get_Transaction_data_set()
    try:
        user_id = int(input("Enter the user_id: "))
        n = int(input("Enter the percentile (0-100): "))
    except ValueError:
        print("User ID and percentile must be valid integers")
        return
    
    # Calculate percentile for a specific user
    from dataset_module import get_Transaction_dataset

def percentile_Trans_transaction():
    # Call a function named "get_Transaction_dataset" and assign its return value to "data"
    data = get_Transaction_dataset()
    try:
        # Prompt user to input user_id and percentile values as integers
        user_id = int(input("Enter the user_id: "))
        n = int(input("Enter the percentile (0-100): "))
    # If user_id and percentile are not integers, print an error message and return
    except ValueError:
        print("User ID and percentile must be valid integers")
        return
    
    # Calculate percentile for a specific user
    if user_id in data:
        # Get the transactions of the specified user
        transactions = data[user_id]
        # Get the amounts of the transactions of the specified user
        amounts = [transaction["amount"] for transaction in transactions.values()]
        # If the specified user has no transactions, print an error message and return
        if len(amounts) == 0:
            print("User ID %s has no transactions" % user_id)
            return
        # Sort the amounts of the transactions of the specified user in ascending order
        amounts.sort()
        # Calculate the index of the percentile in the sorted amounts list
        index = int(n/100 * len(amounts))
        # Get the value of the percentile
        percentile = amounts[index]
        # Print the percentile value for the specified user
        print("The %dth percentile of user %s is: %f" % (n, user_id, percentile))
    # If the specified user does not exist in the transaction data, print an error message and return
    else:
        print("User ID %s does not exist in the transaction data" % user_id)
    
    # Calculate percentile for all users
    # Get all the amounts of the transactions of all users
    all_amounts = [transaction["amount"] for transactions in data.values() for transaction in transactions.values()]
    # If there are no transactions in the dataset, print an error message and return
    if len(all_amounts) == 0:
        print("No transactions found in the dataset")
        return
    # Sort all the amounts of the transactions in the dataset in ascending order
    all_amounts.sort()
    # Calculate the index of the percentile in the sorted amounts list
    index = int(n/100 * len(all_amounts))
    # Get the value of the percentile
    percentile = all_amounts[index]
    # Print the percentile value for all users
    print("The %dth percentile of all transactions is: %f" % (n, percentile))
    
    
from dataset_module import get_Transaction_dataset

def get_the_outlier():
    id=int(input('enter the user_id'))
    data = get_Transaction_dataset()
    # Retrieving the user's transactions from the data set
    user_transactions = data.get(id)
    # Checking if the user exists in the data set
    if user_transactions is None:
        print("User %s not found" % id)
        return
    # Creating empty lists to store the x and y of the user's transactions
    x = []
    y = []
    # Looping through the user's transactions and adding the x and y to their lists
    for transaction in user_transactions.values():
        x.append(transaction["x"])
        x.append(transaction["y"])
    # Calculating the centroid x and y by taking the average of the x and y, respectively
    x_user = sum(x) / len(y)
    y_user = sum(y) / len(y)
    # Printing the centroid x and y
    print("Centroid latitude: %f" % Lat_user)
    print("Centroid longitude: %f" % long_user)
    
    distance_dictionary = {}
    distance_list = []
    for user_id in data:
        transactions = data[user_id]
        if id == user_id:
            for i in transactions.keys():
                x = (transactions[i]["x"])
                y = (transactions[i]["y"])
                distance = ((x - x_user)*2 + (y - y_user)*2)
                distance_list.append(distance)
                distance_dictionary[i] = distance

    index1 = len(sorted(distance_list))*.25
    Q1 = sorted(distance_list)[round(index1)-1]
    index3 = len(sorted(distance_list))*.75
    Q3 = sorted(distance_list)[round(index3)-1]
    IQR = Q3 - Q1
    OutlierLoc =[]
    for i in distance_list:
        if i > (Q3 + (1.5 * IQR)) or i < (Q1 - (1.5*IQR)):
            OutlierLoc.append(i)
    keys = []

    for value in distance_dictionary.values():
        if value in OutlierLoc:
            for key, val in distance_dictionary.items():
                if val == value:
                    keys.append(str(key))
    return keys

