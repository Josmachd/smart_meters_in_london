import numpy as np
import matplotlib.pyplot as plt

def show_plots(): # Show all plots
    plt.show()

def plot1(df): # Plot general View of the model
    fig, ax = plt.subplots(figsize =(30, 6))
    fig.suptitle('Anomaly Isolation forest')

    a = df.loc[df['anomaly_forest'] == -1, ['day_int', 'energy']] #anomaly

    ax.plot(df['day_int'], df['energy'], color='blue', zorder=0)
    ax.scatter(a['day_int'],a['energy'], color='red', zorder=5)
        
    fig.tight_layout()
    #plt.show()

def plot2(df): # Plot selected houses
    h1 = df[df['house'] == 'MAC000018']
    a1 = h1.loc[h1['anomaly_forest'] == -1]
    
    h2 = df[df['house'] == 'MAC000130']
    a2 = h2.loc[h2['anomaly_forest'] == -1]
        
    h3 = df[df['house'] == 'MAC000044']
    a3 = h3.loc[h3['anomaly_forest'] == -1]
    
    
    fig, (ex1, ex2, ex3) = plt.subplots(3, figsize =(30, 6))
    fig.suptitle('Tree houses example')
    
    ex1.set_title('MAC000018')
    ex1.plot(h1['day_int'], h1['energy'], zorder=0)
    ex1.scatter(a1['day_int'],a1['energy'], color='red', zorder=5)
    
    ex2.set_title('MAC000130')
    ex2.plot(h2['day_int'], h2['energy'], zorder=0)
    ex2.scatter(a2['day_int'],a2['energy'], color='red', zorder=5)
    
    ex3.set_title('MAC000044')
    ex3.plot(h3['day_int'], h3['energy'], zorder=0)
    ex3.scatter(a3['day_int'],a3['energy'], color='red', zorder=5)
        
    fig.tight_layout()
    #plt.show()
    
def plot3(df): # Plot parameters distribution

    a = df[df['anomaly_forest'] == -1]
    print()
    print(" # --- WEEK/WEEKEND --- #")
    print(a['WeekDay'].value_counts().sort_values())
    print(" # --- MONTH --- #")
    print(a['MonthOfTheYear'].value_counts().sort_values())
    print(" # --- DAY OF THE WEEK --- #")
    print(a['DayOfTheWeek'].value_counts().sort_values())

    fig, (ex1, ex2, ex3) = plt.subplots(3, figsize =(30, 6))

    barWidth = 0.30
    ww = a['WeekDay'].value_counts().sort_index().to_list()
    dw = a['DayOfTheWeek'].value_counts().sort_index().to_list()
    my = a['MonthOfTheYear'].value_counts().sort_index().to_list()
        
    colors = ["white", "whitesmoke","gainsboro",
              "lightgrey", "lightgray", "silver",
              "darkgrey", "darkgray", "grey",
              "gray", "dimgrey", "dimgray"]
    
    ww_label = ["WeakDay", "WeakEnd"]
    dw_label = [ "Monday",  "Tuesday",  "Wednesday",
                 "Thursday", "Friday", "Saturday",
                 "Sunday"]
    my_label = ["January", "February", "March",
                "April", "May", "June",
                "July", "August", "September",
                "October", "November", "December"]
        
    for i in range(0, len(ww)):
        ex1.bar(i,
                ww[i],
                color =colors[i], width = barWidth,
                edgecolor ='black', label = ww_label[i])
        
        ex1.legend(loc='upper right')
        
    for i in range(0, len(dw)):
        ex2.bar(i,
                dw[i],
                color =colors[i], width = barWidth,
                edgecolor ='black', label = dw_label[i])

        ex2.legend(loc='upper right')

    for i in range(0, len(my)):
        ex3.bar(i,
                my[i],
                color =colors[i], width = barWidth,
                edgecolor ='black', label = my_label[i])

        ex3.legend(loc='upper right')
        
    fig.tight_layout()


    

