from flask import Flask, render_template, request, redirect
import model

app = Flask(__name__)

@app.route("/")
def index():
    ## print the guestbook
    return render_template("index.html", entries=model.get_entries())

@app.route("/add")
def addentry():
    ## add a guestbook entry
    return render_template("addentry.html")

@app.route("/postentry", methods=["POST"])
def postentry():
    name = request.form["name"]
    message = request.form["message"]
    model.add_entry(name, message)
    return redirect("/")

@app.route("/admin")
def admin():
    return render_template("admin.html", entries = model.get_entries())

# delete according to the ID of each post
# past ID when submit the form
# create a unique ID to each post
@app.route("/delete", methods=["POST"] )
def delete():
    #print("delect action")
    id_num = request.form["ID_num"]
    model.delete_entry(id_num)
    #return render_template("admin.html", entries = model.get_entries())
    return redirect('/admin') # the same


if __name__=="__main__":
    model.init()
    app.run(debug=True)
