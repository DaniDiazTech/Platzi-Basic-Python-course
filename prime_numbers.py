def prime():
    pass

def main():
    number = int(input("Your number: "))
    print(f"Your number {number} is prime" if prime(number) 
            else 'Sorry the number {number} is not prime')

if __name__ == '__main__':
    main()
