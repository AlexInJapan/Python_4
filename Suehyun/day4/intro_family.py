from introduce import *

class IntroFamily(Intro):
  def __init__(self, name, age, pet):
    super().__init__(name, age)
    self.pet = pet

  def cat_out(self):
    cattxt = f'飼い猫の名前は、{self.pet}です'
    return cattxt