class Counter:
    def __init__(self, max_number):
        self.i = 0
        self.max_number = max_number
    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        self.i += 1
        if self.i > self.max_number:
            raise StopIteration
            return self.i

count = Counter(5)
for elem in count:
    print(elem)


def raise_to_the_degrees(number, max_degree):
    i = 0
    for _ in range(max_degree):
        yield number ** i
        i += 1


res = raise_to_the_degrees(2, 5)
print(res)
for _ in res:
    print(_)




def helper(work):
    work_in_memory = work
    def helper(work):
        return f"I will help you with your {work_in_memory}. Afterwards I will help you with {work}"
    return helper

helper = helper("homework")
print(helper("cleaning"))
print(helper("driving"))


def checker(function):
    def checker(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print(f"We have problems {exc}")
        else:
            print(f"No problems. Result - {result}")

    return checker

@checker
def calculate(expression):
    return eval(expression)


calculate("2+2")


class Obj:

   def __init__(self, data):
       self.data = data

   def __iter__(self):
       for item in self.data:
           yield item

iterable = Obj([1, 2, 3, 4, 5])

for item in iterable:
   print(item)