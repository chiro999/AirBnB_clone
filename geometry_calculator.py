def calculate_square_area(side_length):
    """
    Calculate the area of a square.

    Parameters:
    - side_length (float): Length of a side of the square.

    Returns:
    - float: Area of the square.
    """
    if side_length <= 0:
        raise ValueError("Side length must be a positive number")

    area = side_length ** 2
    return area


def calculate_circle_area(radius):
    """
    Calculate the area of a circle.

    Parameters:
    - radius (float): Radius of the circle.

    Returns:
    - float: Area of the circle.
    """
    if radius <= 0:
        raise ValueError("Radius must be a positive number")

    pi = 3.141592653589793
    area = pi * radius ** 2
    return area


if __name__ == "__main__":
    # Example usage:
    square_side_length = 5
    circle_radius = 3

    square_area = calculate_square_area(square_side_length)
    circle_area = calculate_circle_area(circle_radius)

    print(f"Square area with side length {square_side_length}: {square_area}")
    print(f"Circle area with radius {circle_radius}: {circle_area}")

