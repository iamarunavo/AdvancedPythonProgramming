def make_stateful_object(initial_value: int):
    val = initial_value

    def get_value():
        nonlocal val
        return val
    def set_value(n):
        nonlocal val
        val = n
        return val
    def reset():
        nonlocal val
        val = initial_value
        return val

    return {
    "get_value": get_value,
    "set_value": set_value,
    "reset": reset
    }
stateful = make_stateful_object(10)
print(stateful['get_value']()) # Output: 10
stateful['set_value'](20)
print(stateful['get_value']()) # Output: 20
stateful['reset']()
print(stateful['get_value']()) # Output: 10