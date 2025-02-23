import pandas as pd

df_credit= pd.read_csv('card_recommendation/card_data.csv')
df_check = pd.read_csv('card_recommendation/card_data_check.csv')

ls_benefits_credit = []
ls_benefits_check = []


def credit_benefits():
    for i in range(len(df_credit.index)): 
        ls_benefits_credit.append(df_credit.Benefits[i])
    
    # credit benefits 1 array 
    import ast

    # Flattening the 2D list and removing duplicates
    credit_flattened_list = set()

    for item in ls_benefits_credit:
        # Convert the string representation of the list into an actual list
        benefits_list = ast.literal_eval(item)
        # Add all elements of the list into the set to avoid duplicates
        credit_flattened_list.update(benefits_list)

        # Convert set back to list for final result
        credit_final_list = list(credit_flattened_list)
        credit_final_list.remove('유의사항')

    return credit_final_list
credit_benefits()



def check_benefits():
    for i in range(len(df_check.index)): 
        ls_benefits_check.append(df_check.Benefits[i])

    # check
    import ast
    check_flattened_list = set()

    for item in ls_benefits_check:
        # Convert the string representation of the list into an actual list
        benefits_list = ast.literal_eval(item)
        # Add all elements of the list into the set to avoid duplicates
        check_flattened_list.update(benefits_list)

    # Convert set back to list for final result
        check_final_list = list(check_flattened_list)
    return check_final_list

check_benefits()