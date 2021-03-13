import pandas as pd
import csv
import matplotlib.pyplot as plt
from prettytable import PrettyTable


def create_df_from_xlsx(excel_sheet):
    data_xlsx = pd.read_excel(excel_sheet, 'Sheet1', index_col=None)
    df = data_xlsx.replace('\n', ' ',regex=True)

    return df

def convert_df_csv(df):
    df.to_csv('fileTSV.csv', sep='\t', encoding='utf-8',  index=False, line_terminator='\r\n')

def convert_csv_list():
    csv_file = open("fileTSV.csv")
    read_csv = csv.reader(csv_file, delimiter="\t")

    #fix up xlsx data
    #convert csv to list
    the_data = list()
    for row in read_csv:
        the_data.append(row)

    the_data[0][0] = ''

    for index, item in enumerate(the_data):
        item.remove(item[0])
        the_data[index] = item

    the_data[0][1] = "Citizen Kane"

    return the_data

def create_table(the_data):
    movies = PrettyTable()
    movies.field_names = ["Ranking", "Name", "Year", "Director", "Country"]
    movies.add_rows(the_data)
    print(movies)

def create_updated_df(the_data):
    the_rankings = list()
    the_names = list()
    the_years = list()
    the_directors = list()
    the_countries = list()

    #create lists of each column
    for ranking, name, year, director, country in the_data:
        the_rankings.append(ranking)
        the_names.append(name)
        the_years.append(year)
        the_directors.append(director)
        the_countries.append(country)
        
    #create updated DataFrame

    df = pd.DataFrame(
        {
            "Ranking": the_rankings,
            "Name": the_names,
            "Year": the_years,
            "Director": the_directors,
            "Country": the_countries
        }
    )

    return df, the_rankings, the_names, the_years, the_directors, the_countries

def create_tsv(df):
    df.to_csv("movie_data.tsv", sep="\t")

def convert_list_data_int(the_list):
    int_list = list()
    for an_item in the_list:
        int_list.append(int(an_item))

    return int_list

def graph(the_years, the_rankings):
    years_int = convert_list_data_int(the_years)
    rankings_int = convert_list_data_int(the_rankings)

    plt.scatter(years_int, rankings_int)
    plt.xlabel("The Year of Release")
    plt.ylabel("Ranking")
    plt.title("Best 50 Movies of All Time")
    plt.show()

excel_sheet = "Best_50_movies_of_all_time.xlsx"

df = create_df_from_xlsx(excel_sheet)
convert_df_csv(df)
the_data = convert_csv_list()
create_table(the_data)
df, the_rankings, the_names, the_years, the_directors, the_countries = create_updated_df(the_data)
create_tsv(df)

graph(the_years, the_rankings)