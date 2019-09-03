    
import base64
import pandas as pd
import requests
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from nltk.stem import WordNetLemmatizer
import re
from nltk.corpus import stopwords
import random
stopwords = set(stopwords.words('english'))
def pre_processing(sentence):
    lemmatizer = WordNetLemmatizer()
    sentence = sentence.lower()
    #sentence = re.sub("\d+"," ",sentence)
    sentence = re.sub('[!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]'," ",sentence)
    stem = ""
    Actual_Words = ["JJ","JJR","JJS",\
                    "RB","RBR","RBS"\
                    "UH",]
                    #"VBG","VBP"]
    Total_Words=[]
    for i in sentence.split():
        Total_Words.append(nltk.pos_tag([i])[0])
        
    print(Total_Words)
    #Total_Words = nltk.pos_tag(nltk.word_tokenize(sentence))
    #print(nltk.word_tokenize(sentence))
    #random.shuffle(Total_Words)
    
    print([item for item in Total_Words if item[1]=="JJ"])
    Final_Words = [word[0] for word in Total_Words if word[1] in Actual_Words]

    print("----",)
    for word in Final_Words:
        if word not in stopwords:
            #print("-----",nltk.pos_tag(word))
            stem+=(lemmatizer.lemmatize(word)+" ")
    return stem[:-1]

def check_good_or_not(tweet_text):
    if len(re.findall('\d+\.?\d*',tweet_text)) >= 5:
        return 0
    return 1
pre_processing("On Feb. 19, the physician-services provide")

def get_hashtags(user):
    hashtag1 = []

    hashtag1.extend([item["text"] for item in user["entities"]["hashtags"]])
    if "retweeted_status" in user:
        hashtag1.extend([item["text"] for item in user["retweeted_status"]["entities"]["hashtags"]])
    return list(set(hashtag1))

def get_user_mentions(user):
    user_mentions = []

    user_mentions.extend([item["screen_name"] for item in user["entities"]["user_mentions"]])
    if "retweeted_status" in user:
        user_mentions.extend([item["screen_name"] for item in user["retweeted_status"]["entities"]["user_mentions"]])
    return list(set(user_mentions))

#'expanded_url'
def get_mentioned_urls(user):
    urls = []
    if "media" not in user["entities"]:
        return urls
    urls.extend([item["expanded_url"] for item in user["entities"]["media"]])
    if "retweeted_status" in user:
        urls.extend([item["expanded_url"] for item in user["retweeted_status"]["entities"]["media"]])
    return list(set(urls))


def get_date_format(date):
    date = date.split()
    date = date[1:3]+date[-1:]
    #print("date : " + str(date))
    return "-".join(date)

def get_time_format(time):
    time = time.split()
    #print("time : " + time[3])
    return time[3]


class Twitter():
    token = "-1"
    base_url = 'https://api.twitter.com/'
    def __init__(self,client_key = "",client_secret = ""):
        self.client_key = '6AkVKj6pXLrnZZvTVNQBYHO3E'#insert your Client Key
        self.client_secret = 'G4OcrNI3A2H7Hb192X3crBilJPfSoCrSdQvNjCgy0RDXSlgENY'#insert your Client Secret Key
    def set_urls(self):

        auth_url = '{}oauth2/token'.format(self.base_url)
        return auth_url
    def b64_encoded_key(self):
        key_secret = '{}:{}'.format(self.client_key, self.client_secret).encode('ascii')
        b64_encoded_key = base64.b64encode(key_secret)
        b64_encoded_key = b64_encoded_key.decode('ascii')
        return b64_encoded_key
    def auth_headers(self):
        auth_headers = {
    'Authorization': 'Basic {}'.format(self.b64_encoded_key()),\
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'\
    }
        return auth_headers
    def auth_data(self):
        auth_data = {
    'grant_type': 'client_credentials'\
    }
        return auth_data
    def get_token(self):
        auth_resp = requests.post(self.set_urls(), headers=self.auth_headers(), data=self.auth_data())
        try:
            auth_resp.json()
            access_token = auth_resp.json()['access_token']
            self.token = access_token
            return access_token
        except:
            return -1
    def search_request(self,q = "@urstrulyMahesh", search_params = {}):
        search_headers = {
    'Authorization': 'Bearer {}'.format(self.token)\
    }
        # search_params = {
        #     'q': q,
        #     #'result_type': result_type,
        #     'tweet_mode' : "extended",
        #     'count': count,
        #     #'include_entities':1,
        #     }

        search_url = '{}1.1/search/tweets.json'.format(self.base_url)

        search_resp = requests.get(search_url, headers=search_headers, params=search_params)
        return search_resp

#print(item.get_token())
def func_twitter():
    metro_polices = ["#saaho"]
    from pprint import pprint
    #[pprint(item["text"]) for item in police["statuses"]]
    public_requests_police = pd.DataFrame()
    for index,search_query in enumerate(metro_polices):
        item = Twitter()
        item.get_token()
        #created object
        parameter = {
        'q': search_query,
        'result_type': "recent",
        'tweet_mode' : "extended",
        'count': 100,
        #'include_entities':1,
        }
        rows_count = 0
        rows = []
        while(rows_count<=1000):
            #total_count+=1
            print("search_params : ",parameter)
    
            police = item.search_request(search_query, search_params = parameter).json()
    
            count = 1
            #print(police)
            for user in police["statuses"]:
                print("*****************")
                #print("User Description : "+user["user"]["description"])
                #print("User Name : "+user["user"]["name"])
                #print("Twitter Name : "+user["user"]["screen_name"])
                #print("profile URL : "+user["user"]["url"])
                #print("Tweet Text : "+user["full_text"])
                #print("Link to tweet : https://twitter.com/statuses/"+user["id_str"])
                print("*****************----",count)
                count+=1
    
    
    
                if "retweeted_status" in user:
                    is_retweeted = "yes"
                    who_retweeted = user["retweeted_status"]["user"]["screen_name"]
                    continue
                else:
                    is_retweeted = "no"
                    who_retweeted = "NA"
                if check_good_or_not(user["full_text"])==0:    
                    continue
                
                rows_count = rows_count+1
                rows.append([user["user"]["name"],user["user"]["screen_name"],user["user"]["location"],user["user"]["description"]\
                ,user["full_text"],user["in_reply_to_screen_name"],str(get_mentioned_urls(user)),user["lang"],"https://twitter.com/statuses/"+user["id_str"],is_retweeted,who_retweeted\
                ,str(get_hashtags(user)),str(get_user_mentions(user)), get_date_format(user["created_at"]), get_time_format(user["created_at"])])
            if "next_results" not in police["search_metadata"]:
                print("main_sdfjaksdljfaklsd ---->>>",police)
                break
            #print(rows)
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("????????????????",police["search_metadata"])
            next = police["search_metadata"]["next_results"]
            print(next)
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",)
    
            new_params = {item.split('=')[0]:item.split('=')[1] for item in next[1:].split('&')}
            #parameter[""]= police["search_metadata"]["next_results"]
            parameter.update(new_params)
            parameter["max_id"] = int(parameter["max_id"])
            parameter["count"] = int(parameter["count"])
            parameter["include_entities"] = 'true'
            parameter["q"] = search_query
            #print("^^^^^^^",total_count,"^^^^^^")
        #print(rows)
        tweets = pd.DataFrame(rows,columns = ["User_Name", "Twitter_Name","Location", "Bio", "Tweet","Replied_to","media","Language","Tweet_Link",\
        "is_Retweeted","Original_Tweet_by","Hashtags","User_Mentions","tweet_date","tweet_time"])
        #print(rows)
        #print("these are tweets:::",tweets)
        public_requests_police = public_requests_police.append(tweets,ignore_index = True)
        tweets.to_excel(search_query+".xlsx")
        #pprint(police)
    public_requests_police.to_excel("public_requests_police.xlsx")
    
    print("---------------------------------------------------------------------")
    
    for i in metro_polices:
        word_cloud = pd.read_excel(i+".xlsx",columns = ["Tweet"])
        temp = word_cloud.Tweet.to_string()
        temp = re.sub("RT ","",temp)
        temp = re.sub("(#[\d\w]+)|@[\d\w]+","",temp)
        temp = re.sub("https.*\s","",temp)
        processed_temp = pre_processing(temp)
        #print(processed_temp)
        wordcloud = WordCloud(width = 800, height = 800,
                    background_color ='white',
                    min_font_size = 10).generate(processed_temp)
        
    
        # plot the WordCloud image
        plt.figure(figsize = (8, 8), facecolor = None)
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.tight_layout(pad = 0)
        plt.savefig("../media/"+i+"without_RT_without_HT_with_digits_co_v3.jpg")
        # plt.show()
        print(wordcloud.process_text(processed_temp))

func_twitter()


