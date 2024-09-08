import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

def task_1_solver(df):
    # filter data as task said
    data = df.loc[(df['year'] >= 2016) & (df['year'] <= 2019)]
    data = data.groupby(['zip_code', 'item_number'])['bottles_sold'].sum().reset_index()
    top_6_indices = data.sort_values(by = ['bottles_sold'], ascending = False).head(6)
    print('Top 6 items:\n', top_6_indices)

    # Plot results using different packages
    plt.figure(figsize = (12, 6))

    for index, row in data.iterrows():
        plt.scatter(index, row['bottles_sold'], label = row['item_number'])

    for index, row in top_6_indices.iterrows():
        plt.annotate(row['item_number'], (index, row['bottles_sold']))

    plt.xlabel('Zipcode')
    plt.ylabel('Bottles sold')
    plt.title('Bottles sold')
    plt.grid(True)
    plt.savefig('./Plots/Task 1/pyplot.png')
    plt.show()

    sns.scatterplot(x = data.index.values, y = data['bottles_sold'], data = data, marker = 'o')

    for index, row in top_6_indices.iterrows():
        plt.annotate(row['item_number'], (index, row['bottles_sold']))

    plt.title('Bottles sold')
    plt.xlabel('Zipcode')
    plt.ylabel('Bottles sold')
    plt.grid(True)
    plt.savefig('./Plots/Task 1/seaborn.png')
    plt.show()

    fig = go.Figure(
        go.Scatter(
            x = data.index.values, y = data['bottles_sold'], mode = 'markers',
            marker = dict(
                size = data['bottles_sold'] / 10,
                color = data.index.values,
                showscale = True
            ),
            text = data.index.values
        )
    )
    fig.update_layout(title = 'Bottles sold', xaxis_title = 'Zipcode', yaxis_title = 'Bottles sold')
    fig.show()