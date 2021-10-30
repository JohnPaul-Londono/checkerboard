from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def checkerboard():
    return render_template("index.html", row = 8, column = 8, color1 = "RoyalBlue", color2 = "lightpink")

@app.route("/<int:num>")
def checkerboard2(num):
    return render_template("index.html", row = num, column = 8, color1 = "Lightpink", color2 = "Royalblue")

@app.route("/<int:num>/<int:num2>")
def checkerboard3(num, num2):
    return render_template("index.html", row = num, column = num2, color1 = "Lightpink", color2 = "Royalblue")
    
@app.route("/<int:num>/<int:num2>/<string:color1>/<string:color2>")
def checkerboard4(num, num2, color1, color2):
    return render_template("index.html", row = num, column = num2, color1 = color1, color2 = color2 )

if __name__=="__main__":
    app.run(debug=True)