class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print("Called static_method")


# test = ClassTest()


# instance methods need the object to call them
# test.instance_method()
# ClassTest.instance_method(test)

# This doesn't need an object to call the method

# ClassTest.class_method()


# static method is just a function that lives inside a class that doesn't use the class or instance at all
ClassTest.static_method()

# instance methods are used for most things
# class methods are used often as factories
# static methods are used to just place a method in a class

