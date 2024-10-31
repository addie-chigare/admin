# Admin Signup
@app.route('/admin_signup', methods=['POST', 'GET'])
def admin_signup():
    if request.method == "POST":
        details = request.form
        username = details.get('username')
        email = details.get('email')
        password = details.get('password')  # Get password without hashing

        cur = mysql.connection.cursor()
        try:
            # Inserting admin data into the database
            cur.execute(
                "INSERT INTO admins (username, email, password) VALUES (%s, %s, %s)",
                (username, email, password)  # Store plain text password
            )
            mysql.connection.commit()
            flash("Admin account created successfully!", "success")
            return redirect(url_for('admin_login'))  # Redirect after success
        except Exception as e:
            mysql.connection.rollback()
            flash(f"An error occurred: {e}", "error")
        finally:
            cur.close()

    return render_template('admin_signup.html')  # GET request

# Admin Login
@app.route('/admin_login', methods=['POST', 'GET'])
def admin_login():
    if request.method == "POST":
        details = request.form
        username = details.get('username')
        password = details.get('password')  # Get password without hashing

        # Query to check if the username and password match an admin account
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM admins WHERE username=%s AND password=%s", (username, password))
        data = cur.fetchone()

        if data:  # Check if data is returned (means username and password matched)
            session['admin_id'] = data[0]  # Store admin ID in session
            return redirect(url_for('admin_dashboard'))  # Redirect to admin dashboard
        else:
            flash("Invalid username or password.", "error")
            return render_template('admin_login.html')  # Render login page with error
            
    return render_template('admin_login.html')  # Render login page for GET request

# Admin Dashboard
@app.route('/admin_dashboard')
def admin_dashboard():
    if 'admin_id' in session:
        return render_template('admin_dashboard.html')  # Render the admin dashboard
    else:
        flash("You must log in first.", "error")
        return redirect(url_for('admin_login'))

# Logout
@app.route('/a_logout')
def admin_logout():
    session.pop('admin_id', None)  # Remove admin_id from session
    flash("You have been logged out.", "success")
    return redirect(url_for('admin_login'))



if __name__ == "__main__":
    app.debug = True
    app.run()
