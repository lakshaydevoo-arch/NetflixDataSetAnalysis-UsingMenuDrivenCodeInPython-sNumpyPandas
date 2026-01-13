import pandas as pd
import seaborn as sb
import matplotlib.pyplot as mpl

data = pd.read_csv("file.csv")
# As it is a large data set so it shows on printing the top 5 rows and last 5 columns
print(data)
print(data.info()) #To show indexes columns , datatypes of each column, memory at once
#ch = int(input("Enter Your Choice : "))
print("Enter 1: To get the HEAD of the dataset")
print("OR")
print("Enter 2: To check if duplicated values are present in the dataset")
print("OR")
print("Enter 3: To check if there are any NULL values present in the dataset")
print("OR")
print("Enter 4: To show all rows that have NULL values")
print("OR")
print("Enter 5: To handle/fill/remove NULL values")
print("OR")
print("Enter 6: To find the value at a specified row and column [R,C]")
print("OR")
print("Enter 7: To plot number of movies released each year (bar graph)")
print("OR")
print("Enter 8: To group movies by category/genre and see average rating")
print("OR")
print("Enter 9: To check which movies were released in the year 2000")

while(True):
    user_ch =  int(input())


    if(user_ch == 1) :      
        print(data.head())
    elif(user_ch ==2):
        print(data.duplicated()) 
        print(data[data.duplicated()])
        print("Dropping the duplicates data now!!! ")
        data.drop_duplicates(inplace=True)
        print("Now again printing the duplicates call we will get no duplicates: ")
        print(data[data.duplicated()])
    elif(user_ch ==3):
        print(data.isnull()) # when true then there is a null values
        print(data.isnull().sum()) # returns the sum of null values in every column
    elif(user_ch == 4):
        sb.heatmap(data.isnull())
        mpl.show()
    elif(user_ch ==5): # Handling null values
        data.fillna("handled")
        print(data[data.isnull()])
    elif(user_ch == 6): # To find the specified column and speciied row in a data set [R,C]
        print(data[data['Title'].isin(['House of Cards'])])
    elif(user_ch == 7):
        data['Release_Date'] = data['Release_Date'].str.strip() #Strip is needed because we have in this dataset a space beore the Release_Date
        data['Data_newdatetime'] = pd.to_datetime(data['Release_Date'])
        print(data['Data_newdatetime'].dt.year.value_counts()) # print is necessary to use with it
        print(data)
        print(data["Data_newdatetime"].dt.year.value_counts().plot(kind = "bar"))
        mpl.show() #I HAVE SHOWN HERE USING BAR GRAPH
    elif(user_ch ==8):
        #This is group by function
        print(data.groupby('Category').Category.count())# Count of movies and tv shows
        print(data.groupby('Category').Category.count().plot(kind='bar')) 
        mpl.show() # this shows all the sum of the values using bar graph
        #Plotting using seaborn library
        sb.countplot(data['Category'])
        mpl.show()
    elif(user_ch == 9):
        #This is to check which movies were released in year 2000
        data['Release_Date'] = data['Release_Date'].str.strip() #Strip is needed because we have in this dataset a space beore the Release_Date
        data['Data_newdatetime'] = pd.to_datetime(data['Release_Date'])
        print(data['Data_newdatetime'].dtype)
        data['Year'] =   data['Data_newdatetime'].dt.year
        print(data[(data['Category'] == 'Movie' ) & (data['Year'] == 2021)])
    toend = input("Do you want to see more any of the detils of the datset or not ? ")
    if(toend in 'Yy'):
        continue
    else:
        break
    