
def parse_collection(text):
    try:
        if not isinstance(text, str):
            return "", 0.0

        if ":" not in text:
            return "", 0.0

        material, kg = text.split(":", 1)

        material = material.strip().title()
        kg = float(kg.strip())

        return material, kg

    except (ValueError, TypeError, AttributeError, OverflowError):
        return "", 0.0


def weight_average(weights_csv):
    try:
        if not isinstance(weights_csv, str):
            return 0

        values = []

        for value in weights_csv.split(","):
            try:
                values.append(int(value.strip()))
            except (ValueError, TypeError, OverflowError):
                continue

        if not values:
            return 0

        return sum(values) // len(values)

    except (ValueError, TypeError, AttributeError, OverflowError):
        return 0


def net_points(text):
    try:
        if not isinstance(text, str):
            return 0

        if "|" not in text:
            return 0

        points, penalty = text.split("|", 1)

        points = float(points.strip())
        penalty = float(penalty.strip())

        total = points * 2 - penalty

        return max(total, 0)

    except (ValueError, TypeError, AttributeError, OverflowError):
        return 0


def main():
    print("==== Running parse_collection ====")
    user_input = input("Enter material:weight in kg: ")
    print("Material and Weight:", parse_collection(user_input))

    print("\n==== Running weight_average ====")
    user_input = input("Enter weights in kg as CSV: ")
    print("Average Weight:", weight_average(user_input))

    print("\n==== Running net_points ====")
    user_input = input("Enter points|penalty: ")
    print("Net Points:", net_points(user_input))


if __name__ == "__main__":
    main()
