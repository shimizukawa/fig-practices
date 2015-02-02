# -*- coding: utf-8 -*-
from flask import Flask
from redis import Redis
import os
app = Flask(__name__)

# ホスト＝redisというのは、figが設定している/etc/hostsを参照しています。後ほど補足
# もちろん、Docker標準の環境変数を利用してもOKです
redis = Redis(host='redis', port=6379)  

@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello World! I have been seen %s times.' % redis.get('hits')

if __name__ == "__main__":
    # これはflaskの設定Tipsですが、他のコンテナから見えるようにhost="0.0.0.0"を設定する必要があります
    app.run(host="0.0.0.0", debug=True)
