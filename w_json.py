import urllib.request as req
import datetime
import time
import schedule

# URLや保存ファイル名を指定
url01 = "https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json"  #東京
url02 = "https://www.jma.go.jp/bosai/forecast/data/forecast/040000.json"  #宮城県
url03 = "https://www.jma.go.jp/bosai/forecast/data/forecast/230000.json"  #愛知県
url04 = "https://www.jma.go.jp/bosai/forecast/data/forecast/270000.json"  #大阪府
url05 = "https://www.jma.go.jp/bosai/forecast/data/forecast/390000.json"  #高知県
url06 = "https://www.jma.go.jp/bosai/forecast/data/forecast/460100.json"  #鹿児島県
url07 = "https://www.jma.go.jp/bosai/forecast/data/forecast/400000.json"  #福岡県
url08 = "https://www.jma.go.jp/bosai/forecast/data/forecast/340000.json"  #広島県
url09 = "https://www.jma.go.jp/bosai/forecast/data/forecast/170000.json"  #石川県
url10 = "https://www.jma.go.jp/bosai/forecast/data/forecast/150000.json"  #新潟県

def job():
    filename01 = 'tenki01.json'
    filename02 = 'tenki02.json'
    filename03 = 'tenki03.json'
    filename04 = 'tenki04.json'
    filename05 = 'tenki05.json'
    filename06 = 'tenki06.json'
    filename07 = 'tenki07.json'
    filename08 = 'tenki08.json'
    filename09 = 'tenki09.json'
    filename10 = 'tenki10.json'
    # ダウンロード
    req.urlretrieve(url01, filename01)
    req.urlretrieve(url02, filename02)
    req.urlretrieve(url03, filename03)
    req.urlretrieve(url04, filename04)
    req.urlretrieve(url05, filename05)
    req.urlretrieve(url06, filename06)
    req.urlretrieve(url07, filename07)
    req.urlretrieve(url08, filename08)
    req.urlretrieve(url09, filename09)
    req.urlretrieve(url10, filename10)
    # req.urlretrieve(url08, filename08)

def job01():
    print(datetime.datetime.now())

schedule.every(720).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

