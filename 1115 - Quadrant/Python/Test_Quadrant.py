from Coordinate import Coordinate
from Quadrant import Quadrant


def test_should_get_first_quadrant_coordinate():
    # Arrange / Setup
    a = 10
    b = 20
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == "First"


def test_should_get_second_quadrant_coordinate():
    # Arrange / Setup
    a = -154
    b = 180
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == "Second"


def test_should_get_third_quadrant_coordinate():
    # Arrange / Setup
    a = -81
    b = -17
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == "Third"

def test_should_get_fourth_quadrant_coordinate():
    # Arrange / Setup
    a = 10
    b = -20
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == "Fourth"


def test_should_get_none_coordinate():
    # Arrange / Setup
    a = 0
    b = 0
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == ""