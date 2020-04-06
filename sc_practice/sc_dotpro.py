# このように書くと、特定の関数のみimport出来ます。
from bs4 import BeautifulSoup

html = '''\
<html>
<body>
  <h1 class="class1">Hello, world</h1>
  <h2>This is Dot-pro</h2>
  <p class="class2">Mac</p>
  <p class="class2">Windows</p>
  <p class="class2">Linux</p>
  <a class="class3" href="http://foo.com">こちらをクリック！</a>
</body>
</html>\
        '''

# htmlをbeautifulsoupオブジェクトにする
soup = BeautifulSoup(html)

'''
要素へのアクセス
---------------
findメソッドを使用します
役割：該当する要素１つを返す。
  find(要素, クラス)
第二引数のクラス名に関しては必須ではありませんが、クラスでパースしたい場合には必要です。
'''
h1 = soup.find('h1', 'class1')
# htmlのタグも含めたオブジェクト
print(h1)
# テキストのみを抽出
print(h1.text)

'''
複数欲しい要素がある場合
----------------------
findAllメソッドを使用します
役割：該当する要素全てをリストのオブジェクトとして返す
  findAll(要素, クラス)

リストに対して `.text` プロパティを使用することは出来ないので、
リストの要素それぞれに対して処理をしてあげる必要があります。
'''
p_tags = soup.findAll('p', 'class1')
for p_tag in p_tags:
  print(p_tag.text)

'''
リンクをパースする場合
---------------------
aタグをパースし、getメソッドにて`href`を指定します。
'''
a = soup.find('a', 'class3')
link = a.get('href')
print(link)
