def send_summary_email(customer: dict) -> None:
    recipient = customer["email"].lower()
    print(f"Sending summary email to {recipient}")
