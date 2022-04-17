


from flask import Blueprint, request, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
    #return "Welcome Home"
    return render_template("home.html")

@home_routes.route("/about")
def about():
    print("ABOUT...")
    #return "About Me"
    return render_template("about.html")

@home_routes.route("/another")
def another():
    print("ANOTHER PAGE MAYBE...")
    return "Here is another page"


@home_routes.route("/hello")
def hello_world():
    print("HELLO...", dict(request.args))

    # if the request contains url params, for example a request to "/hello?name=Harper"
    # the request object's args property will hold the values in a dictionary-like structure
    url_params = dict(request.args)
    print("URL PARAMS:", url_params) #> can be empty like {} or full of params like {"name":"Harper"}
 
    #go check the URL params for the one called "name", and use it if possible
    #if no "name" parameter is specified, use a default value 
    name = request.args.get("name") or "World"


    message = f"Hello, {name}!"
    #return message
    return render_template("hello.html", message=message, other="YOLO")