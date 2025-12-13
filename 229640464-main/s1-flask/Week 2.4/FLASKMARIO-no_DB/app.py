from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            height = int(request.form.get("height"))
            if 1 <= height <= 8:
                result = generate_pyramid(height)
            else:
                result = "Height must be a number between 1 and 8."
        except ValueError:
            result = "Invalid input. Please enter an integer."
    return render_template("index.html", result=result)

def generate_pyramid(height):
    pyramid = []
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        hashes = "#" * i
        pyramid.append(f"{spaces}{hashes}  {hashes}")
    return "<br>".join(pyramid)

if __name__ == "__main__":
    app.run(debug=True)
