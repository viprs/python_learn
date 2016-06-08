class Cat():
    def __init__(self, name='', color=''):
        self.name = name
        self.color = color

    def say_name(self):
        return self.name

    def miao(self):
        print "miao"

    def run(self):
        print "run away"

if __name__ == "__main__":
    c1 = Cat('kitty', 'black white')
    c1.miao()
    print c1.say_name()

    c2 = Cat('bobo', 'grey')
    c2.run()
    print c2.say_name()