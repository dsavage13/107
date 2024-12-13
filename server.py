from flask import Flask, request, abort
import json
from config import db
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # warning this disables CORS policy

@app.get('/')
def home():
    return "hello from flask"
# this is just an example
# @app.post('/')
# def homePost():
#   return "Hello from flask post"


# Endpoints
@app.get('/test')
def test():
    return "Hello from the test server"

# Endpoints using JSON
@app.get("/api/about")
def aboutGet():
    name = {"name": "Damian"}
    return json.dumps(name)

# Create a new route /greet/{name}  

@app.get('/greet/<name>')
def greet(name):
    return f"""
<h1 style=color:blue>Hello {name}<h1>"""

# Creating the farewell message
@app.get('/farewell/<name>')
def farewell(name):
    return f"""
<h1 style=color:red>Goodbye {name}<h1>"""

# Creating a POST Request
products = []

def fix_id(obj):
    obj["_id"] = str(obj["_id"])
    return obj

@app.get("/api/products")
def get_products():
    products_db = []
    cursor = db.products.find({})
    for prod in cursor:
        if "title" in prod:
            products_db.append(fix_id(prod))
    return json.dumps(products_db)

@app.post("/api/products")
def save_products():
    item = request.get_json()
    print(item)
    # products.append(item)
    db.products.insert_one(item)
    return json.dumps(fix_id(item))

@app.put("/api/products/<int:index>")
def update_products(index):
    updated_item = request.get_json()
    if 0 <= index <= len(products):
        products[index] = updated_item
        return json.dumps(updated_item)
    else:
        return "That index does not exist"

@app.delete("/api/products/<int:index>")
def delete_products(index):
    delete_item = request.get_json()
    if 0 <= index <= len(products):
        delete_item = products.pop(index)
        return json.dumps(delete_item)
    else:
        return "That index does not exist"

# pacth -- the method to update an especific element into python is: list.update

@app.patch("/api/products/<int:index>")
def patch_products(index):
    updated_field = request.get_json()
    if 0 <= index <= len(products):
        updated_field(index).update(updated_field)
        return json.dumps(updated_field)
    else:
        return "That index does not exist"
    
#######################################
############ COUPONS ##################
#######################################

@app.post("/api/coupons")
def save_coupons():
    item = request.get_json()
    db.coupons.insert_one(item)
    return json.dumps(fix_id(item))

@app.get("/api/coupons")
def get_coupons():
    coupons_db = []
    cursor = db.coupons.find({})
    for coupon in cursor:
        coupons_db.append(fix_id(coupon))
        
    return json.dumps(coupons_db)

@app.get("/api/coupons/<code>")
def validate_coupon(code):
    coupon = db.coupons.find_one({"code": code})
    if coupon == None:
        print("Error: Invalid Coupon")
        return abort(404, "Invalid Code")
        
    return json.dumps(fix_id(coupon))


app.run(debug=True)