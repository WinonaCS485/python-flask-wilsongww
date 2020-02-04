from flask import Flask, render_template
import pymysql
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/re7538jj')
def re7538jj():
    
    

    # Connect to the database
    connection = pymysql.connect(host='mrbartucz.com',
                             user='re7538jj',
                             password='************',
                             db='re7538jj_University',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.Cursor)

    try:
        with connection.cursor() as cursor:
            # Select all Students
        
            sql = "SELECT * from Students"

        
            # execute the SQL command
            cursor.execute(sql)
            data = cursor.fetchall()
            
        

    finally:
        
        return render_template('database.html', data = data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

    
    
