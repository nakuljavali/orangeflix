import os
from flask import Flask
import OrangeFlix as of
import webbrowser

app = Flask(__name__)

@app.route('/')
def server():
    oFlix = of.OrangeFlix()
    oFlix.getTime()
    oFlix.addVideos()
    webbrowser.open(oFlix.createPlaylist())
    return 'Success'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
