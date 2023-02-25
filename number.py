class Number:
    def __init__(self, value: int):
        self.value = value


    def get_number(self):
        """
        Returns the number.

        returns: int
        """
        return self.value

    def is_odd(self):
        """
        Returns True if the number is odd, otherwise False.

        returns: bool

        """
        return self.value % 2 == 1

    def is_even(self):
        """
        Returns True if the number is even, otherwise False. 

        returns: bool
        """
        return self.value % 2 == 0

    def is_prime(self):
        """
        Returns True if the number is prime, otherwise False.

        returns: bool
        """
        x = range(2, self.value)
        for i in x:
            if self.value % i != 0:
                return True
            else: 
                return False

    def get_divisors(self):
        """
        Returns a list of all the divisors of the number.

        returns: list
        """
        l = []
        for i in range(1, self.value+1):
            if self.value % i == 0:
                l.append(i)
        
        return l

    def get_length(self):
        """
        Returns the number of digits in the number.

        returns: int
        """
        return len(str(self.value))

    def get_sum(self):
        """
        Returns the sum of all the digits in the number.

        returns: int
        """
        x = []
        y = 0
        for i in str(self.value):
            x.append(i)
        for k in x:
            y += int(k)
        return y

    def get_reverse(self):
        """
        Returns the number in reverse.

        returns: int
        """
        return int(str(self.value)[::-1])
    def is_palindrome(self):
        """
        Returns True if the number is a palindrome, otherwise False.

        returns: bool
        """
        palin = str(self.value)[::-1]
        return palin == self.value
    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """
        x = []
        for i in str(self.value):
            x.append(int(i))
        return x

    def get_max(self):
        """
        Returns the largest digit in the number.

        returns: int
        """
        x = []
        for i in str(self.value):
            x.append(int(i))
        return max(x)

    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """
        x = []
        for i in str(self.value):
            x.append(int(i))
        return min(x)

    def get_average(self):
        """
        Returns the average of all the digits in the number.

        returns: float
        """
        x = []
        for i in str(self.value):
            x.append(int(i))
        m = 0
        for i in x:
            m += i
        return m / len(str(self.value))
    def get_median(self):
        """
        Returns the median of all the digits in the number.

        returns: float
        """
        

    def get_range(self):
        """
        Returns the range of all the digits in the number.

        returns: list
        """
        pass

    def get_frequency(self):
        """
        Returns a dictionary of the frequency of each digit in the number.

        returns: dict
        """
        pass
    

# Create a new instance of Number
number = Number(36)
# print(number.get_number())
# print(number.is_even())
print(number.get_reverse())