from src.config import load_settings
from src.orders import load_orders, build_dashboard
from src.notifications import send_summary_email


def main() -> None:
    settings = load_settings()
    orders = load_orders("data/orders.json")
    dashboard = build_dashboard(orders)
    send_summary_email(dashboard["owner"])

    if settings["debug"]:
        print("Debug mode enabled")

    print("Dashboard generated:", dashboard)


if __name__ == "__main__":
    main()
