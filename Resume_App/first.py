from flask import Flask, render_template, jsonify

app = Flask(__name__, root_path='/Users/c_sav/Documents/web/Resume_App',
            static_url_path='')


@app.route('/home')
def first_template():
    return render_template("Newb.html")


placeholder = [{'id':1,
                'var2':'2',
                'var3':'3'}]

@app.route('/api/jj')
def api_jj():
    return jsonify(placeholder)

if __name__ == '__main__':
    app.run(debug=False)