from gc import get_debug

import flash
from werkzeug.utils import redirect
from flask import Flask, render_template, request,session,url_for,flash
import pymysql
from pymysql.cursors import DictCursor

app=Flask(__name__,static_folder = 'static', template_folder = 'templates', static_url_path = '/static')
app.config.from_object(__name__)
app.config['SECRET_KEY']='7d441f27d441f27567d441f2b6176a'

# import ar_master
# mm=ar_master.master_flask_code()

def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='ecommerce',
        charset='utf8',
        cursorclass=DictCursor

    )

@app.route('/', methods=['GET', 'POST'])
def loginform():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        connection = get_db_connection()
        with connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
                user = cursor.fetchone()
                if user:
                    session['user_id'] = user['id']
                    session['username'] = user['username']
                    session['firstname'] = user['firstname']
                    session['email'] = user['email']
                    session['phoneno'] = user['phoneno']
                    return render_template('index.html')
                else:
                    # flash('Invalid credentials', 'error')
                    return redirect(url_for('loginform'))
    return render_template('loginform.html')


@app.route('/registerform', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        phoneno = request.form['phoneno']
        username = request.form['username']
        password = request.form['password']
        confirmpassword = request.form['confirmpassword']

        if password != confirmpassword:
            return render_template('registerform.html')

        connection = get_db_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = """
                      INSERT INTO users (firstname, lastname, email, phoneno, username, password)
                      VALUES (%s, %s, %s, %s, %s, %s) \
                      """
                cursor.execute(sql, (firstname, lastname, email, phoneno, username, password))
                connection.commit()

            return redirect(url_for("loginform"))

    return render_template('registerform.html')


@app.route('/index')
def homepage():
    return render_template('index.html')


@app.route('/admin', methods=['GET', 'POST'])
def admin_login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == 'admin':
            return redirect(url_for("welcomeadmin"))
        else:
            error = "Invalid username or password"

            return render_template('admin.html', error=error)

    return render_template('admin.html')

@app.route('/customer')
def customer():
    return render_template('customer.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/addcard', methods=['POST'])
def addcard():
    if 'user_id' not in session:
        return redirect('/') # User not logged in


    user_id = session['user_id']
    name = request.form['name']
    price = request.form['price']
    image = request.form['image']
    firstname = session.get('firstname')
    email = session.get('email')
    phoneno = session.get('phoneno')


    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO cart (user_id, product_name, price, image_path, firstname, email, phoneno,quantity) VALUES (%s, %s, %s, %s, %s,%s,%s,%s)",
                (user_id, name, price, image, firstname, email, phoneno,1))
    conn.commit()
    cur.close()
    conn.close()

    return redirect('/showcart')


@app.route('/showcart')
def showcart():
    if 'user_id' not in session:
        return redirect(url_for('loginform'))

    user_id = session['user_id']
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM cart WHERE user_id = %s", (user_id,))
    items = cursor.fetchall()
    cursor.close()
    connection.close()

    return render_template("showcart.html", items=items)

@app.route('/removefromcart', methods=['POST'])
def removefromcart():
    if 'user_id' not in session:
        return redirect(url_for('loginform'))  # redirect to login if not logged in

    user_id = session['user_id']
    product_id = request.form['product_id']

    conn = get_db_connection()
    cursor = conn.cursor()

    # Make sure to delete the product that belongs to this user only
    cursor.execute("DELETE FROM cart WHERE id = %s AND user_id = %s", (product_id, user_id))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for('showcart'))  # return to the cart page





@app.route('/userprofile')
def userprofile():
    if 'email' not in session:
        flash("Please log in to continue.", "error")
        return redirect(url_for('loginform'))

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT firstname, lastname, email, phoneno FROM users WHERE email = %s", (session['email'],))
    user_data = cursor.fetchone()
    cursor.close()
    connection.close()

    if user_data:
        return render_template('userprofile.html', userprofile= {
            'firstname': user_data["firstname"],
            'lastname': user_data['lastname'],
            'email': user_data['email'],
            'phoneno': user_data['phoneno']
        })
    else:
        flash("User not found.", "error")
        return redirect(url_for('loginform'))


# @app.route('/welcomeadmin')
# def welcomeadmin():
#     connection = get_db_connection()
#     with connection:
#         with connection.cursor() as cursor:
#             sql = """
#                SELECT * FROM users
#             """
#             cursor.execute(sql)
#             welcomeadmin = cursor.fetchall()
#     return render_template('welcomeadmin.html', welcomeadmin=welcomeadmin)


@app.route('/welcomeadmin')
def welcomeadmin():
    connection = get_db_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = """
               SELECT * FROM users
            """
            cursor.execute(sql)
            welcomeadmin = cursor.fetchall()


            cursor.execute("""
                           SELECT firstname, email ,phoneno, product_name, price,quantity
                           FROM cart
                           """)
            userproducts = cursor.fetchall()

    return render_template('welcomeadmin.html',welcomeadmin=welcomeadmin,userproducts=userproducts)

@app.route('/privacypolicy')
def privacypolicy():
    return render_template('privacypolicy.html')

@app.route('/termsuser')
def termsuser():
    return render_template('termsuser.html')

@app.route('/salesrefunds')
def salesrefunds():
    return render_template('salesrefunds.html')


if __name__=='__main__':
    app.run(debug=True,use_reloader=True, port="6800")
