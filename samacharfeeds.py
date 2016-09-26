from pymongo import MongoClient
import feedparser

Client = MongoClient()
db = Client["Samachar"]
collection = ["Feeds"]
feed1 = feedparser.parse('http://www.samacharjagat.com/rss/auto')
feed2 = feedparser.parse('http://www.samacharjagat.com/rss/business')
feed3 = feedparser.parse('http://www.samacharjagat.com/rss/career')
feed4 = feedparser.parse('http://www.samacharjagat.com/rss/cartoons')
feed5 = feedparser.parse('http://www.samacharjagat.com/rss/city')
feed6 = feedparser.parse('http://www.samacharjagat.com/rss/current-affair')
feed7 = feedparser.parse('http://www.samacharjagat.com/rss/day-special')
feed8 = feedparser.parse('http://www.samacharjagat.com/rss/entertainment')
feed9 = feedparser.parse('http://www.samacharjagat.com/rss/health')
feed10 = feedparser.parse('http://www.samacharjagat.com/rss/international')
feed11 = feedparser.parse('http://www.samacharjagat.com/rss/jokes')
feed12 = feedparser.parse('http://www.samacharjagat.com/rss/jyotish')
feed13 = feedparser.parse('http://www.samacharjagat.com/rss/lifestyle')
feed14 = feedparser.parse('http://www.samacharjagat.com/rss/national')
feed15 = feedparser.parse('http://www.samacharjagat.com/rss/offbeat')
feed16 = feedparser.parse('http://www.samacharjagat.com/rss/olympic')
feed17 = feedparser.parse('http://www.samacharjagat.com/rss/opinion')
feed18 = feedparser.parse('http://www.samacharjagat.com/rss/recipes')
feed19 = feedparser.parse('http://www.samacharjagat.com/rss/religion')
feed20 = feedparser.parse('http://www.samacharjagat.com/rss/social-media')
feed21 = feedparser.parse('http://www.samacharjagat.com/rss/sports')
feed22 = feedparser.parse('http://www.samacharjagat.com/rss/technology-gadgets')
feed23 = feedparser.parse('http://www.samacharjagat.com/rss/travel')
feed24 = feedparser.parse('http://www.samacharjagat.com/rss/zara-hat-ke')
for i in feed1['items']:
	feeds1 = {'a1':i["title"],'b1':i["description"],'c1':i["summary"]}
	db.collection.insert(feeds1)
	print(feeds1)
for i in feed2['items']:
	feeds2 = {'a2':i["title"],'b2':i["description"],'c2':i["summary"]}
	db.collection.insert(feeds2)
	print(feeds2)
for i in feed3['items']:
	feeds3 = {'a3':i["title"],'b3':i["description"],'c3':i["summary"]}
	db.collection.insert(feeds3)
	print(feeds3)
for i in feed4['items']:
	feeds4 = {'a4':i["title"],'b4':i["description"],'c4':i["summary"]}
	db.collection.insert(feeds4)
	print(feeds4)
for i in feed5['items']:
	feeds5 = {'a5':i["title"],'b5':i["description"],'c5':i["summary"]}
	db.collection.insert(feeds5)
	print(feeds5)
for i in feed6['items']:
	feeds6 = {'a6':i["title"],'b6':i["description"],'c6':i["summary"]}
	db.collection.insert(feeds6)
	print(feeds6)
for i in feed7['items']:
	feeds7 = {'a7':i["title"],'b7':i["description"],'c7':i["summary"]}
	db.collection.insert(feeds7)
	print(feeds7)
for i in feed8['items']:
	feeds8 = {'a8':i["title"],'b8':i["description"],'c8':i["summary"]}
	db.collection.insert(feeds8)
	print(feeds8)
for i in feed9['items']:
	feeds9 = {'a9':i["title"],'b9':i["description"],'c9':i["summary"]}
	db.collection.insert(feeds9)
	print(feeds9)
for i in feed10['items']:
	feeds10 = {'a10':i["title"],'b10':i["description"],'c10':i["summary"]}
	db.collection.insert(feeds10)
	print(feeds10)
for i in feed11['items']:
	feeds11 = {'a11':i["title"],'b11':i["description"],'c11':i["summary"]}
	db.collection.insert(feeds11)
	print(feeds11)
for i in feed12['items']:
	feeds12 = {'a12':i["title"],'b12':i["description"],'c12':i["summary"]}
	db.collection.insert(feeds12)
	print(feeds12)
for i in feed13['items']:
	feeds13 = {'a13':i["title"],'b13':i["description"],'c13':i["summary"]}
	db.collection.insert(feeds13)
	print(feeds13)
for i in feed14['items']:
	feeds14 = {'a14':i["title"],'b14':i["description"],'c14':i["summary"]}
	db.collection.insert(feeds14)
	print(feeds14)
for i in feed15['items']:
	feeds15 = {'a15':i["title"],'b15':i["description"],'c15':i["summary"]}
	db.collection.insert(feeds15)
	print(feeds15)
for i in feed16['items']:
	feeds16 = {'a16':i["title"],'b16':i["description"],'c16':i["summary"]}
	db.collection.insert(feeds16)
	print(feeds16)
for i in feed17['items']:
	feeds17 = {'a17':i["title"],'b17':i["description"],'c17':i["summary"]}
	db.collection.insert(feeds17)
	print(feeds17)
for i in feed18['items']:
	feeds18 = {'a18':i["title"],'b18':i["description"],'c18':i["summary"]}
	db.collection.insert(feeds18)
	print(feeds18)
for i in feed19['items']:
	feeds19 = {'a19':i["title"],'b19':i["description"],'c19':i["summary"]}
	db.collection.insert(feeds19)
	print(feeds19)
for i in feed20['items']:
	feeds20 = {'a20':i["title"],'b20':i["description"],'c20':i["summary"]}
	db.collection.insert(feeds20)
	print(feeds20)
for i in feed21['items']:
	feeds21 = {'a21':i["title"],'b21':i["description"],'c21':i["summary"]}
	db.collection.insert(feeds21)
	print(feeds21)
for i in feed22['items']:
	feeds22 = {'a22':i["title"],'b22':i["description"],'c22':i["summary"]}
	db.collection.insert(feeds22)
	print(feeds22)
for i in feed23['items']:
	feeds23 = {'a23':i["title"],'b23':i["description"],'c23':i["summary"]}
	db.collection.insert(feeds23)
	print(feeds23)
for i in feed24['items']:
	feeds24 = {'a24':i["title"],'b24':i["description"],'c24':i["summary"]}
	db.collection.insert(feeds24)
	print(feeds24)
