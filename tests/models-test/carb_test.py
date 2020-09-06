"""
testCar.py
---------------------
Testing the Car class
"""

class TestCarB:

  def testCarB(self, carsB):
    """ Testing the car.__str__(self) method
    """
    assert carsB['huracan'].getBrand() == 'Lamborghini'
    assert carsB['huracan'].getModel() == 'Huracán'
    assert carsB['huracan'].getYear() == 2014
    assert carsB['huracan'].getColor() == 'Green'
    # assert carsB['huracan'].getWheels() == 4
    assert carsB['huracan'].getHorsePower() == 602
    assert carsB['huracan'].getGears() == 7

  def testStart(self, carsB):
    carsB['m5'].start()
    assert carsB['m5'].getSpeed() == 1

  def testStop(self, carsB):
    carsB['m5'].stop()
    assert carsB['m5'].getSpeed() == 0

  def testAccelerate(self, carsB):
    carsB['m5'].accelerate(10)
    assert carsB['m5'].getSpeed() == 10

  def testBrake(self, carsB):
    carsB['huracan'].accelerate(10)
    carsB['huracan'].brake(3)
    assert carsB['huracan'].getSpeed() == 7
