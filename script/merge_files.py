import numpy as np 
import pandas as pd 
import os 


def year_list(first_year, last_year):
    year_list = [str(first_year+i)+'-'+str(first_year+i+1) for i in range(last_year-first_year)]
    return year_list

def itinenbun(year, main_df):
    #main_dfから該当年の部分を抜き出す
    nukidasi = year[:5]+year[-2:]
    print(nukidasi)
    gaitou = main_df[main_df['season'] == nukidasi]
    #給料ファイルを読み込む
    salary = pd.read_csv('csv_files/'+year+'_new.csv')
    #salary_listに給料のデータを入れていく
    salary_list = []
    player = []
    for i in range(len(gaitou)):
        found = False
        for j in range(len(salary)):
            if gaitou.iloc[i].player_name == salary.iloc[j].Player and gaitou.iloc[i].player_name not in player:
                salary_list.append(salary.iloc[j]['\n\t\t\t\t\t\t\t'+year[:4]+'/'+year[-2:]+'\t\t\t\t\t\t'])
                player.append(gaitou.iloc[i].player_name)
                found = True
            if j == len(salary)-1 and found == False:
                salary_list.append(np.nan)
    #salary_listをgaitouに追加してcsv出力して終わり
    print(len(gaitou))
    print(len(salary_list))
    gaitou['salary'] = salary_list
    gaitou['salary'] = gaitou['salary'].str.replace('\n', '')
    gaitou['salary'] = gaitou['salary'].str.replace('\t', '')
    gaitou.to_csv('/Users/username/itinengoto/'+year+".csv")


if __name__ == '__main__':
    year_list = year_list(1996, 2019)
    os.mkdir('itinengoto')
    main_df = pd.read('all_seasons.csv')
    for year in year_list:
        if year == '2016-2017':
            continue
        itinenbun(year, main_df)