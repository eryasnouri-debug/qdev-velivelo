from enum import Enum

class Verdict(Enum):
  SANS_DEPASSEMENT = 0,
  AVEC_DEPASSEMENT = 1,
  AMENDE = 2
