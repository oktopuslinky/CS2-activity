import pandas as pd
import csv

#https://cmdlinetips.com/2020/03/save-a-pandas-data-frame-as-csv-file/

excel_sheet = "Best_50_movies_of_all_time.xlsx"

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
    
    print(the_data)
    return the_data
    
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
        
    print(the_rankings)

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

    print(df)
    return df, the_rankings, the_names, the_years, the_directors, the_countries

def create_tsv(df):
    df.to_csv("movie_data.tsv", sep="\t")



df = create_df_from_xlsx(excel_sheet)
convert_df_csv(df)
the_data = convert_csv_list()
df, the_rankings, the_names, the_years, the_directors, the_countries = create_updated_df(the_data)
create_tsv(df)