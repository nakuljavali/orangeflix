from sets import Set
import urllib2
import datetime
import json
import os

class OrangeFlix:
    formattedTime = datetime.datetime.now()
    channelList = ['UCajXeitgFL-rb5-gXI-aG8Q', # The Great Big Story
                   'UCmmPgObSUPw1HL2lq6H4ffA', # Geography Now
                   'UCuCkxoKLYO_EQ2GeFtbM_bw', # Half as Interesting
                   'UC9RM-iSvTu1uPJb8X5yp3EQ', # Wendover Productions
                   'UC2C_jShtL725hvbm1arSV9w', # CGP Grey
                   'UCP5tjEmvPItGyLhmjdwP7Ww', # Real Life Lore
                   'UCsXVk37bltHxD1rDPwtNM8Q', # Kurzgesagt
                   'UCYO_jab_esuFRV4b17AJtAw', # 3Blue1Brown
                   'UCH4BNI0-FOK2dMXoFtViWHw', # Its Okay to be smart
                   'UCtwKon9qMt5YLVgQt1tvJKg', # Objectivity
                   'UCzR-rom72PHN9Zg7RML9EbA', # PBS Eons
                   'UCoxcjq-8xIDTYp3uz647V5A', # Numberphile
                   'UC64UiPJwM_e9AqAd7RiD7JA', # Today I Found Out
                   'UC7_gcs09iThXybpVgjHZ_7g'] # PBS Space Time

    userList = ['scishow']
    videoList = Set()

    def setTime(self, days = 1):
        yesterday = datetime.datetime.now() - datetime.timedelta(days = days)
        self.formattedTime =  yesterday.strftime("%Y-%m-%dT%H:%M:%SZ")

    def getAndAddChannelIdsFromUserList(self):
        for user in self.userList:
            query = ("https://www.googleapis.com/youtube/v3/channels?"
                     "part=contentDetails&"
                     "forUsername={0}&"
                     "key={1}".format(user, os.environ['ORANGEFLIX_KEY'])
                     )
            response = urllib2.urlopen(query)
            res = response.read()
            items = json.loads(res)["items"]
            for item in items:
                id = item['id']
                self.channelList.append(id)
                print id
            response.close()

    def addVideos(self):
        for channel in self.channelList:
            query = ("https://www.googleapis.com/youtube/v3/search?"
                     "part=snippet&"
                     "channelId={0}&"
                     "maxResults=5&"
                     "order=date&"
                     "publishedAfter={1}&"
                     "type=video&"
                     "key={2}".format(channel, self.formattedTime, os.environ['ORANGEFLIX_KEY'])
                    )
            response = urllib2.urlopen(query)
            res = response.read()
            items = json.loads(res)["items"]

            for item in items:
                id = item['id']['videoId']
                self.videoList.add(id)

    def createPlaylist(self):
        res = 'https://www.youtube.com/watch_videos?video_ids='
        for video in self.videoList:
            res += video + ','
        print "Playlist created: " + res
        return res
