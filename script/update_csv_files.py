import pandas as pd 

def year_list(first_year, last_year):
    year_list = [str(first_year+i)+'-'+str(first_year+i+1) for i in range(last_year-first_year)]
    return year_list

def file_update(year)
    def file_update(year):
    filename = '/Users/username/csv_files/'+year+'.csv'
    df = pd.read_csv(filename)
    
    #改行文字とスペース文字を削除
    df['Player'] = df['Player'].str.replace('\n', '')
    df['Player'] = df['Player'].str.replace('\t', '')
    #列名を変更
    df_new = df.rename(columns={'\n\t\t\t\t\t\t\t'+year[:4]+'/'+year[-2:]+'\t\t\t\t\t\t': year})
    df_new = df.rename(columns={'\n\t\t\t\t\t\t\t'+year[:4]+'/'+year[-2:]+'(*)\t\t\t\t\t\t': year+'_unknown'})
    #右端のよくわからない列を削除
    df_new.drop(year+'_unknown', axis=1)
    #新しいファイルの名前にして保存
    df.to_csv('/Users/username/csv_files/'+year+'_new.csv')


if __name__ == '__main__':
    year_list = year_list(1996, 2019)
    for year in year_list:
        if year == '2016-2017':
            continue
        file_update(year)