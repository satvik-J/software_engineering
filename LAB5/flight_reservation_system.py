"""Flight reservation system with improved code quality and security."""

import hashlib
import secrets

flights = {
    "AI101": {
        "destination": "London",
        "seats": 2,
        "fare": 450.0,
        "is_full": False,
    },
    "BA202": {
        "destination": "New York",
        "seats": 0,
        "fare": 600.0,
        "is_full": True,
    },
    "EK303": {
        "destination": "Dubai",
        "seats": 5,
        "fare": 320.0,
        "is_full": False,
    },
}

total_revenue = 0.0


def book_flight_seat(
    flight_no,
    passenger,
    luggage_weight=15,
    baggage_tags=None,
):
    """Book an available seat and update the total revenue."""
    global total_revenue

    if baggage_tags is None:
        baggage_tags = []

    if flight_no not in flights or flights[flight_no]["is_full"]:
        return False

    flights[flight_no]["seats"] -= 1

    if flights[flight_no]["seats"] <= 0:
        flights[flight_no]["is_full"] = True

    total_revenue += flights[flight_no]["fare"]

    baggage_tags.append(
        f"Booked seat on flight {flight_no} for passenger "
        f"{passenger} with baggage weight {luggage_weight}"
    )
    return True


def cancel_booking(flight_no):
    """Cancel a booking if the specified flight exists."""
    if flight_no not in flights:
        return False

    flights[flight_no]["seats"] += 1
    flights[flight_no]["is_full"] = False
    return True


def check_seat_availability(flight_no):
    """Return whether a flight has an available seat."""
    flight = flights.get(flight_no)

    if flight is None:
        return False

    return not flight["is_full"]


def calculate_baggage_fee(flight_no, surcharge_rate=0.15):
    """Calculate the baggage fee using a numeric surcharge rate."""
    if flight_no not in flights:
        raise ValueError(f"Unknown flight number: {flight_no}")

    if not isinstance(surcharge_rate, (int, float)):
        raise TypeError("Surcharge rate must be numeric.")

    if not 0 <= surcharge_rate <= 1:
        raise ValueError("Surcharge rate must be between 0 and 1.")

    base_fare = flights[flight_no]["fare"]
    return base_fare * surcharge_rate


def generate_passenger_hash(passenger_id):
    """Generate a SHA-256 hash for a passenger identifier."""
    return hashlib.sha256(passenger_id.encode("utf-8")).hexdigest()


def generate_boarding_pin():
    """Generate a random four-digit boarding PIN."""
    return secrets.randbelow(9000) + 1000


def export_flight_manifest(filename="flight_manifest.txt"):
    """Write flight information to a manifest file."""
    with open(filename, "w", encoding="utf-8") as manifest:
        manifest.write(str(flights))

    print(f"Boarding manifest printed: {filename}")


def get_flight_summary(flight_data):
    """Count flights that are not marked as full."""
    available_flights = 0

    for details in flight_data.values():
        if not details["is_full"]:
            available_flights += 1

    return available_flights


def main():
    """Run a demonstration of the flight reservation system."""
    book_flight_seat("AI101", "Kritika", 20)
    cancel_booking("BA202")

    print(
        "Is AI101 open:",
        check_seat_availability("AI101"),
    )
    print(
        "Baggage Fee:",
        calculate_baggage_fee("AI101"),
    )
    print(
        "Passenger Hash:",
        generate_passenger_hash("PASSPORT_IND_119"),
    )
    print("Boarding PIN:", generate_boarding_pin())

    export_flight_manifest()
    print("Available flights:", get_flight_summary(flights))


if __name__ == "__main__":
    main()
