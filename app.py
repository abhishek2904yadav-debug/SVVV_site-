from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)
app.secret_key = "svvv_secret_key"

# ---------------- Database Connection ----------------

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="Abhi2904@",          # Change if required
    database="project",
    autocommit=True
)

# ---------------- Home ----------------

@app.route('/')
def index():
    return render_template('index.html')


# ---------------- About ----------------

@app.route('/about')
def about():
    return render_template('about.html')


# ---------------- Course ----------------

@app.route('/course')
def course():
    return render_template('Course.html')


# ---------------- Blog ----------------

@app.route('/blog', methods=['GET', 'POST'])
def blog():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        comment = request.form['comment']

        try:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO comments(name,email,comment)
                    VALUES(%s,%s,%s)
                """, (name, email, comment))

            flash("Comment posted successfully!", "success")

        except Exception as e:
            flash(f"Error: {e}", "danger")

        return redirect(url_for('blog'))

    return render_template('Blog.html')


# ---------------- Contact ----------------

@app.route('/contact', methods=['GET', 'POST'])
def contact():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        try:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO Contact(name,email,subject,message)
                    VALUES(%s,%s,%s,%s)
                """, (name, email, subject, message))

            flash("Message sent successfully!", "success")

        except Exception as e:
            flash(f"Error: {e}", "danger")

        return redirect(url_for('contact'))

    return render_template('Contact.html')


# ---------------- Trainer Registration Page ----------------

@app.route('/trainer')
def trainer():
    return render_template('trainer.html')


# ---------------- Student Registration ----------------

@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        student_id = request.form['id']
        fullname = request.form['fullname']
        training = request.form['training']
        trainer_name = request.form['trainer']
        batch = request.form['batch']

        try:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO Student
                    (id, Fullname, training, trainer, Batch)
                    VALUES (%s,%s,%s,%s,%s)
                """, (
                    student_id,
                    fullname,
                    training,
                    trainer_name,
                    batch
                ))

            flash("Student Registered Successfully!", "success")

        except Exception as e:
            flash(f"Registration Failed: {e}", "danger")

        return redirect(url_for('trainer'))

    return render_template('trainer.html')


# ---------------- Run ----------------

if __name__ == "__main__":
    app.run(debug=True)