from Duck import MallardDuck,ModelDuck
from FlyBehavior import FlyNoWay

def main():
    mallard = MallardDuck()
    mallard.display()
    mallard.performQuack()
    mallard.performFly()
    mallard.swim()

    model = ModelDuck()
    model.display()
    model.performFly()
    model.set_fly_behavior(FlyNoWay())
    model.performFly()
    model.swim()


if __name__ == "__main__":
    main()
