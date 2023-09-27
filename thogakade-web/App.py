from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)
app.secret_key = 'many random bytes'

con = pymysql.connect(host='localhost', user='root', password='80221474', charset='utf8', db='thogakade')
cur = con.cursor()


@app.route('/')
def Index():
    cur = con.cursor()
    cur.execute("SELECT  * FROM customer")
    data = cur.fetchall()
    cur.close()

    return render_template('index.html', customer= data)


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        id = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        print(email, name, phone)
        # # cur = mysql.connection.cursor()
        cur.execute("INSERT INTO customer (id, name, gmail, phone) VALUES (%s, %s, %s, %s)", (id, name, email, phone))
        con.commit()
        return redirect(url_for('Index'))


@app.route('/delete/<string:id_data>', methods=['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    # cur = mysql.connection.cursor()
    cur.execute("DELETE FROM customer WHERE id=%s", (id_data,))
    con.commit()
    return redirect(url_for('Index'))


@app.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        print(email)
        cur.execute("""
               UPDATE customer
               SET name=%s, gmail=%s, phone=%s
               WHERE id=%s
            """, (name, email, phone, id_data))
        flash("Data Updated Successfully")
        con.commit()
        return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(debug=True)
