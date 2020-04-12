# Store the prime number in a file for later usage (e.g. for finding new prime numbers with the knowledge contained in the file)
output_file = 'C:/Python Projects/Playground/prime_numbers.txt'

array = [2, 3, 4, 5, 6, 7, 8, 9]
prime_array = []

number = 2

with open(output_file, 'w') as file:

    while True:
        isPrime = True
        for row in array:
            if array.index(row) != (len(array)-1):
                if isPrime:
                    if row != number:
                        if (number / row).is_integer() == True:
                            isPrime = False
                    else:
                        prime_array.append(number)
                        file.write(str(number) + '\n')
                        break
                else:
                    break
            else:
                if isPrime:
                    if row != number:
                        if (number / row).is_integer() == True:
                            isPrime = False
                        else:
                            array.append(number)
                            prime_array.append(number)
                            file.write(str(number) + '\n')
                            break
                    else:
                        break

        number = number + 1
