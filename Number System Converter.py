def convert_num_system(num, from_base, to_base):
    if from_base != 10:
        decimal_num = int(num, from_base)
    else:
        decimal_num = int(num)

    if to_base == 2:
        return bin(decimal_num)[2:]
    elif to_base == 8:
        return oct(decimal_num)[2:]
    elif to_base == 10:
        return str(decimal_num)
    elif to_base == 16:
        return hex(decimal_num)[2:]
    else:
        return "Unsupported base"

def main():
    print("Bases")
    print("Binary: 2")
    print("Octal: 8")
    print("Decimal: 10")
    print("HexaDecimal: 16")
    num = input("Enter number: ")
    from_base = int(input("Base of input number: "))
    to_base = int(input("Base of output number: "))
    
    converted_num = convert_num_system(num, from_base, to_base)
    print(f"{num} in base {from_base} is {converted_num} in base {to_base}")

if __name__ == "__main__":
    main()