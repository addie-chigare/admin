from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.utils import secure_filename
from flask_mysqldb import MySQL  
from werkzeug.security import generate_password_hash
import logging
import os
import bcrypt
from flask import session
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
app.secret_key = '4534789265' 

# Configure MySQL connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '' 
app.config['MYSQL_DB'] = 'sgmbe'
app.config['UPLOAD_FOLDER'] = 'static/upload_floder'



mysql = MySQL(app)
logging.basicConfig(level=logging.DEBUG)
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)



@app.route('/')
def index():
    return render_template('admin_login.html')
""""
@app.route('/users', methods=['GET'])
def user_list():
    users = execute_db_query("SELECT * FROM signup")
    return render_template('user_list.html', users=users)

@app.route('/delete_user/<int:user_id>', methods=['GET'])
def delete_user(user_id):
    if execute_db_query("DELETE FROM signup WHERE id = %s", (user_id,)):
        flash('User deleted successfully!', 'success')
    else:
        flash('An error occurred while deleting the user.', 'danger')
    return redirect(url_for('user_list'))

@app.route('/block_user/<int:user_id>', methods=['GET'])
def block_user(user_id):
    if execute_db_query("UPDATE signup SET is_blocked = %s WHERE id = %s", (1, user_id)):
        flash('User blocked successfully!', 'success')
    else:
        flash('An error occurred while blocking the user.', 'danger')
    return redirect(url_for('user_list'))

@app.route('/unblock_user/<int:user_id>', methods=['GET'])
def unblock_user(user_id):
    if execute_db_query("UPDATE signup SET is_blocked = %s WHERE id = %s", (0, user_id)):
        flash('User unblocked successfully!', 'success')
    else:
        flash('An error occurred while unblocking the user.', 'danger')
    return redirect(url_for('user_list'))


"""
@app.route('/admin_signup', methods=['POST', 'GET'])
def admin_signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        cur = mysql.connection.cursor()
        try:
            cur.execute("INSERT INTO admin_signup (username, email, password) VALUES (%s, %s, %s)",
                        (username, email, password))
            mysql.connection.commit()
            flash("Admin account created successfully!", "success")
            return redirect(url_for('admin_login'))  # Redirect to avoid resubmission
        except Exception as e:
            mysql.connection.rollback()
            app.logger.error(f"An error occurred: {e}")
            flash("An error occurred while creating the account.", "danger")
            return render_template('admin_signup.html')
        finally:
            cur.close()

    return render_template('admin_signup.html')

  
@app.route('/admin_login', methods=['POST', 'GET'])
def admin_login():
    if request.method == "POST":
        details = request.form
        email = details.get('username')
        password = details.get('password')
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM  admin_signup  WHERE email=%s AND password=%s", (email, password))
        data = cur.fetchone()
        if data:
            session['user_id'] = data[0]
            return redirect(url_for('admin_dashboard'))
        else:
            flash("Invalid email or password.", "error")

    return render_template('admin_login.html')


@app.route('/admin_dashboard')
def admin_dashboard():
    # Check if the user is logged in
    if 'user_id' not in session:
        flash("Please log in to access the dashboard.", "warning")
        return redirect(url_for('admin_login'))  # Redirect to login if not logged in

    return render_template('admin_dashboard.html')  # Render the dashboard template

@app.route('/admin_logout')
def admin_logout():
    # Clear the session and redirect to login
    session.pop('user_id', None)
    flash("You have been logged out.", "success")
    return redirect(url_for('admin_login'))



@app.route('/add_product', methods=['POST', 'GET'])
def add_product():
    if request.method == "POST":
        details = request.form
        product_name = details.get('product-name')
        category = details.get('category')
        price = details.get('price')
        quantity = details.get('quantity')
        description = details.get('description')

        # Check if the file is present and valid
        if 'photo' not in request.files:
            flash("No file part", "danger")
            return redirect(request.url)

        file = request.files['photo']

        if file.filename == '':
            flash("No file selected", "danger")
            return redirect(request.url)

        #if not allowed_file(file.filename):
            flash("Invalid file type", "danger")
            return redirect(request.url)

        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        cur = mysql.connection.cursor()
        try:
            cur.execute(
                "INSERT INTO products (product_name, category, price, quantity, description, imagePath) VALUES (%s, %s, %s, %s, %s, %s)",
                (product_name, category, price, quantity, description, f'upload_folder/{filename}')
            )
            mysql.connection.commit()
            flash("Product added successfully!", "success")
            return redirect(url_for('list_products'))
        except Exception as e:
            mysql.connection.rollback()
            app.logger.error(f"An error occurred: {e}")
            flash("An error occurred while adding the product.", "danger")
        finally:
            cur.close()

    return render_template('add_product.html')


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        details = request.form
        product_name = details.get('product-name')
        category = details.get('category')
        price = details.get('price')
        quantity = details.get('quantity')
        description = details.get('description')

        if 'photo' not in request.files or request.files['photo'].filename == '':
            flash("No file selected", "error")
            return redirect(request.url)

        file = request.files['photo']
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        cur = mysql.connection.cursor()
        try:
            cur.execute(
                "INSERT INTO books (product_name, category, price, quantity, description, imagePath) VALUES (%s, %s, %s, %s, %s, %s)",
                (product_name, category, price, quantity, description, f'upload_folder/{filename}')
            )
            mysql.connection.commit()  # Commit the transaction
            flash("Book added successfully!", "success")
            return redirect(url_for('list_products'))
        except Exception as e:
            mysql.connection.rollback()  # Rollback in case of error
            app.logger.error(f"An error occurred: {e}")
            flash("An error occurred while adding the book.", "error")
        finally:
            cur.close()

    return render_template('add_book.html')

"""""
@app.route('/product/<int:product_id>')
def product(product_id):
    product_data = execute_db_query("SELECT * FROM products WHERE id = %s", (product_id,), fetchone=True)

    if product_data:
        return render_template('product_page.html', 
                               product_name=product_data[1],
                               price=product_data[3],
                               description=product_data[4],
                               category=product_data[2],
                               quantity=product_data[5],
                               image_path=product_data[6])
    else:
        flash("Product not found", "error")
        return redirect(url_for('list_products'))

@app.route('/deleteproducts', methods=['POST'])
def deleteproducts():
    product_id = request.form['id']
    if execute_db_query("DELETE FROM products WHERE id = %s", (product_id,)):
        flash("Product deleted successfully!", "success")
    else:
        flash("An error occurred while deleting the product.", "danger")
    return redirect(url_for('list_products'))

@app.route('/updateproducts', methods=['POST'])
def updateproducts():
    product_id = request.form['id']
    product_name = request.form['product-name']
    category = request.form['category']
    price = request.form['price']
    quantity = request.form['quantity']
    description = request.form['description']

    if execute_db_query("""#UPDATE products 
                            #SET product_name = %s, category = %s, price = %s, quantity = %s, description = %s 
                            ##WHERE id = %s""",
                         #(product_name, category, price, quantity, description, product_id)):
        #flash("Product updated successfully!", "success")
    #else:
       # flash("An error occurred while updating the product.", "danger")

    #return redirect(url_for('list_products'))
"""
@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        details = request.form
        product_name = details.get('product-name')
        category = details.get('category')
        price = details.get('price')
        quantity = details.get('quantity')
        description = details.get('description')

        if 'photo' not in request.files or request.files['photo'].filename == '':
            flash("No file selected", "error")
            return redirect(request.url)

        file = request.files['photo']
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

         cur = mysql.connection.cursor()
        try:
            cur.execute (
            "INSERT INTO books (product_name, category, price, quantity, description, imagePath) VALUES (%s, %s, %s, %s, %s, %s)",
            (product_name, category, price, quantity, description, f'upload_folder/{filename}')
        ):
            flash("Book added successfully!", "success")
            return redirect(url_for('list_products'))
        else:
            flash("An error occurred while adding the book.", "error")

    return render_template('add_book.html')
"""


@app.route('/products', methods=['GET'])
def list_products():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM products")
    products = cur.fetchall()
    cur.close()

    return render_template('product_list.html', products=products)


@app.route('/list_feedback', methods=['GET'])
def list_feedback():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM feedback")
    products = cur.fetchall()
    cur.close()

    return render_template('list_feedback.html', products=products)

@app.route('/ViewOrder')
def ViewOrder():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM purchases")
        orders = cur.fetchall()
        cur.close()
    except Exception as e:
        flash(f"An error occurred while fetching orders: {e}", "error")
        return redirect(url_for('admin_dashboard')) 

    return render_template('ViewOrder.html', orders=orders)






"""""
@app.route('/electronics', methods=['GET', 'POST'])
def electronics():
    if request.method == 'POST':
        details = request.form
        device_name = details.get('product_name')
        category = details.get('category')
        price = details.get('price')
        quantity = details.get('quantity')
        description = details.get('description')

        if 'photo' not in request.files or request.files['photo'].filename == '':
            flash("No file selected", "error")
            return redirect(request.url)

        file = request.files['photo']
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        # Save the file
        file.save(file_path)

        if execute_db_query(
            """#INSERT INTO electronics (device_name, category, price, quantity, description, imagePath) 
              # VALUES (%s, %s, %s, %s, %s, %s)""",
            #(device_name, category, price, quantity, description, f'upload_folder/{filename}')
        #):
           # flash("Product added successfully!", "success")
#return redirect(url_for('list_electronics'))  # Redirect to the list of electronics
        #else:
          #  flash("An error occurred while adding the product.", "error")

    #return render_template('electronics.html')

 # Admin Forgot Password
"""""
@app.route('/admin_forgot_password', methods=['GET', 'POST'])
def admin_forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        
        try:
            user = execute_db_query("SELECT * FROM admins WHERE email=%s", (email,), fetchone=True)

            if user:
                # Here you would ideally send an email with a reset link
                flash('A reset link has been sent to your email!', 'info')
                return redirect(url_for('admin_login'))  # Redirect after sending email
            else:
                flash("Email not found.", "error")
        except Exception as e:
            flash(f"An error occurred: {e}", "error")

    return render_template('admin_forgot_password.html')


# Admin Reset Password
@app.route('/admin_reset_password', methods=['GET', 'POST'])
def admin_reset_password():
    if request.method == 'POST':
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        if new_password == confirm_password:
            # Ideally, you should verify a token here
            admin_id = session.get('admin_id')  # Fetch the admin ID if logged in

            if admin_id:
                try:
                    execute_db_query(
                        "UPDATE admins SET password=%s WHERE id=%s",
                        (new_password, admin_id)
                    )
                    flash("Your password has been updated!", "success")
                    return redirect(url_for('admin_login'))
                except Exception as e:
                    flash(f"An error occurred: {e}", "error")
            else:
                flash("Admin not logged in.", "error")
        else:
            flash("Passwords do not match.", "error")

    return render_template('admin_reset_password.html')


@app.route('/ViewOrder')
def ViewOrder():
    try:
        orders = execute_db_query("SELECT * FROM purchases", fetchone=False)
        return render_template('ViewOrder.html', purchases=orders)
    except Exception as e:
        flash(f"An error occurred while fetching orders: {e}", "error")
        return redirect(url_for('admin_dashboard'))  # Redirect or handle the error as needed
"""

#user side code 


@app.route('/user_list')
def user_list():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, full_name, email, is_blocked FROM signup")  # Adjust as per your table
    users = cur.fetchall()
    cur.close()
    return render_template('user_list.html', users=users)

@app.route('/block_user/<int:user_id>')
def block_user(user_id):
    cur = mysql.connection.cursor()
    cur.execute("UPDATE signup SET is_blocked = 1 WHERE id = %s", (user_id,))
    mysql.connection.commit()
    flash("User blocked successfully!", "success")
    cur.close()
    return redirect(url_for('user_list'))

@app.route('/unblock_user/<int:user_id>')
def unblock_user(user_id):
    cur = mysql.connection.cursor()
    cur.execute("UPDATE signup SET is_blocked = 0 WHERE id = %s", (user_id,))
    mysql.connection.commit()
    flash("User unblocked successfully!", "success")
    cur.close()
    return redirect(url_for('user_list'))

@app.route('/delete_user/<int:user_id>')
def delete_user(user_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM signup WHERE id = %s", (user_id,))
    mysql.connection.commit()
    flash("User deleted successfully!", "success")
    cur.close()
    return redirect(url_for('user_list'))


if __name__ == "__main__":
    app.run(debug=True)
    
