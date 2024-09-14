@greet
def hello():
    print("helllow world")
def greet(fx):
    def mfx():
      print("good morning")
      fx()
      print("thanks for using this function")
    return mfx

#decorator
def add(a,b):
    print(a+b)

hello()
add()