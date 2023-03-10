import string
import random
import datetime
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


def generate_code(length, code_type):
    chars = string.digits
    if code_type == "alphanumerical":
        chars += string.ascii_uppercase
    while True:
        code = ''.join(random.choice(chars) for _ in range(length))
        if 'E' in code and code.count('E') == 1 and not set('BDGILOQVZ01') & set(code):
            return code


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        code_type = request.form["code_type"]
        code_length = int(request.form["code_length"])
        num_codes = int(request.form["num_codes"])

        codes = set()
        while len(codes) < num_codes:
            code = generate_code(code_length, code_type)
            codes.add(code)

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"output/codes_{timestamp}.txt"
        with open(filename, "w") as f:
            f.write("\n".join(codes))

        return render_template("template.html", output=f"{num_codes} {code_type} codes generated and saved to {filename}")

    return render_template("template.html")


if __name__ == "__main__":
    app.run(debug=True)
