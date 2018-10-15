import pandas as pd

df = pd.read_csv("code_7974.csv", header=0)
df.columns=["Date", "Close", "Open", "High", "Low", "Volume", "Percent"]
df["index"] = [i for i in range(len(df))]
print(df.head(10))

etf_list = [1305,#ダイワ 上場投信-トピックス
            1306,#TOPIX連動型上場投資信託
            1308,#上場インデックスファンドTOPIX
            1320,#ダイワ 上場投信-日経225
            1321,#日経225連動型上場投資信託
            1330,#上場インデックスファンド225
            #1610,#ダイワ 上場投信-東証電気機器株価指数
            #1613,#東証電気機器株価指数連動型上場投資信託
            #1624,#(NEXT FUNDS)機械上場投信
            #1625,#(NEXT FUNDS)電機･精密上場投信
            #1641,#ダイワ 上場投信･TOPIX-17機械
            #1642,#ダイワ 上場投信･TOPIX-17電機･精密
            2038,#NEXT NOTES 日経・TOCOM 原油 ダブル・ブル ETN
            ]

for etf in etf_list:
    print(etf)
    df_etf = pd.read_csv("etf_" + str(etf) + ".csv", header=0)
    df_etf.columns = ["Date", "Close", "Open", "High", "Low", "Volume", "Percent"]
        
    dates = []
    closeis = []
    percents = []
    
    for d in df["Date"]:
        date = df_etf.loc[(df_etf.Date == d), "Date"]#任天堂の日付をETFファイルから検索
        yesterday_date = date.values[0]
        dates.append(date.values[0])#日付をデータセットに追加
            
        close = df_etf.loc[(df_etf.Date == d), "Close"]#日付が一致した日のETFのCloseのデータを取り出す
        percent = df_etf.loc[(df_etf.Date == d), "Percent"]
        
        if str(close.values[0]) != str("nan"):#取り出したCloseがnanでないかを判断
            yesterday_close = close.values[0]
            closeis.append(close.values[0])
        
        else:
            closeis.append(yesterday_close)
        
        if str(percent.values[0]) != str("nan"):#取り出したCloseがnanでないかを判断
            yesterday_percent = percent.values[0]
            percents.append(percent.values[0])
        
        else:
            percents.append(yesterday_percent)
                
    df_etf2 = pd.DataFrame({"Date_" + str(etf) : dates, "Close_" + str(etf) : closeis,"Percent_" + str(etf) : percents})#新しくデータフレームを作成
    df = pd.concat([df, df_etf2], axis=1)#任天堂のデータとETFデータを統合

df.to_csv("code_7974_plus.csv")
