# coding: UTF-8
import csv
import requests, bs4

# 認証プロキシ環境下での設定
proxy_dict = {
    "http": "http://ctwc0156:3Er6ede9@proxy.doshisha.ac.jp:8080/",
    "https": "http://ctwc0156:3Er6ede9@proxy.doshisha.ac.jp:8080/"
}

#2018年の任天堂の株価csvファイルの作成
csvFile = open("7974_kabuka.csv", 'w', newline = '', encoding = 'utf-8')
writer = csv.writer(csvFile)
writer.writerow(['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])

#URLのリスト
urls = ['https://96ut.com/stock/jikei.php?code=7974&year=2018',
        'https://96ut.com/stock/jikei.php?code=7974&year=2017',
        'https://96ut.com/stock/jikei.php?code=7974&year=2016',
        'https://96ut.com/stock/jikei.php?code=7974&year=2015',
        'https://96ut.com/stock/jikei.php?code=7974&year=2014',
        'https://96ut.com/stock/jikei.php?code=7974&year=2013',
        'https://96ut.com/stock/jikei.php?code=7974&year=2012',
        'https://96ut.com/stock/jikei.php?code=7974&year=2011'
        ]

#Webページを取得
for url in urls:
    res = requests.get(url, proxies=proxy_dict)
    #BeautifulSoupオブジェクトに変換
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    
    #テーブルを指定
    table = soup.findAll("table",{"class":"kuro"})[0]
    rows = table.findAll("tr")
    
    csvFile = open("7974_kabuka.csv", 'a', newline = '', encoding = 'utf-8')
    writer = csv.writer(csvFile)
    
    try:
        for row in rows:
            csvRow = []
            for cell in row.findAll(['td', 'th']):
                csvRow.append(cell.get_text())
            #株価テーブルの日本語の列を排除
            if "日付" in csvRow:
                pass
            else:
                writer.writerow(csvRow)
    finally:
        csvFile.close()
