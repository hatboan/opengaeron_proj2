import pandas as pd

data = pd.read_csv('2019_kbo_for_kaggle_v2.csv')

d15 = data[data['year']==2015]
d16 = data[data['year']==2016]
d17 = data[data['year']==2017]
d18 = data[data['year']==2018]
d15h = d15.sort_values(by='H', ascending=False)
d15avg = d15.sort_values(by='avg', ascending=False)
d15hr = d15.sort_values(by='HR', ascending=False)
d15obp = d15.sort_values(by='OBP', ascending=False)
com15 = pd.DataFrame({
    '15_H': d15h.iloc[:10]['batter_name'].tolist(),
    '15_Avg': d15avg.iloc[:10]['batter_name'].tolist(),
    '15_HR': d15hr.iloc[:10]['batter_name'].tolist(),
    '15_OBP': d15obp.iloc[:10]['batter_name'].tolist()
})
print(com15)

d16h = d16.sort_values(by='H', ascending=False)
d16avg = d16.sort_values(by='avg', ascending=False)
d16hr = d16.sort_values(by='HR', ascending=False)
d16obp = d16.sort_values(by='OBP', ascending=False)
com16 = pd.DataFrame({
    '16_H': d16h.iloc[:10]['batter_name'].tolist(),
    '16_Avg': d16avg.iloc[:10]['batter_name'].tolist(),
    '16_HR': d16hr.iloc[:10]['batter_name'].tolist(),
    '16_OBP': d16obp.iloc[:10]['batter_name'].tolist()
})
print(com16)

d17h = d17.sort_values(by='H', ascending=False)
d17avg = d17.sort_values(by='avg', ascending=False)
d17hr = d17.sort_values(by='HR', ascending=False)
d17obp = d17.sort_values(by='OBP', ascending=False)
com17 = pd.DataFrame({
    '17_H': d17h.iloc[:10]['batter_name'].tolist(),
    '17_Avg': d17avg.iloc[:10]['batter_name'].tolist(),
    '17_HR': d17hr.iloc[:10]['batter_name'].tolist(),
    '17_OBP': d17obp.iloc[:10]['batter_name'].tolist()
})
print(com17)

d18h = d18.sort_values(by='H', ascending=False)
d18avg = d18.sort_values(by='avg', ascending=False)
d18hr = d18.sort_values(by='HR', ascending=False)
d18obp = d18.sort_values(by='OBP', ascending=False)
com18 = pd.DataFrame({
    '18_H': d18h.iloc[:10]['batter_name'].tolist(),
    '18_Avg': d18avg.iloc[:10]['batter_name'].tolist(),
    '18_HR': d18hr.iloc[:10]['batter_name'].tolist(),
    '18_OBP': d18obp.iloc[:10]['batter_name'].tolist()
})
print(com18)

d18war = d18.sort_values(by='war',ascending=False)
d18war_1 = d18war[d18war['cp'] == '포수']
d18war_2 = d18war[d18war['cp'] == '1루수']
d18war_3 = d18war[d18war['cp'] == '2루수']
d18war_4 = d18war[d18war['cp'] == '3루수']
d18war_5 = d18war[d18war['cp'] == '유격수']
d18war_6 = d18war[d18war['cp'] == '좌익수']
d18war_7 = d18war[d18war['cp'] == '중견수']
d18war_8 = d18war[d18war['cp'] == '우익수']
com18_high_war = pd.DataFrame({
    '포수': d18war_1[:1]['batter_name'].tolist(),
    '1루수': d18war_2[:1]['batter_name'].tolist(),
    '2루수': d18war_3[:1]['batter_name'].tolist(),
    '3루수': d18war_4[:1]['batter_name'].tolist(),
    '유격수': d18war_5[:1]['batter_name'].tolist(),
    '좌익수': d18war_6[:1]['batter_name'].tolist(),
    '중견수': d18war_7[:1]['batter_name'].tolist(),
    '우익수': d18war_8[:1]['batter_name'].tolist()
})
print(com18_high_war)

d_num = data[['R','H','HR','RBI','SB','war','avg','OBP','SLG','salary']]
d_corr = d_num.corrwith(d_num.salary)
d_corr_sort = d_corr.sort_values(ascending=False)
print(d_corr_sort)
d_corr_1 = d_corr_sort[1:2]
print("\n" + d_corr_1.index[0] + " has the highest correlation with salary")