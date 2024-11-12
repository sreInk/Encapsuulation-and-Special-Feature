class myclass:
    __privateVar = 19
    def __privateMeth(self):
        print("Yoima")
    def hello(self):
        print("HI")
foo = myclass()
foo.hello()
foo.__privateMeth