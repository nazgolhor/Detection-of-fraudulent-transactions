#!/usr/bin/env python
# coding: utf-8

# In[2]:


def get_Transaction_dataset():
    
    try:

        Transact = {}
        with open('Transaction.txt') as f:
            for line in f:
                data = line.strip().split(":")
                #print(data)
                user_id = int(data[0])
                #print(user_id)
                transaction_id = int(data[1])
                description = data[2]
                amount = float(data[3])
                x = float(data[4])
                y = float(data[5])
                #print()
                checking_fraudulent = data[6].lower() == 'true'


                if user_id not in Transact:
                    Transact[user_id] = {}
                #print(users)
                Transact[user_id][transaction_id] = {
                    "description": description,
                    "amount": amount,
                    "x": x,
                    "y": y,
                    'checking_fraudulent': checking_fraudulent
                }
    except ValueError:
        print("Data not found from Transaction.txt.")
    except ZeroDivisionError:
        print("Data not found from Transaction.txt")
    except TypeError:
        print("Data not found from Transaction.txt")
    except:
        print("Data not found from Transaction.txt")
         

    return Transact


# In[ ]:




