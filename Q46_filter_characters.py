
# Q46. Filter Characters from a String

def filter_characters(target, reference):
    # Convert reference characters into a set
    remove_chars = set(reference)

    # Keep only characters not present in the reference
    result = ""

    for ch in target:
        if ch not in remove_chars:
            result += ch

    return result


# Sample input
target = "programming"
reference = "grm"

print("Result:", filter_characters(target, reference))
