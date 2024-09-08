import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.io as pio

def task_2_solver(df):
    # filter data as task said
    data = df.loc[(df['year'] >= 2016) & (df['year'] <= 2019)]
    data['sales_percentage'] = 100 * (data.groupby('store_name')['sale_dollars'].transform('sum') / data['sale_dollars'].sum()) # create sales percentage column
    new_data = data[['store_name', 'sales_percentage']] # new dataframe with sales percentage per Store
    new_data = new_data.drop_duplicates(subset = ['store_name']) # create the final dataframe by keeping the unique values based on store name
    new_data = new_data.sort_values(by = ['sales_percentage'], ascending = False).head(20) # top 20 results sorted

    # plot using pyplot
    plt.barh(new_data['store_name'], new_data['sales_percentage'], align = 'center')

    for index, row in new_data.iterrows():
        plt.annotate(round(row['sales_percentage'], 2), (row['sales_percentage'], row['store_name']))

    plt.subplots_adjust(left = 0.2)
    plt.xlabel('%Sales')
    plt.ylabel('Store Name')
    plt.title('%Sales by store')
    plt.savefig('./Plots/Task 2/pyplot.png')
    plt.show()

    # plot using seaborn
    sns.barplot(x = new_data['sales_percentage'], y = new_data['store_name'], orient = 'h')

    for index, row in new_data.iterrows():
        plt.annotate(round(row['sales_percentage'], 2), (row['sales_percentage'], row['store_name']))

    plt.subplots_adjust(left = 0.2)
    plt.xlabel('%Sales')
    plt.ylabel('Store Name')
    plt.title('%Sales by store')
    plt.savefig('./Plots/Task 2/seaborn.png')
    plt.show()

    # plot using Plotly
    trace = go.Bar(
        x = new_data['sales_percentage'],
        y = new_data['store_name'],
        orientation = 'h',
        marker = dict(
            color = new_data['sales_percentage'],
            line = dict(color = 'black', width = 1.5),
            showscale = True
        ),
        text = round(new_data['sales_percentage'], 2),
        textposition = 'outside'
    )

    layout = go.Layout(
        title = dict(
            text = '%Sales by Store',
            font = dict(size = 16, color = 'black')
        ),
        xaxis = dict(title = '%Sales'),
        yaxis = dict(title = 'Store Name'),
        plot_bgcolor = 'lightgray'
    )
    fig = go.Figure(data = [trace], layout = layout)
    pio.show(fig)
