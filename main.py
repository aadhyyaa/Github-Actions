class Hello:
    @staticmethod
    def ans():
        answer = input("What is the capital of India?  ")
        return answer
    

if __name__ == '__main__':
    answer = Hello.ans()
    print(answer)