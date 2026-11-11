
# Q61: Precious Metal Loan Management
# Demonstrates TypeError and ValueError exception handling

def calculate_interest(metal, purity, amount, tenure):

    rates = {
        "gold": {18: 8.0, 22: 7.0, 24: 6.0},
        "silver": {925: 9.0, 950: 8.5, 999: 8.0},
        "platinum": {900: 10.0, 950: 9.5, 999: 9.0}
    }

    metal = metal.lower()

    if metal not in rates:
        raise ValueError("Invalid metal type")

    if purity not in rates[metal]:
        raise ValueError("Unsupported purity for this metal")

    if amount <= 0 or tenure <= 0:
        raise ValueError("Amount and tenure must be positive")

    rate = rates[metal][purity]
    interest = (amount * rate * tenure) / 100

    print("Metal:", metal.title())
    print("Purity:", purity)
    print("Loan Amount:", amount)
    print("Tenure:", tenure, "years")
    print("Interest Rate:", rate, "%")
    print("Total Interest: Rs.", interest)


# Function to handle errors in each test case
def run_case(description, function_call):

    print("\n", description)

    try:
        function_call()

    except TypeError as e:
        print("TypeError:", e)

    except ValueError as e:
        print("ValueError:", e)

    else:
        print("Interest calculated successfully.")

    finally:
        print("Loan processing completed.")


# Valid loan details
run_case(
    "Valid Loan",
    lambda: calculate_interest("gold", 22, 500000, 2)
)

# Missing argument cases
run_case("Missing all arguments", lambda: calculate_interest())
run_case("Missing purity and other arguments",
         lambda: calculate_interest("gold"))
run_case("Missing amount and tenure",
         lambda: calculate_interest("gold", 22))
run_case("Missing tenure",
         lambda: calculate_interest("gold", 22, 500000))
run_case("Missing multiple arguments",
         lambda: calculate_interest("silver"))

# Invalid metal
run_case("Invalid Metal",
         lambda: calculate_interest("diamond", 999, 100000, 2))

# Invalid purity
run_case("Invalid Purity",
         lambda: calculate_interest("gold", 15, 100000, 2))
