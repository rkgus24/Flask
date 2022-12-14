from distutils import debug
from flask import Flask

app = Flask(__name__)

topics = [
    {'id': 1, 'title': 'html', 'body': 'html is ...'},
    {'id': 2, 'title': 'css', 'body': 'css is ...'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript is ...'}
]

def template(contents, content):
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {contents}
            </ol>
            {contents}
            <ul>
            <li><a href="/create/">create</a></li> 
            </ul>
        </body>
    </html>
    '''
    
def getContents():
    liTages=''
    for topic in topics:
        liTags = liTages + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return liTages

@app.route('/')
def index():
    return template(getContents(), '<h2>Welcome</h2>Hello, WEB')

@app.route('/read/<int:id>/')
def read(id):
    title = ''
    body = ''
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
            break
    return template(getContents(), f'<h2>{title}</h2>{body}')

@app.route('/create/')
def create():
    content = '''
        <form action="/create/"method="POST">
            <p><input type ="text" name="title" placeholder="title"></p>
            <p><textarea name="body" placeholder="body"></textarea></p>
            <p><input type="submit" value="creat"></p>
        </form>
    '''
    return template(getContents(), content)

app.run(debug=True)
