def apply_transformation(numbers: list[int], transform_function: Callable) -> list:
    return [transform_function(num) for num in numbers]