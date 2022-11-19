import flask
import flask_bcrypt
import flask_login
import flask_sqlalchemy
import flask_mobility


app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stockfight.db'

mobility = flask_mobility.Mobility(app)
db = flask_sqlalchemy.SQLAlchemy(app)
bcrypt = flask_bcrypt.Bcrypt(app)
login_manager = flask_login.LoginManager(app)

app.app_context().push()

from stockfight import routes
