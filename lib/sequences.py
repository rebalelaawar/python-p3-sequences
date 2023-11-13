def print_fibonacci(length):
    sequence = []
    if length > 0:
        sequence.append(0)
        if length > 1:
            sequence.append(1)
            if length > 2:
                x = 2
                while x < length:
                    sequence.append(sequence[x-1] + sequence[x-2])
                    x += 1
                    
    print(sequence)


    


        
    