def computerFunction(num1,num2):
    #[2:] to remove 0b prefix
    binNum1 = bin(num1)[2:]
    binNum2 = bin(num2)[2:]
    #pad string with zeros to same length
    maxLen = max(len(binNum1),len(binNum2))
    binNum1 = binNum1.zfill(maxLen)
    binNum2 = binNum2.zfill(maxLen)
    #xor and convert to int
    xor_results = [str(int(a) ^ int(b)) for a, b in zip(binNum1, binNum2)]
    xor_str = ''.join(xor_results)
    output = int(xor_str, 2)
    return output

result1 = computerFunction(10,20)
print(result1)
result2 = computerFunction(17,35)
print(result2)
result3 = computerFunction(61, 233)
print(result3)





