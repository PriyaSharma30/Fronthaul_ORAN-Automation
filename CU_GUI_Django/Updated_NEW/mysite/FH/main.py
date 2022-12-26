# from crypt import methods
# from sqlite3 import Time
from flask  import *
import json , time

# from matplotlib.font_manager import json_dump
# from pip import main

app =Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    data_set = {'Page':'Home','Message':'Successly load the home page', 'Timestamp': time.time()}
    json_dump= json.dumps(data_set)

    return json_dump


@app.route('/user/', methods=['GET'])
def request_page():
    user_query= str(request.args.get('user')) #/user/?user=abc

    data_set = {'Page':'request','Message':'Successly got the request for {user_query}', 'Timestamp': time.time()}
    json_dump= json.dumps(data_set)

    return json_dump




if __name__=='__main__':
    app.run(port=7777)

