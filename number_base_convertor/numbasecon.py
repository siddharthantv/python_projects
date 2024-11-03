import argparse

# Dictionary to map names to bases
BASE_MAP = {
    "binary": 2,
    "octal": 8,
    "decimal": 10,
    "hexadecimal": 16
}

def convert_base(number, from_base, to_base):
    try:
        # Convert number to base 10
        base10 = int(number, from_base)
        
        # Convert base 10 number to the desired base
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        
        if base10 == 0:
            return "0", f"Convert {number} from base {from_base} to base 10:\nValue in base 10: 0\nConvert 0 from base 10 to base {to_base}:\nValue in base {to_base}: 0"
        
        steps = [f"Convert {number} from base {from_base} to base 10:"]
        steps.append(f"Value in base 10: {base10}")
        
        steps.append(f"Convert {base10} from base 10 to base {to_base}:")
        while base10 > 0:
            remainder = base10 % to_base
            result = digits[remainder] + result
            steps.append(f"{base10} / {to_base} = {base10 // to_base} with remainder {remainder} ({digits[remainder]})")
            base10 //= to_base
        
        steps.append(f"Value in base {to_base}: {result}")
        return result, "\n".join(steps)
    except ValueError:
        return "Invalid input", "Invalid input"

def main():
    parser = argparse.ArgumentParser(description="Convert numbers between different bases.")
    parser.add_argument('number', type=str, help='The number to convert.')
    parser.add_argument('from_base', type=str, choices=BASE_MAP.keys(), help='The base of the input number.')
    parser.add_argument('to_base', type=str, choices=BASE_MAP.keys(), help='The base to convert to.')
    
    args = parser.parse_args()
    
    from_base = BASE_MAP[args.from_base]
    to_base = BASE_MAP[args.to_base]
    
    result, steps = convert_base(args.number, from_base, to_base)
    
    print(f"Result: {result}\n")
    print(f"{args.to_base.capitalize()} Steps:\n{steps}")

if __name__ == "__main__":
    main()
