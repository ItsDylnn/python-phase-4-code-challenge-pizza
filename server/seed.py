
from app import app, db
from models import Restaurant, Pizza, RestaurantPizza

with app.app_context():
    db.drop_all()
    db.create_all()

    r1 = Restaurant(name="Karen's Pizza Shack", address="address1")
    r2 = Restaurant(name="Sanjay's Pizza", address="address2")

    p1 = Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese")
    p2 = Pizza(name="Geri", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")

    db.session.add_all([r1, r2, p1, p2])
    db.session.commit()

    rp1 = RestaurantPizza(price=5, pizza_id=p1.id, restaurant_id=r1.id)
    db.session.add(rp1)
    db.session.commit()

