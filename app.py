from flask import Flask, redirect, url_for, request, render_template_string

app = Flask(__name__)

# Success route
@app.route('/success/<name>')
def success(name):
    return f'Welcome {name}!'

# Login route
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form.get('nm')  # Fetch 'nm' from form
        if user:
            return redirect(url_for('success', name=user))
        else:
            return "Name not provided in form data!", 400
    else:
        user = request.args.get('nm')  # Fetch 'nm' from URL query
        if user:
            return redirect(url_for('success', name=user))
        else:
            return '''
            <form action="/login" method="post">
                <label for="nm">Enter your name:</label>
                <input type="text" id="nm" name="nm">
                <input type="submit" value="Submit">
            </form>
            '''

if __name__ == 'main':
    app.run(debug=True)