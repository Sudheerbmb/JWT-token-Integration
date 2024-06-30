from flask import Flask, request, jsonify, render_template
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey123'  # Replace with your secret key
app.config['JWT_SECRET_KEY'] = 'superjwtsecretkey456'  # Replace with your JWT secret key
jwt = JWTManager(app)

# Dummy user data
USER_DATA = {
    'username': 'sudheer',
    'password': '123'
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == USER_DATA['username'] and password == USER_DATA['password']:
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token), 200
        else:
            return jsonify({"msg": "Bad username or password"}), 401
    return render_template('login.html')

@app.route('/index')
@jwt_required()
def index():
    current_user = get_jwt_identity()
    return render_template('index.html', user=current_user)

if __name__ == '__main__':
    app.run(debug=True)
