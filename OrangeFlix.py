import urllib2
import datetime
import json
import os

class OrangeFlix:
    formattedTime = datetime.datetime.now()
    channelList = ['UCajXeitgFL-rb5-gXI-aG8Q', # The Great Big Story
                   'UCmmPgObSUPw1HL2lq6H4ffA'] # Geography Now
    videoList = []

    def getTime(self):
        yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
        self.formattedTime =  yesterday.strftime("%Y-%m-%dT%H:%M:%SZ")

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
                self.videoList.append(id)

    def createPlaylist(self):
        res = 'https://www.youtube.com/watch_videos?video_ids='
        for video in self.videoList:
            res += video + ','
        return res
