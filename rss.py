from pymongo import MongoClient
import feedparser

Client = MongoClient()
db = Client["RSS"]
collection = db["Feeds"]
feed = feedparser.parse('http://www.amarujala.com/rss/national-news.xml')
feed1 = feedparser.parse('http://www.amarujala.com/rss/india.xml')
feed2 = feedparser.parse('http://www.amarujala.com/rss/india.xml')
feed3 = feedparser.parse('http://www.amarujala.com/rss/sports-news.xml')
feed4 = feedparser.parse('http://www.amarujala.com/rss/business.xml')
feed5 = feedparser.parse('http://www.amarujala.com/rss/technology-news.xml')
feed6 = feedparser.parse('http://www.amarujala.com/rss/automobiles-news.xml')
feed7 = feedparser.parse('http://www.amarujala.com/rss/entertainment.xml')
feed8 = feedparser.parse('http://www.amarujala.com/rss/lifestyle-news.xml')
feed9 = feedparser.parse('http://www.amarujala.com/rss/spirituality-news.xml')
feed10 = feedparser.parse('http://www.amarujala.com/rss/astrology-news.xml')
feed11 = feedparser.parse('http://www.amarujala.com/rss/jobs.xml')
feed12 = feedparser.parse('http://www.amarujala.com/rss/uttar-pradesh-news.xml')
feed13 = feedparser.parse('http://www.amarujala.com/rss/uttarakhand-news.xml')
feed14 = feedparser.parse('http://www.amarujala.com/rss/himachal-pradesh-news.xml')
feed15 = feedparser.parse('http://www.amarujala.com/rss/delhi-news.xml')
feed16 = feedparser.parse('http://www.amarujala.com/rss/jammu-news.xml')
feed17 = feedparser.parse('http://www.amarujala.com/rss/punjab-news.xml')
feed18 = feedparser.parse('http://www.amarujala.com/rss/haryana-news.xml')
feed19 = feedparser.parse('http://www.amarujala.com/rss/bihar-news.xml')
feed20 = feedparser.parse('http://www.amarujala.com/rss/chhattisgarh-news.xml')
feed21 = feedparser.parse('http://www.amarujala.com/rss/madhya-pradesh-news.xml')
feed22 = feedparser.parse('http://www.amarujala.com/rss/rajasthan-news.xml')
feed23 = feedparser.parse('http://www.amarujala.com/rss/jharkhand-news.xml')
feed24 = feedparser.parse('http://www.amarujala.com/rss/allahabad-news.xml')
feed25 = feedparser.parse('http://www.amarujala.com/rss/agra-news.xml')
feed26 = feedparser.parse('http://www.amarujala.com/rss/ambala-news.xml')
feed27 = feedparser.parse('http://www.amarujala.com/rss/chandigarh-news.xml')
feed28 = feedparser.parse('http://www.amarujala.com/rss/delhi-news.xml')
feed29 = feedparser.parse('http://www.amarujala.com/rss/gurgaon-news.xml')
feed30 = feedparser.parse('http://www.amarujala.com/rss/haridwar-news.xml')
feed31 = feedparser.parse('http://www.amarujala.com/rss/jalandhar-news.xml')
feed32 = feedparser.parse('http://www.amarujala.com/rss/jammu-news.xml')
feed33 = feedparser.parse('http://www.amarujala.com/rss/kanpur-news.xml') 
feed34 = feedparser.parse('http://www.amarujala.com/rss/shimla-news.xml')
for i in feed['items']:
	feeds = {'a':i["title"],'b':i["description"]}
	db.collection.insert(feeds)
	print(feeds)
for i in feed1['items']:
	feeds1 = {'a1':i["title"],'b1':i["description"]}
	db.collection.insert(feeds1)
	print(feeds1)
for i in feed2['items']:
	feeds2 = {'a2':i["title"],'b2':i["description"]}
	db.collection.insert(feeds2)
	print(feeds2)
for i in feed3['items']:
	feeds3 = {'a3':i["title"],'b3':i["description"]}
	db.collection.insert(feeds3)
	print(feeds3)
for i in feed4['items']:
	feeds4 = {'a4':i["title"],'b4':i["description"]}
	db.collection.insert(feeds4)
	print(feeds4)
for i in feed5['items']:
	feeds5 = {'a5':i["title"],'b5':i["description"]}
	db.collection.insert(feeds5)
	print(feeds5)
for i in feed6['items']:
	feeds6 = {'a6':i["title"],'b6':i["description"]}
	db.collection.insert(feeds6)
	print(feeds6)
for i in feed7['items']:
	feeds7 = {'a7':i["title"],'b7':i["description"]}
	db.collection.insert(feeds7)
	print(feeds7)
for i in feed8['items']:
	feeds8 = {'a8':i["title"],'b8':i["description"]}
	db.collection.insert(feeds8)
	print(feeds8)
for i in feed9['items']:
	feeds9 = {'a9':i["title"],'b9':i["description"]}
	db.collection.insert(feeds9)
	print(feeds9)
for i in feed10['items']:
	feeds10 = {'a10':i["title"],'b10':i["description"]}
	db.collection.insert(feeds10)
	print(feeds10)
for i in feed11['items']:
	feeds11 = {'a11':i["title"],'b11':i["description"]}
	db.collection.insert(feeds11)
	print(feeds11)
for i in feed12['items']:
	feeds12 = {'a12':i["title"],'b12':i["description"]}
	db.collection.insert(feeds12)
	print(feeds12)
for i in feed13['items']:
	feeds13 = {'a13':i["title"],'b13':i["description"]}
	db.collection.insert(feeds13)
	print(feeds13)
for i in feed14['items']:
	feeds14 = {'a14':i["title"],'b14':i["description"]}
	db.collection.insert(feeds14)
	print(feeds14)
for i in feed15['items']:
	feeds15 = {'a15':i["title"],'b15':i["description"]}
	db.collection.insert(feeds15)
	print(feeds15)
for i in feed16['items']:
	feeds16 = {'a16':i["title"],'b16':i["description"]}
	db.collection.insert(feeds16)
	print(feeds16)
for i in feed17['items']:
	feeds17 = {'a17':i["title"],'b17':i["description"]}
	db.collection.insert(feeds17)
	print(feeds17)
for i in feed18['items']:
	feeds18 = {'a18':i["title"],'b18':i["description"]}
	db.collection.insert(feeds18)
	print(feeds18)
for i in feed19['items']:
	feeds19 = {'a19':i["title"],'b19':i["description"]}
	db.collection.insert(feeds19)
	print(feeds19)
for i in feed20['items']:
	feeds20 = {'a20':i["title"],'b20':i["description"]}
	db.collection.insert(feeds20)
	print(feeds20)
for i in feed21['items']:
	feeds21 = {'a21':i["title"],'b21':i["description"]}
	db.collection.insert(feeds21)
	print(feeds21)
for i in feed22['items']:
	feeds22 = {'a22':i["title"],'b22':i["description"]}
	db.collection.insert(feeds22)
	print(feeds22)
for i in feed23['items']:
	feeds23 = {'a23':i["title"],'b23':i["description"]}
	db.collection.insert(feeds23)
	print(feeds23)
for i in feed24['items']:
	feeds24 = {'a24':i["title"],'b24':i["description"]}
	db.collection.insert(feeds24)
	print(feeds24)
for i in feed25['items']:
	feeds25 = {'a25':i["title"],'b25':i["description"]}
	db.collection.insert(feeds25)
	print(feeds25)
for i in feed26['items']:
	feeds26 = {'a26':i["title"],'b26':i["description"]}
	db.collection.insert(feeds26)
	print(feeds26)
for i in feed27['items']:
	feeds27 = {'a27':i["title"],'b27':i["description"]}
	db.collection.insert(feeds27)
	print(feeds27)
for i in feed29['items']:
	feeds28 = {'a28':i["title"],'b28':i["description"]}
	db.collection.insert(feeds28)
	print(feeds28)
for i in feed30['items']:
	feeds30 = {'a30':i["title"],'b30':i["description"]}
	db.collection.insert(feeds30)
	print(feeds30)
for i in feed31['items']:
	feeds31 = {'a31':i["title"],'b31':i["description"]}
	db.collection.insert(feeds31)
	print(feeds31)
for i in feed32['items']:
	feeds32 = {'a32':i["title"],'b32':i["description"]}
	db.collection.insert(feeds32)
	print(feeds32)
for i in feed33['items']:
	feeds33 = {'a33':i["title"],'b33':i["description"]}
	db.collection.insert(feeds33)
	print(feeds33)
for i in feed34['items']:
	feeds34 = {'a34':i["title"],'b34':i["description"]}
	db.collection.insert(feeds34)
	print(feeds34)
	




