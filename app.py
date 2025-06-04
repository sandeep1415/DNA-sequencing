from flask import Flask, render_template, request

try:
    from anarci import number
except ImportError:  # gracefully handle missing dependency
    number = None

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', numbering=None)

@app.route('/number', methods=['POST'])
def do_number():
    seq = request.form.get('sequence', '').strip()
    scheme = request.form.get('scheme', 'imgt')
    result = ""
    if not seq:
        result = "No sequence provided."
    elif number is None:
        result = "ANARCI library not installed."
    else:
        numbering, chain_type = number(seq, scheme=scheme)
        if numbering:
            # numbering is a list of tuples: [(position, aa)]
            result_lines = [f"{pos}\t{aa}" for pos, aa in numbering]
            result = "\n".join(result_lines)
        else:
            result = "Sequence could not be numbered."
    return render_template('index.html', numbering=result)

if __name__ == '__main__':
    app.run(debug=True)
