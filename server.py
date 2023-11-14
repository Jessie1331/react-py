
from flask import Flask, request, abort

from config import me, db
from mockData import catalog, coupon_codes
import json
from flask_cors import CORS

app = Flask(__name__)
# CORS(app)
@app.get("/api")
def index():
    return "Hello from Flask!"

def fix_id(record):
    record["_id"] = str(record['_id'])
    
    return(record)

@app.get("/api/catalog")
def catalog():
    catalog = catalog.objects.all()
    catalog = [fix_id(record) for record in catalog]
    return json.dumps(catalog)

@app.get("/test")
def test():
    return "Test"


@app.get("/api/about")
def about():
    return json.dumps(me)

@app.get("/api/catalog")
def get_catalog():
    courser = db,products.find({})
    results = []

    for products in  courser:
        results.append(fix_id(products))
    return json.dumps(results)

@app.post("/api/catalog")
def save_product():
    product = request.get_json()
    db.products.insert_one(product)
    # catalog.append(product)
    return json.dumps(product)


@app.post("/api/version")
def version():
    v = {
        "version": "1.0.0"
        "name"  "Jesenia"
    }
    return json.dumps(v)



@app.get("/api/catalog")
def load_catalog():
    return json.dumps(catalog)

@app.post('/api/catalog')
def save_product():
    product = request.get_json()
    product["_id"] = [len(catalog) + 1]
    catalog.append(product)

    return json.dumps(product)

@app.Get('api/reports')
def get_reports():
    return json.dumps(catalog)


@app.put('/api/catalog/<id>')
def update_product(id):
    product = request.get_json()
    catalog[id] = product
    return json.dumps(product)



# get all products in givin catagory
@app.get("/app/product/<cat>")
def get_by_catagory(cat):
    courser = db.prods.find({"catagory": cat})
    results = []
    for prod in courser:
          if prod['catagory'] == cat:
              fix_id(prod)
              results.append(prod)

    return json.dumps(results)

#get search term
@app.get("api/products//search/<term>")
def product_search(term):
    results = []
    for prod in catalog:
        if prod['title'] == term:
            results.append(prod)

@app.get('/api/coupon/<code>')
def get_all_coupon(code):
    results = []
    for code in coupon_codes:
        if  ['discount'] == code:
            results.append(code)




@app.post('/api/Catalog')
def save_coupon(code):
    coupon = request.get_json()
    coupon[code] = [code + 1]
    catalog.append(coupon)



    

@app.get("/api/catalog")
def catalog():
    prods = fix_id(catalog)
    return json.dumps(prods)

@app.get("/api/coupons")
def coupons():
    prods = fix_id(coupon_codes)
    return json.dumps(prods)
    return json.dumps(fix_id(prods))    







@app.get("/app/product/<cat>")
def get_by_catagory(cat):
    

    results = []
    for prod in catalog:
          if prod['catagory'] == cat:
              results.append(prod)

    return json.dumps(results)

    
    #serch exact name

@app.get("/app/product/search/<term>")
def product_search(term):
    results = []
    for prod in catalog:
          if prod['title'] == term:
              results.append(prod)

    return json.dumps(results)  
#serch term in name
@app.get("/app/product/search/<term>")
def product_search(term):
    results = []
    for prod in catalog:
          if term.lower() in prod['title'].lower:
              results.append(prod)

    return json.dumps(results)

#lower price then given number
@app.get("/api/product/lower/<price>")
def product_lower(price):
     results = []
     real_price = float(price)
     courser = db.products.find({'price': {'lte': real_price}})
     for prods in courser:
        fix_id(prods)
        results.apprnd(prods)

     return json.dumps(results)

@app.get('/api/product/greater/<price>')
def product_greater(price):
    #  results = []
     real_price = float(price)
     courser = db.products.find({'price': {'gte': real_price}})
     for prods in courser:
        fix_id(prods)
     return json.dumps


#get all products
@app.get("/api/products")
def get_products():

    return json.dumps(catalog)


#get api coupons
@app.get("/api/coupons")
def get_coupons():
    results = []
    courser = db.coupon_codes.find({})
    for coupon in courser:
       fix_id(coupon)
       results.append(coupon)
    return json.dumps(results)


#save coupon
@app.getpost("api/coupons")
def save_coupon():
    coupon = request.get_json()
    coupon._id = len(coupon_codes)
    
    coupon_codes.append(coupon)
    db.coupon_codes.insert_one(coupon)
    fix_id(coupon)

    return json.dumps(coupon)



#serch and return 
@app.get("api/coupon/<code>")
def search_coupon(code):
    courser = db.coupon_codes.find({'code': code})
      
    # courser = db.coupons.find_one({'code': '$regex':{ f"^{code}$" } '$options': "i" })
    for coupon in courser:
         if coupon['code'].lower() == code.lower():
           if not coupon:
        
             return   abort(404,"invalid Coupon Code")
    fix_id(coupon)

    return json.dumps(coupon)



app.run(debug=True)