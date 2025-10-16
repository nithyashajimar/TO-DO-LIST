from flask import Flask, render_template, request, redirect, url_for

# Custom folder names
app = Flask(__name__, template_folder='html_pages', static_folder='assets')

todo_items = []

@app.route('/')
def home():
    return render_template('todo_page.html', todo_items=todo_items)

@app.route('/add', methods=['POST'])
def add_task():
    todo_item = request.form['todo_item']
    if todo_item:
        todo_items.append(todo_item)
    return redirect(url_for('home'))

@app.route('/delete/<int:index>')
def delete_task(index):
    if 0 <= index < len(todo_items):
        todo_items.pop(index)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
