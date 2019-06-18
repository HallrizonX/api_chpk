from string import Template


class Builder:
    def __init__(self):
        values = (method for method in self.__dir__() if
                  (method.startswith('__') is False and method.endswith('__') is False) or
                  (method.startswith('_') is False and method.endswith('_') is False)
                  )

        for item in values:
            def set_attr(val, name=item, self=self):
                self.__setattr__(name, val)
                return self

            self.__dict__[f'set_{item}'] = set_attr


class CarBuild(Builder):
    test = ""
    count = 0
    rank = 0


if __name__ == "__main__":
    c = CarBuild().set_test(10).set_count(10).set_rank(100)
    print(c.test)
    print(c.count)
    print(c.rank)
    a = c
