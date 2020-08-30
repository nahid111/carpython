import pytest
from models.Car import Car
from models.CarB import CarB

@pytest.fixture(scope='session')
def cars():
  """ Create our Cars, this only gets executed once per session.
  :return: a dict of car objects
  """
  m5 = Car(brand='BMW', model='M5', horsePower=617)
  huracan = Car(brand='Lamborghini', model='Huracán', year=2014,
                color='Green', horsePower=602, gears=7)

  return {'m5': m5, 'huracan': huracan}

@pytest.fixture(scope='session')
def carsB():
  """ Create our Cars, this only gets executed once per session.
  :return: a dict of car objects
  """
  m5 = CarB.Builder().brand('BMW').model('M5').horsePower(617).build()
  huracan = CarB.Builder().brand('Lamborghini').model('Huracán')\
    .horsePower(602).year(2014).color('Green').gears(7).build()

  return {'m5': m5, 'huracan': huracan}
