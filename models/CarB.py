"""
CarB
--------------------------------------
Contains a base Car class with builder
"""

class CarB:
  """
  This is a conceptual class representation of a simple Car

  :param brand: Brand of the car
  :type brand: str, optional
  :param model: Model of the car
  :type model: str, optional
  :param year: Year of the car
  :type year: int, optional
  :param color: Color of the car
  :type color: str, optional
  :param wheels: Number of wheels of the car
  :type wheels: int, optional
  :param horsePower: Number of HorsePower of the car
  :type horsePower: int, optional
  :param gears: Number of Gears of the car
  :type gears: int, optional
  """

  def __init__(self, builder):
    """Constructor method"""
    self.__brand = builder.brand
    self.__model = builder.model
    self.__year = builder.year
    self.__color = builder.color
    self.__wheels = builder.wheels
    self.__horsePower = builder.horsePower
    self.__gears = builder.gears
    self.__speed = 0

  def __str__(self):
    return (
      f'Brand: {self.__brand}\n'
      f'Model: {self.__model}\n'
      f'Year: {self.__year}\n'
      f'Color: {self.__color}\n'
      f'Wheels: {self.__wheels}\n'
      f'HorsePower: {self.__horsePower}\n'
      f'Gears: {self.__gears}\n'
    )

  # ------------------------------
  #           Getters
  # ------------------------------
  def getBrand(self) -> str:
    """ Getter for the property Brand
    :return brand: brand of the car
    """
    return self.__brand

  def getModel(self) -> str:
    """ Getter for the property Model
    :return model: model of the car
    """
    return self.__model

  def getYear(self) -> int:
    """ Getter for the property Year
    :return year: year of the car
    """
    return self.__year

  def getColor(self) -> str:
    """ Getter for the property Color
    :return color: color of the car
    """
    return self.__color

  def getWheels(self) -> int:
    """ Getter for the property Wheels
    :return wheels: wheels of the car
    """
    return self.__wheels

  def getHorsePower(self) -> int:
    """ Getter for the property HorsePower
    :return speed: speed of the car
    """
    return self.__horsePower

  def getGears(self) -> int:
    """ Getter for the property Gears
    :return gears: gears of the car
    """
    return self.__gears

  def getSpeed(self) -> int:
    """ Getter for the property Speed
    :return speed: speed of the car
    """
    return self.__speed


  # ------------------------------
  #           Methods
  # ------------------------------
  def start(self) -> int:
    """ starts the car, sets speed to 1
    :return speed: current speed of the car
    """
    self.__speed += 1
    return self.__speed

  def stop(self) -> int:
    """ stops the car, sets speed to zero
    :return speed: current speed of the car
    """
    self.__speed = 0
    return self.__speed

  def accelerate(self, val=5) -> int:
    """ increases speed by amount of val

    :param val: speed unit to be increased
    :return speed: current speed of the car
    """
    self.__speed += val
    return self.__speed

  def brake(self, val=5) -> int:
    """ decreases speed by amount of val

    :param val: speed unit to be decreased
    :return speed: current speed of the car
    """
    self.__speed -= val
    return self.__speed


  # ------------------------------
  #           Builder
  # ------------------------------
  class Builder:
    """The builder class"""

    # def __init__(self):
    #   self.wheels = 4

    def brand(self, brand) -> object:
      """ Builder for the property Brand """
      self.brand = brand
      return self

    def model(self, model) -> object:
      """ Builder for the property Model """
      self.model = model
      return self

    def year(self, year) -> object:
      """ Builder for the property Year """
      self.year = year
      return self

    def color(self, color) -> object:
      """ Builder for the property Color """
      self.color = color
      return self

    def wheels(self, wheels) -> object:
      """ Builder for the property Wheels """
      self.wheels = wheels
      return self

    def horsePower(self, horsePower) -> object:
      """ Builder for the property HorsePower """
      self.horsePower = horsePower
      return self

    def gears(self, gears) -> object:
      """ Builder for the property Gears """
      self.gears = gears
      return self

    def build(self) -> object:
      return CarB(self)
