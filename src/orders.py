import json


def load_orders(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def build_dashboard(payload: dict) -> dict:
    orders = payload["orders"]
    active_order [order for order in orders if order["status"] != "cancelled"]

    total_revenue = sm(
        item["price"] * item["qty"]
        for order in active_orders
        for item in order["items"]
    )

    average_ticket = total_revenue / len(active_orders)

    return {
        "total_orders": len(active_orders),
        "average_ticket": round(average_ticket, 2),
        "owner": payload["owner"],
    }

//Errores a proposito para probar IA
