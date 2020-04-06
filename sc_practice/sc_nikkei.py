import requests
from bs4 import BeautifulSoup

url = 'https://www.nikkei.com/markets/worldidx/'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'lxml')

table = soup.find('table','cmn-table_style1' )   #'cmn-table_style1'→これ入れないとなんだか抽出できる値の数が違う
data = table.findAll('tr')  #ここで書くデータの行を取得

dict_soba = {}
#dataから各値を抽出
for da in data:
    th = da.th
    td = da.td
    # ここが一番大事？
    # 銘柄の文字列に余計な文字や記号が入ってしまっているので整形
    # replace (a,b)はaをbに変えるという構文
    cleaned_th = th.text.replace('\xa0','').replace('※', '')
    #格納
    dict_soba[cleaned_th] = td.text

print(dict_soba)
