from abc import ABC, abstractmethod
from FlyBehavior import FlyWithWings
from QuackBehavior import Quack

# 抽象类
class Duck(ABC):
    def __init__(self, fly_behavior=FlyWithWings(), quack_behavior=Quack()):
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior
    
    @abstractmethod
    def display(self):
        pass
    
    def performFly(self):
        self.fly_behavior.fly()
    
    def performQuack(self):
        self.quack_behavior.quack()
    
    def swim(self):
        print("All ducks float, even decoys!")
    
    def set_fly_behavior(self, fly_behavior):
        self.fly_behavior = fly_behavior
    
    def set_quack_behavior(self, quack_behavior):
        self.quack_behavior = quack_behavior

    

class MallardDuck(Duck):
    def display(self):
        print("I'm a mallard duck!")


class ModelDuck(Duck):
    def display(self):
        print("I'm a model duck!")


