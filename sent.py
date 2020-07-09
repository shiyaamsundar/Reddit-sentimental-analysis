import praw
client_id="J8Xe3VqzLUrhvw"
client_secret="1GyMIYK8Pe9NJjdMAstKoPDKK4s"
user_agent="reddit"
username="shiyaamsundar"
passwd=""

reddit=praw.Reddit(client_id=client_id,client_secret=client_secret,user_agent=user_agent,username=username,password=passwd)
subred=reddit.subreddit("coronavirus")
hot=subred.hot(limit=11)
new=subred.new(limit=10)
controv=subred.controversial(limit=10)
top=subred.top(limit=10)
gilded=subred.gilded(limit=10)
cnt=0

for i in hot:
	print(cnt,
		'Title:{},      ups:{},        downs:{},       Have we visited:{}'.format(i.title,i.ups,i.downs,i.visited))
	i.comments.replace_more(limit=0)
	cnt+=1

	for j in i.comments.list():
		print(20*'-')
		print('Parent id',j.parent())
		print('comment id',j.id)
		#print(j.body)
		with open("doc4.txt","a") as f:
			print(str(j.body).encode('utf-8'),file=f)
			
			
