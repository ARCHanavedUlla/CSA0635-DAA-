def reverse_number(num, rev=0if num == ):
        return rev
    
    digit = num % 10
    rev = rev * 10 + digit
    

    return reverse_number(num // 10, rev)

num = int(input("Enter a number: "))

reversed_num = reverse_number(num)

print("Reverse of", num, "is", reversed_num)
