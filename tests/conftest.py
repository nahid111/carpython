import pytest
from models.car import Car

@pytest.fixture(scope='session')
def cars():
  """ Create our Cars, this only gets executed once per session.
  :return: a dict of car objects
  """
  m5 = Car(brand='BMW', model='M5', horsePower=617)
  huracan = Car(
    brand='Lamborghini',
    model='Huracán',
    year=2014,
    color='Green',
    horsePower=602,
    gears=7
  )

  return {'m5': m5, 'huracan': huracan}
