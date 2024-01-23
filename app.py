from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "admin"
app.config['MYSQL_DB'] = "my_db"
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')
    
    
@app.route('/cricket', methods = ['GET','POST'])
def cricket():
     if request.method=='GET':
         with mysql.connection.cursor() as cur:
            cur.execute("SELECT question FROM cricket")
            question_c = list(cur.fetchall())

         return render_template('form_cricket.html', question_c = question_c)
     else:
         ans = request.form['qid']

         with mysql.connection.cursor() as cur:
            cur.execute("SELECT answer FROM cricket where question = %s",(ans,))
            answer_c = list(cur.fetchall())
         return render_template('form_cricket.html', answer_det = str(answer_c[0]['answer']))

        #  cur = mysql.connection.cursor()
        #  answer_c = cur.execute("SELECT answer from cricket where question = '%s'",(ans,))
        #  answer_c = cur.execute("SELECT id, date_created, question, answer FROM cricket")
        #  answer_det = list(cur.fetchall())
        #  return render_template('form_cricket.html', answer_det = str(answer_c[0]['answer']))
        #  return '<h1>' + str(answer_c[0]['answer']) + '</h1>'
     
     
@app.route('/football', methods = ['GET','POST'])
def football():
     if request.method=='GET':
        with mysql.connection.cursor() as cur:
            cur.execute("SELECT question FROM football")
            question_f = list(cur.fetchall())
        return render_template('form_football.html', question_f = question_f)
     else:
         ans = request.form['qid']

         with mysql.connection.cursor() as cur:
            cur.execute("SELECT answer FROM football where question = %s",(ans,))
            answer_c = list(cur.fetchall())
         return render_template('form_football.html', answer_det = str(answer_c[0]['answer']))
     
@app.route('/hockey', methods = ['GET','POST'])
def hockey():
     if request.method=='GET':
        with mysql.connection.cursor() as cur:
            cur.execute("SELECT question FROM hockey")
            question_h = list(cur.fetchall())
        return render_template('form_hockey.html', question_h = question_h)
     else:
         ans = request.form['qid']

         with mysql.connection.cursor() as cur:
            cur.execute("SELECT answer FROM hockey where question = %s",(ans,))
            answer_c = list(cur.fetchall())
         return render_template('form_hockey.html', answer_det = str(answer_c[0]['answer']))
     
@app.route('/update_cricket', methods = ['GET', 'POST'])
def update_cricket():
    if request.method=='GET':
        return render_template('update_c.html')
    else:
        q = request.form['question']
        a = request.form['answer']
        with mysql.connection.cursor() as cur:
            cur.execute("INSERT INTO cricket (question, answer) VALUES (%s,%s)",(q,a))
            mysql.connection.commit()
        return render_template('update_c.html')

@app.route('/update_football', methods = ['GET', 'POST'])
def update_football():
    if request.method=='GET':
        return render_template('update_f.html')
    else:
        q = request.form['question']
        a = request.form['answer']
        with mysql.connection.cursor() as cur:
            cur.execute("INSERT INTO football (question, answer) VALUES (%s,%s)",(q,a))
            mysql.connection.commit()
        return render_template('update_f.html')

@app.route('/update_hockey', methods = ['GET', 'POST'])
def update_hockey():
    if request.method=='GET':
        return render_template('update_h.html')
    else:
        q = request.form['question']
        a = request.form['answer']
        with mysql.connection.cursor() as cur:
            cur.execute("INSERT INTO hockey (question, answer) VALUES (%s,%s)",(q,a))
            mysql.connection.commit()
        return render_template('update_.html')


if __name__=='__main__':
    app.run(debug=True, use_reloader=True)