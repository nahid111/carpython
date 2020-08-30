"""
testCar.py
---------------------
Testing the Car class
"""

class TestCar:

  def testCar(self, cars):
    """ Testing the car.__str__(self) method
    """
    m5_str = 'Brand: BMW\nModel: M5\nYear: None\nColor: White\nWheels: 4\nHorsePower: 617\nGears: 5\n'
    assert str(cars['m5']) == m5_str

  def testStart(self, cars):
    cars['m5'].start()
    assert cars['m5'].speed == 1

  def testStop(self, cars):
    cars['m5'].stop()
    assert cars['m5'].speed == 0

  def testAccelerate(self, cars):
    cars['m5'].accelerate(10)
    assert cars['m5'].speed == 10

  def testBrake(self, cars):
    cars['huracan'].accelerate(10)
    cars['huracan'].brake(3)
    assert cars['huracan'].speed == 7
