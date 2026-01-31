import pandas as pd
import seaborn as sb
import matplotlib.pyplot as mpl

# ------------------- Load Data ------------------- #
def load_data(file_path):
    data = pd.read_csv(file_path)
    print("Data Loaded Successfully!\n")
    print(data.head())
    print(data.info())
    return data

# ------------------- Basic Plots ------------------- #
def plot_numeric_columns(data):
    numeric_cols = data.select_dtypes(include=['number']).columns
    if len(numeric_cols) < 2:
        print("Not enough numeric columns to plot!")
        return
    
    x = numeric_cols[0]
    y = numeric_cols[1]

    # 1. Line Plot
    mpl.figure(figsize=(8,4))
    mpl.plot(data[x], data[y], marker='o')
    mpl.title(f"Line Plot of {x} vs {y}")
    mpl.xlabel(x)
    mpl.ylabel(y)
    mpl.show()

    # 2. Bar Plot
    mpl.figure(figsize=(8,4))
    mpl.bar(data[x], data[y])
    mpl.title(f"Bar Plot of {x} vs {y}")
    mpl.xlabel(x)
    mpl.ylabel(y)
    mpl.show()

    # 3. Histogram
    mpl.figure(figsize=(8,4))
    mpl.hist(data[y], bins=10, color='skyblue', edgecolor='black')
    mpl.title(f"Histogram of {y}")
    mpl.xlabel(y)
    mpl.ylabel("Frequency")
    mpl.show()

    # 4. Heatmap
    mpl.figure(figsize=(8,6))
    sb.heatmap(data[numeric_cols].corr(), annot=True, cmap="coolwarm")
    mpl.title("Correlation Heatmap")
    mpl.show()

# ------------------- Dataset Operations ------------------- #
def show_head(data):
    print(data.head())

def check_duplicates(data):
    print(data.duplicated())
    print(data[data.duplicated()])
    print("Dropping duplicate rows...")
    data.drop_duplicates(inplace=True)
    print("Duplicates removed.")
    print(data[data.duplicated()])

def check_nulls(data):
    print(data.isnull())
    print(data.isnull().sum())

def plot_nulls_heatmap(data):
    sb.heatmap(data.isnull())
    mpl.show()

def handle_nulls(data):
    data.fillna("handled", inplace=True)
    print("Nulls handled.")
    print(data[data.isnull()])

def find_row_by_title(data, title):
    print(data[data['Title'].isin([title])])

def movies_per_year(data):
    data['Release_Date'] = data['Release_Date'].str.strip()
    data['Data_newdatetime'] = pd.to_datetime(data['Release_Date'])
    print(data['Data_newdatetime'].dt.year.value_counts())
    data['Data_newdatetime'].dt.year.value_counts().plot(kind="bar")
    mpl.show()

def group_by_category(data):
    print(data.groupby('Category').Category.count())
    data.groupby('Category').Category.count().plot(kind='bar')
    mpl.show()
    sb.countplot(data['Category'])
    mpl.show()

def movies_in_year(data, year):
    data['Release_Date'] = data['Release_Date'].str.strip()
    data['Data_newdatetime'] = pd.to_datetime(data['Release_Date'])
    data['Year'] = data['Data_newdatetime'].dt.year
    print(data[(data['Category'] == 'Movie') & (data['Year'] == year)])


def main():
    file_path = "file.csv"
    data = load_data(file_path)
    
    while True:
        print("Menu Options:")
        print("1: Show HEAD of dataset")
        print("2: Check duplicates")
        print("3: Check for NULL values")
        print("4: Show NULL values heatmap")
        print("5: Handle NULL values")
        print("6: Find row by Title")
        print("7: Plot movies per year")
        print("8: Group by Category")
        print("9: Movies released in a specific year")
        print("10: Plot numeric columns overview")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            show_head(data)
        elif choice == 2:
            check_duplicates(data)
        elif choice == 3:
            check_nulls(data)
        elif choice == 4:
            plot_nulls_heatmap(data)
        elif choice == 5:
            handle_nulls(data)
        elif choice == 6:
            title = input("Enter the Title to search: ")
            find_row_by_title(data, title)
        elif choice == 7:
            movies_per_year(data)
        elif choice == 8:
            group_by_category(data)
        elif choice == 9:
            year = int(input("Enter the year to search for movies: "))
            movies_in_year(data, year)
        elif choice == 10:
            plot_numeric_columns(data)
        else:
            print("Invalid choice!")

        cont = input("Do you want to continue? (Y/N): ")
        if cont.lower() != 'y':
            break

if __name__ == "__main__":
    main()
