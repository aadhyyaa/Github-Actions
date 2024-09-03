class Hello:
    @staticmethod
    def hello_world():
        greeting = input('Enter a greeting')
        return greeting
    

if __name__ == '__main__':
    greeting = Hello.hello_world()
    print(greeting)