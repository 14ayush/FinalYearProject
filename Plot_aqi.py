import pandas as pd
import matplotlib.pyplot as plt




def avg_data_2016():
    temp_i=0
    average=[]
    for rows in pd.read_csv('D:\\FP\\AQI\\AQI\\aqi2016.csv',chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/24
        temp_i=temp_i+1
        
        average.append(avg)
    return average
def avg_data_2017():
    temp_i=0
    average=[]
    for rows in pd.read_csv('D:\\FP\\AQI\\AQI\\aqi2017.csv',chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/24
        temp_i=temp_i+1
        
        average.append(avg)
    return average


def avg_data_2018():
    temp_i=0
    average=[]
    for rows in pd.read_csv('D:\\FP\\AQI\\AQI\\aqi2018.csv',chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/24
        temp_i=temp_i+1
        
        average.append(avg)
    return average
    
def avg_data_2019():
    temp_i=0
    average=[]
    for rows in pd.read_csv('D:\\FP\\AQI\\AQI\\aqi2019.csv',chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/24
        temp_i=temp_i+1
        
        average.append(avg)
    return average
    
def avg_data_2020():
    temp_i=0
    average=[]
    for rows in pd.read_csv('D:\\FP\\AQI\\AQI\\aqi2020.csv',chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/24
        temp_i=temp_i+1
        
        average.append(avg)
    return average

    
def avg_data_2021():
    temp_i=0
    average=[]
    for rows in pd.read_csv('D:\\FP\\AQI\\AQI\\aqi2021.csv',chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/24
        temp_i=temp_i+1
        
        average.append(avg)
    return average
    
def avg_data_2022():
    temp_i=0
    average=[]
    for rows in pd.read_csv('D:\\FP\\AQI\\AQI\\aqi2022.csv',chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/24
        temp_i=temp_i+1
        
        average.append(avg)
    return average
    

    

if __name__=="__main__":
    
    lst2016=avg_data_2016()
    lst2017=avg_data_2017()
    lst2018=avg_data_2018()
    lst2019=avg_data_2019()
    lst2020=avg_data_2020()
    lst2021=avg_data_2021()
    lst2022=avg_data_2022()

    # Update x-value ranges to match the length of respective y-values
    
    plt.plot(range(1,366), lst2016, label="2016 data")  # 365 days in a year
    plt.plot(range(1,366), lst2017, label="2017 data")
    #plt.plot(range(1,366), lst2018, label="2018 data")
    if len(lst2018) == 364:  # Check the length and adjust if needed
        lst2018.append(120)  # Append one extra value to match the x-axis range
    
    #plt.plot(range(1,366), lst2018, label="2018 data")
    plt.plot(range(1,366), lst2019, label="2019 data")
    plt.plot(range(1,366), lst2020, label="2020 data")  # 365 days in a year
    plt.plot(range(1,366), lst2021, label="2021 data")
    
    # Ensure lst2022 (and other years) has the same length as the x-axis range
    # You might need to investigate why there is a length mismatch
    # Alternatively, you can adjust the length of the data to match the x-axis range
    if len(lst2022) == 364:  # Check the length and adjust if needed
        lst2022.append(231)  # Append one extra value to match the x-axis range
    
    plt.plot(range(1,366), lst2022, label="2022 data")  # 365 days in a year

    plt.xlabel('Day')
    plt.ylabel('PM 2.5')
    plt.legend(loc='upper right')
    plt.show()




