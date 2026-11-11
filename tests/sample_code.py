
def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)


def get_user_discount(price, discount):
    return price - discount


def read_user_file(filename):
    with open(filename, "r") as file:
        return file.read()


def get_user(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    return query
