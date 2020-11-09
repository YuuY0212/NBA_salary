import requests
from bs4 import BeautifulSoup
import csv
import time
#hoopshypeのページから選手の給料をスクレイピングして１年ごとにcsvファイルに保存する
base_year = 1990
last_year = 2019


def year_list(base_year, last_year):
    gap = last_year - base_year
    year_list = [str(base_year+i)+'-'+str(base_year+i+1)+'/' for i in range(gap)]
    return year_list


def main(year_list):
    for year in year_list:
        get_and_save(year)
        time.sleep(10)
        print('1年分終了しました')


def get_and_save(year):
    url = "https://hoopshype.com/salaries/players/" + year
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    tables = soup.find_all('tr')
    data_list = [[item.text for item in row.find_all('td')] for row in tables]
    file_name = year[:9] + '.csv'
    with open(file_name, 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(data_list)

if __name__ == "__main__":
    year_list = year_list(base_year, last_year)
    main(year_list)
