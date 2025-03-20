from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)

DATABASE = 'C:/Users/yalmo/Desktop/cryptgram/db_CG'

# Function to get the database connection
def get_db():
    """Establish a connection to the database if it doesn't exist already."""
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row  # Enables dictionary-like access
    return db

# Function to close the database connection
@app.teardown_appcontext
def close_connection(exception):
    """Closes the database connection at the end of the request."""
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Function to fetch all records from the database
def query_db(query, args=(), one=False):
    """Query the database and return results."""
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/')
def show_posts():
    """Display posts fetched from the database."""
    posts = query_db("SELECT username, post FROM db_CryptNet ORDER BY postID DESC")
    return render_template('CRYPTGRAM.html', posts=posts)

def main():
    """Run the Flask app."""
    print("Starting the process...")
    app.run(debug=True)

if __name__ == '__main__':
    main()
