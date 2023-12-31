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

    cur.execute("SELECT  * FROM item")
    items = cur.fetchall()
    cur.close()

    return render_template('index.html', customer=data, item=items)


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        id = request.form['id']
        name = request.form['name']
        address = request.form['address']
        salary = request.form['salary']
        print(address, name, salary)
        cur.execute("INSERT INTO customer (customerID, Name, address, salary) VALUES (%s, %s, "
                    "%s, %s)", (id, name, address, salary))
        con.commit()
        return redirect(url_for('Index'))


@app.route('/delete/<string:id_data>', methods=['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur.execute("DELETE FROM customer WHERE customerID=%s", (id_data,))
    con.commit()
    return redirect(url_for('Index'))


@app.route('/deleteItem/<string:id_data>', methods=['GET'])
def deleteItem(id_data):
    flash("Record Has Been Deleted Successfully")
    cur.execute("DELETE FROM item WHERE itemCode=%s", (id_data,))
    con.commit()
    return redirect(url_for('Index'))


@app.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        address = request.form['address']
        salary = request.form['salary']
        cur.execute("""
               UPDATE customer
               SET Name=%s, address=%s,  salary=%s
               WHERE customerID=%s
            """, (name, address, salary, id_data))
        flash("Data Updated Successfully")
        con.commit()
        return redirect(url_for('Index'))


@app.route('/item_update', methods=['POST', 'GET'])
def item_update():
    id = request.form['updateItemId']
    description = request.form['updateItemName']
    unitPrice = int(request.form['updateItemPrice'])
    qty = float(request.form['updateItemQty'])
    print("update")
    cur.execute("""
                  UPDATE item
                  SET description=%s, qtyOnHand=%s,  uniPrice=%s
                  WHERE itemCode=%s
               """, (description, qty, unitPrice, id))
    con.commit()
    return redirect(url_for('Index'))


@app.route('/item_insert', methods=['POST'])
def item_insert():
    if request.method == "POST":
        id = request.form['Itemid']
        description = request.form['itemName']
        unitPrice = int(request.form['unitPrice'])
        qty = float(request.form['qty'])
        print("update")
        cur.execute("INSERT INTO item ( itemCode, description, qtyOnHand,  uniPrice) VALUES (%s, %s, "
                    "%s, %s)", (id, description, qty, unitPrice))
        con.commit()
        return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(debug=True)
