# Simple in-memory storage
ORDERS_DB = {"orders": {}, "next_id": 1}

MENU_DB = {
    "undhiyu": {
        "name": "Undhiyu",
        "price": 120.00,
        "description": "Traditional Gujarati mixed vegetable curry cooked with spices, fenugreek dumplings, and coconut.",
        "quantity": 1
    },
    "khichdi": {
        "name": "Khichdi",
        "price": 90.00,
        "description": "Comforting Gujarati dish made from rice and lentils, lightly seasoned with ghee and cumin.",
        "quantity": 1
    },
    "dal_dhokli": {
        "name": "Dal Dhokli",
        "price": 110.00,
        "description": "Lentil stew cooked with wheat flour dumplings, flavored with jaggery and tamarind.",
        "quantity": 1
    },
    "thepla": {
        "name": "Thepla",
        "price": 60.00,
        "description": "Spiced flatbread made from whole wheat flour and fenugreek leaves, served with curd or pickle.",
        "quantity": 4
    },
    "handvo": {
        "name": "Handvo",
        "price": 100.00,
        "description": "Savory lentil cake baked with vegetables and tempered with mustard seeds and curry leaves.",
        "quantity": 1
    },
    "fafda_jalebi": {
        "name": "Fafda Jalebi",
        "price": 80.00,
        "description": "Classic Gujarati breakfast combo — crispy fafda served with sweet jalebi and papaya chutney.",
        "quantity": 1
    },
    "shrikhanda": {
        "name": "Shrikhanda",
        "price": 70.00,
        "description": "Sweetened hung curd dessert flavored with saffron and cardamom, served chilled.",
        "quantity": 1
    },
    "roti": {
        "name": "Roti",
        "price": 10.00,
        "description": "Soft whole wheat flatbread, a staple accompaniment to all Gujarati meals.",
        "quantity": 1
    },
    "gujarati_thali": {
        "name": "Gujarati Thali",
        "price": 250.00,
        "description": "A full traditional Gujarati platter with dal, kadhi, sabzi, roti, rice, farsan, and dessert.",
        "quantity": 1
    },
    "khichu": {
        "name": "Khichu",
        "price": 50.00,
        "description": "Steamed rice flour dough seasoned with green chili and cumin, served hot with oil.",
        "quantity": 1
    }
}


def get_menu_info(dish_name):
    """Get menu item information."""
    dish = MENU_DB.get(dish_name.lower())
    if dish:
        return {
            "name": dish["name"],
            "description": dish["description"],
            "price": dish["price"],
            "quantity": dish["quantity"]
        }
    return {"error": f"Dish '{dish_name}' not found"}


def place_order(customer_name, dish_name):
    """Place a simple food order with predefined quantity."""
    dish = MENU_DB.get(dish_name.lower())
    if not dish:
        return {"error": f"Dish '{dish_name}' not found"}

    order_id = ORDERS_DB["next_id"]
    ORDERS_DB["next_id"] += 1

    order = {
        "id": order_id,
        "customer": customer_name,
        "dish": dish["name"],
        "quantity": dish["quantity"],
        "total": dish["price"],
        "status": "pending"
    }
    ORDERS_DB["orders"][order_id] = order

    return {
        "order_id": order_id,
        "message": f"Order {order_id} placed: {dish['quantity']} {dish['name']} for ₹{order['total']:.2f}",
        "total": order['total'],
        "quantity": dish['quantity']
    }


def lookup_order(order_id):
    """Look up an existing order."""
    order = ORDERS_DB["orders"].get(int(order_id))
    if order:
        return {
            "order_id": order_id,
            "customer": order["customer"],
            "dish": order["dish"],
            "quantity": order["quantity"],
            "total": order["total"],
            "status": order["status"]
        }
    return {"error": f"Order {order_id} not found"}


# Function mapping dictionary
FUNCTION_MAP = {
    'get_menu_info': get_menu_info,
    'place_order': place_order,
    'lookup_order': lookup_order
}
