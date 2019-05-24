from functools import wraps

def dec2(name=""):
    def wrap(fnc):
        def inner(*args, **kwargs):
            print(name)
            print(fnc(*args, **kwargs))
        return inner
    return wrap


@dec2()
def main(val1, val2=20):
    return f"{val1} {val2}"

if __name__ == "__main__":
    main(11)