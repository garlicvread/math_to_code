"""
When you add two very long numbers, you may face a memory overflow problem.
To avoid this problem, you can use BigInt.

However, BigInt is not supported in all browsers,
and sometimes the number is too big to be stored in BigInt.

To solve this problem, you can use string to store the number.

1. When you receive two numbers, convert them to strings.
2. From the all the way back of the strings, add them.
3. Store the result in a variable. Let's say the name of the result as 'result'.
4. The length of the result is maximally 2.
   Thus, If the length of the result is 2,
   store the first character of the result to another variable called "carry_sum".
6. Repeat this process to the next digit.
   In this time, you need to calculate the sum of the second digits of the strings + the "carry_sum".
7. If the length of calculation is 2,
   store the first character of the result to 'carry_sum' and the second character to 'result'.
8. Repeat this process until there is no left characters for both strings.
9. If there is a "carry_sum" left, add it to the end of the result.
10. Reverse the result, and return it.
"""


def add_big_numbers(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    carry_sum = 0
    result = ''
    for i in range(max(len(num1), len(num2))):
        if i < len(num1):
            carry_sum += int(num1[-(i + 1)])
        if i < len(num2):
            carry_sum += int(num2[-(i + 1)])
        result += str(carry_sum % 10)
        carry_sum = carry_sum // 10
    if carry_sum > 0:
        result += str(carry_sum)
    print(int(result[::-1]))


num1 = 29385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592293850259827345298492758722592756297592759782348297459238759229385025982734529849275872259275629759275978234829745923875922938502598273452984927587225927562975927597823482974592387592
num2 = 3456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434563456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434563456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434563456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434563456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434563456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434563456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434563456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434563456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567890876543456545678767898909876543232343434543456543456543456789087654345654567876789890987654323234343454345654345654345678908765434565456787678989098765432323434345434565434565434567
print(len(str(num1)), len(str(num2)))
add_big_numbers(num1, num2)
