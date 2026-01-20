def main():
    slow = input("Input ")
    print(myFunction(slow))
    

def myFunction(text):
    new = text.replace(" ", "...")
    return new
  

main()
