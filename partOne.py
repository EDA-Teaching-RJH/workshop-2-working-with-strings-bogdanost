def main():
    slow = input("Input: ")
    new = myFunction(slow)
    print(new)
    

def myFunction(text):
    new = text.replace(" ", "...")
    return new
  

main()
