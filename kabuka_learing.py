import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

df = pd.read_csv("code_7974_plus.csv")
df = df.sort_values(by=["index"], ascending=False)
print(df.tail(20))

df = df.iloc[0:len(df) - 1]
print(df.tail())

df_train = df.iloc[0:len(df)-1]
df_test  = df.iloc[len(df)-1:len(df)]

xlist = ["Percent_1305",
         "Percent_1306",
         "Percent_1308",
         "Percent_1320",
         "Percent_1321",
         "Percent_1330",
         "Percent_2038",
         ]

x_train = []
y_train = []
for s in range(0, len(df_train) -1):
  
    x_train.append(df_train[xlist].iloc[s])

    if df_train["Close"].iloc[s + 1] > df_train["Close"].iloc[s]:
        y_train.append(1)
    else:
        y_train.append(-1)

rf = RandomForestClassifier(n_estimators=len(x_train), random_state=0)
rf.fit(x_train, y_train)

test_x = df_test[xlist].iloc[0]
test_y = rf.predict(test_x.values.reshape(1, -1))

print("result : ", test_y[0])
