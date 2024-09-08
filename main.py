import pandas as pd
from clean_data import clean_data
from most_popular_per_zip_code import task_1_solver
from sales_percentage_per_store import task_2_solver

def main():
    data = pd.read_csv('./Data/finance_liquor_sales.csv') # create a DataFrame with csv data

    data = clean_data(data) # clean data using the function
    task_1_solver(data) # solve the first task using the function
    task_2_solver(data) # solve the second task using the function

if __name__ == '__main__':
    main()
