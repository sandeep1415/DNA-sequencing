import os
from flask import Flask, render_template, request

try:
    from anarci import number
except ImportError:  # gracefully handle missing dependency
    number = None

BASE_DIR = os.path.dirname(__file__)
app = Flask(__name__, template_folder=os.path.join(BASE_DIR, 'templates'))

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

def main():
    """Launch the Flask development server."""
    app.run(debug=False, host="0.0.0.0", port=5000)


if __name__ == '__main__':
    main()
