"""
Car Model
-------------------------
Contains a base Car class
"""

class Car:
  """
  This is a conceptual class representation of a simple Car

  :param brand: Brand of the car, defaults to "None"
  :type brand: str, optional
  :param model: Model of the car, defaults to "None"
  :type model: str, optional
  :param year: Year of the car, defaults to "None"
  :type year: int, optional
  :param color: Color of the car, defaults to "White"
  :type color: str, optional
  :param wheels: Number of wheels of the car, defaults to 4
  :type wheels: int, optional
  :param horsePower: Number of HorsePower of the car, defaults to 0
  :type horsePower: int, optional
  :param gears: Number of Gears of the car, defaults to 5
  :type gears: int, optional
  """

  def __init__(self,
               brand: str = None,
               model: str = None,
               year: int = None,
               color: str = 'White',
               wheels: int = 4,
               horsePower: int = 0,
               gears: int = 5):
    """Constructor method"""
    self.brand = brand
    self.model = model
    self.year = year
    self.color = color
    self.wheels = wheels
    self.horsePower = horsePower
    self.gears = gears
    self.speed = 0

  def __str__(self):
    return (
      f'Brand: {self.brand}\n'
      f'Model: {self.model}\n'
      f'Year: {self.year}\n'
      f'Color: {self.color}\n'
      f'Wheels: {self.wheels}\n'
      f'HorsePower: {self.horsePower}\n'
      f'Gears: {self.gears}\n'
    )

  def start(self) -> int:
    """ starts the car, sets speed to 1
    :return speed: current speed of the car
    """
    self.speed += 1
    return self.speed

  def stop(self) -> int:
    """ stops the car, sets speed to zero
    :return speed: current speed of the car
    """
    self.speed = 0
    return self.speed

  def accelerate(self, val=5) -> int:
    """ increases speed by amount of val

    :param val: speed unit to be increased
    :return speed: current speed of the car
    """
    self.speed += val
    return self.speed

  def brake(self, val=5) -> int:
    """ decreases speed by amount of val

    :param val: speed unit to be decreased
    :return speed: current speed of the car
    """
    self.speed -= val
    return self.speed
