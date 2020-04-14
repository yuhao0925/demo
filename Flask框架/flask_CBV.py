from flask import views, Flask

app = Flask(__name__)


class Login(views.MethodView):
    def get(self):
        return "get 200"

    def post(self):
        return 'post 200'


app.add_url_rule("/login", view_func=Login.as_view(name="login"))

if __name__ == '__main__':
    app.run()
