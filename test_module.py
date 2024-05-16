#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Here the distance_module and statistics_module are imported inorder to fetch functions from them.
import distance_module as mod
import statistics_module as modi
# defining an usder interface module for customer to interact with the functions.
def user_interface_with_other_module():
    # using while loop for looping the questions again until the customer decides to quit.
    while True:
        
            #list of choices for the client to select one
        print('\n')
        print("Thank you for using our transaction analysis too")
        print("-------------------------------------------------------")
        print("Please select one from the options listed below.")
        print('\n')
        print('DISTANCE')
        print("1.Calculate distance between two transactions made by the same user")
        print("2.Calculate distance between two transactions made by the different users")
        print('\n')
        print('transaction')
        print("3.Calculate the average number of transactions for the specified user_id and all user_ids.")
        print("4.Calculate the mode number of transactions for the specified user_id and all user_ids")
        print("5.Calculate the median number of transactions for the specified user_id and all user_ids")
        print("6.Calculate the interquartile range of transactions of the given user_id and all user_ids")
        print("7.Calculate the Location Centroid of the given user_id, based on their Transaction Locations")
        print("8.Calculate the Standard Deviation of Transactions of the given user_id.")
        print("9.Check whether the given transaction_id is fraudulent or not and also specify the details of that transaction_id")
        print("10.Discover the abnormal transactions for the given user_id")
        print("11.Calculate the Z score of transactions of the given user_id and all user_ids")
        print("12.Calculate the frequencies of transactions at any given location")
        print("13.Calculate the nth percentiles of transactions of any user and all of users")
        print("14.Calculate the outliers of each location of given user_id")
        print("15.Quit")
            # prompts the customer to choose an option by entering a numerical choice
        choice = int(input("Enter your selection.: "))
            #if the customer enter 1, goes to distance module for single user transaction 

        if choice == 1:
            mod.distance_of_any_user()
            #if the customer enter 2, goes to distance module for different user transaction 
        elif choice == 2:
            mod.distance_of_different_user()
            #if the customer enter 3, goes to statistics module for finding average 
        elif choice == 3:
            modi.get_the_average()
            #if the customer enter 4, goes to statistics module for finding mode
        elif choice == 4:
            modi.get_the_mode()
            #if the customer enter 5, then goes to statistics module for finding median
        elif choice == 5:
            modi.get_the_median()
            #if the customer enter 6, then goes to statistics module for finding interquartile range
        elif choice == 6:
            modi.get_the_interquartile_range()
            #if the customer enter 7, then goes to statistics module for finding location centroid
        elif choice ==7:
            modi.get_the_location_centroid()
            #if the customer enter 8, then goes to statistics module for finding standard deviation
        elif choice == 8:
            modi.get_the_standard_deviation()
            #if the customer enter 9, then goes to statistics module for checking whether fraudulent or not
        elif choice == 9:
            modi.checking_if_fraudulent()
            #if the customer enter 10, then goes to statistics module for finding abnormal transaction
        elif choice == 10:
            modi.get_the_abnormal_transaction()
            #if the customer enter 11, then goes to statistics module for finding z scores
        elif choice == 11:
            modi.get_the_z_scores()
            #if the customer enter 12, then goes to statistics module for finding location_frequency
        elif choice == 12:
            modi.get_the_location_frequency()
            #if the customer enter 13, then goes to statistics module for finding nth percentile
        elif choice == 13:
            modi.percentile_Trans_transaction()
            #if the customer enter 14, then goes to returning the outliers
        elif choice == 14:
            modi.get_the_outlier()
            #if the customer enter 15, then quits the program
        elif choice == 15:
            print("Bye!")
            break
        else:
                #Otherwise prints invalid choice 
            print("Sorry dear customer,Invalid choice, please try again.")
        # showing exceptions and providing proper comments to be showed
        


