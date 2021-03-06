import pandas as pd
import matplotlib.pyplot as plt
import csv
import Database


def showStatistics():
    orders = Database.orders
    dates = []
    revenues = []
    for id, order in orders.items():
        dates.append(order.date.strftime("%m-%d-%Y"))
        revenues.append(order.revenue)

    data = {'Date':  dates,
    'Purchase': revenues,
    }
    # data = {'Date':  ['09-01-2020', '09-01-2020', '09-02-2020', '09-02-2020', '09-02-2020', '09-03-2020', '09-03-2020', '09-03-2020', '09-04-2020', '09-04-2020', '09-04-2020', '09-04-2020', '09-05-2020', '09-05-2020', '09-05-2020', '09-05-2020', '09-05-2020', '09-06-2020', '09-06-2020', '09-06-2020', '09-07-2020', '09-07-2020', '09-07-2020', '09-07-2020', '09-07-2020', '09-07-2020', '09-07-2020', '09-08-2020', '09-08-2020', '09-09-2020', '09-09-2020', '09-10-2020', '09-10-2020', '09-10-2020', '09-11-2020', '09-11-2020', '09-12-2020', '09-12-2020', '09-13-2020', '09-14-2020', '09-14-2020', '09-15-2020', '09-15-2020', '09-16-2020', '09-16-2020', '09-17-2020', '09-17-2020', '09-18-2020', '09-18-2020', '09-20-2020', '09-21-2020', '09-22-2020', '09-22-2020', '09-22-2020', '09-23-2020', '09-23-2020', '09-24-2020', '09-25-2020', '09-25-2020', '09-25-2020', '09-25-2020', '09-26-2020', '09-27-2020', '09-27-2020', '09-28-2020', '09-29-2020', '09-30-2020', '09-30-2020', '09-30-2020', '09-30-2020',],
    #  'Purchase': [40, 26, 27, 34, 28, 21, 28, 34, 16, 36, 28, 22, 15, 56, 27, 13, 35, 41, 12, 15, 16, 17, 13, 16, 18, 22, 15, 16, 17, 13, 18, 26, 18, 12, 24, 22, 27, 24, 18, 21, 18, 24, 26, 26, 18, 32, 35, 26, 27, 23, 26, 38, 32, 25, 22, 15, 26, 27, 13, 28, 36, 11, 16, 23, 29, 22, 17, 23, 20, 21 ],
    #  }

    df = pd.DataFrame (data, columns = ['Date','Purchase'])
    df['Date'] = pd.to_datetime(df['Date'])
    #print (df.groupby(['Date']).sum().reset_index())
    plt.plot(df.groupby(['Date']).sum())
    plt.title('Revenue/Date Diagram')
    plt.xlabel('Date')
    plt.ylabel('Revenue (DKK)')
    plt.xticks(rotation=45)
    plt.show()
