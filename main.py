class Hello:
    @staticmethod
    def hello_world():
        greeting = 'Hello World'
        return greeting
    

if __name__ == '__main__':
    greeting = Hello.hello_world()
    print(greeting)