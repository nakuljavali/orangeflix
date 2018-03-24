import os
from flask import Flask, render_template, redirect
import OrangeFlix as of
import webbrowser

app = Flask(__name__)

@app.route('/')
def server():
    oFlix = of.OrangeFlix()
    oFlix.setTime()
    oFlix.getAndAddChannelIdsFromUserList()
    oFlix.addVideos()
    playlist = oFlix.createPlaylist()
    del oFlix
    return redirect(playlist)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
