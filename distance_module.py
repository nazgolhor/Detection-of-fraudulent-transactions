#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from dataset_module import get_Transaction_dataset

def distance_of_any_user():
        # Call a function named "get_Transaction_dataset" and assign its return value to "data"
    data = get_Transaction_dataset()
    try:
        # Get user_id and transaction IDs from the user
        user_id = int(input('Enter the user_id: '))
        transaction_id1 = int(input('Enter the first transaction id: '))
        transaction_id2 = int(input('Enter the second transaction id: '))
        
        # Get the transaction1 and 2
        transaction1 = data[user_id][transaction_id1]
        transaction2 = data[user_id][transaction_id2]
        # Get the x, y values from the transaction1 and 2
        x1, y1 = transaction1['x'], transaction1['y']
        x2, y2 = transaction2['x'], transaction2['y']
        # Calculate the distance between the two transactions
        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        # Print the distance
        print('The distance is', distance)
        # Handle specific exceptions
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    except KeyError:
        print("Invalid user_id or transaction_id. Please enter the correct value.")
    except TypeError:
        print("Invalid transaction data. Please check the data types of x and y values.")
    except ZeroDivisionError:
        print("Division by zero happened during distance calculation.")
    except:
        print("Sorry a different kind of Error happened!")



# In[ ]:



from dataset_module import get_Transaction_dataset

def distance_of_different_user():
        # Call a function named "get_Transaction_dataset" and assign its return value to "data"
    data = get_Transaction_dataset()
    try:
        # Get user IDs and transaction IDs from the user
        user1 = int(input('Enter the first user_id: '))
        user2 = int(input('Enter the second user_id: '))
        transaction_id1 = int(input('Enter the first transaction id: '))
        transaction_id2 = int(input('Enter the second transaction id: '))
        
        # Get the transactions from the data set for both users
            
        transaction1 = data[user1].get(transaction_id1)
        transaction2 = data[user2].get(transaction_id2)
        
        # Check if either transaction is not found, return None

        if not transaction1 or not transaction2:
            return None
        # Get the x, y values from the transaction1 and 2
        
        x1, y1 = transaction1["x"], transaction1["y"]
        x2, y2 = transaction2["x"], transaction2["y"]
        
        # Print the distance
        print('The distance is', ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
        # Handle specific exceptions
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    except KeyError:
        print("Invalid user_id or transaction_id. Please enter the correct value.")
    except TypeError:
        print("Invalid transaction data. Please check the data types of x and y values.")
    except ZeroDivisionError:
        print("Division by zero happened during distance calculation.")
    except:
        print("Sorry a different kind of Error happened!")

