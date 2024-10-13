from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    keyword = request.form['keyword']
    num_images = request.form['num_images']
    down_storage_dir = request.form['filename']
    email = request.form['email']

    # Run MainPipe.py with the provided inputs
    os.system(f"python MainPipe.py {keyword} {num_images} \"{down_storage_dir}\" \"{email}\"")

    return f"Input Received: {keyword}, {num_images}, {down_storage_dir}, {email}"

if __name__ == "__main__":
    app.run(debug=True)
