def get_valid_input():
    users_input = input("Enter stock quantity (or 'quit' to exit): ")

    if users_input.lower() == "quit":
        return "quit"

    if not users_input.isdigit():
        print("Error: Invalid input. Please enter a valid non-negative integer.")
        return None

    total = int(users_input)

    if total < 0:
        print("Error: Negative values are not allowed.")
        return None

    return total


def process_delivery(current_total, new_value):
    return current_total + new_value


def calculate_tax(amount):
    return amount * 0.10


def generate_report(total_units, failed_attempts):
    print(f"Total Deliveries Processed: {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")


def main():
    inventory = 0
    failed_entries = 0
    deliveries_processed = 0

    while True:
        result = get_valid_input()

        if result == "quit":
            generate_report(deliveries_processed, failed_entries)
            break

        if result is None:
            failed_entries += 1
            continue

        delivery_amount = result
        tax = calculate_tax(delivery_amount)
        print(f"  Delivery: {delivery_amount} units | Tax: ${tax:.2f}")

        inventory = process_delivery(inventory, delivery_amount)
        deliveries_processed += 1


if __name__ == "__main__":
    main()