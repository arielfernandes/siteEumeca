import os
from flask import Flask, render_template, Blueprint
from src.eumeca_blueprint.eumeca import eumeca_blueprint
app = Flask(__name__)
app.register_blueprint(eumeca_blueprint)

if __name__ == '__main__':
    # app.run(debug=True)
    port = int(os.getenv('PORT'), '5000')
    app.run(host='0.0.0.0', port=port)
