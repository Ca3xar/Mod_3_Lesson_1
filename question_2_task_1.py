service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"},
}
def open_ticket(ticket_id, customer, issue):
    if ticket_id in service_tickets:
        print(f"Ticket {ticket_id} already exists.")
    else:
        service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}
        print(f"Ticket {ticket_id} opened for {customer}.")
def update_ticket_status(ticket_id, new_status):
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = new_status
        print(f"Ticket {ticket_id} status updated to {new_status}.")
    else:
        print(f"Ticket {ticket_id} not found.")
def display_tickets(status_filter=None):
     for ticket_id, details in service_tickets.items():
        if status_filter is None or details["Status"].lower() == status_filter.lower():
            print(f"{ticket_id}: Customer: {details['Customer']}, Issue: {details['Issue']}, Status: {details['Status']}")

if __name__ == "__main__":
    
    open_ticket("Ticket003", "Simon", "Login problem")
    
    update_ticket_status("Ticket001", "closed")
    
    
    print("\nAll Tickets:")    
    display_tickets()

    print("\nOpen Tickets:")
    display_tickets(status_filter="open")

    print("\nClosed Tickets:")
    display_tickets(status_filter="closed")