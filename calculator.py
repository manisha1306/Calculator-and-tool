class Calculator():
        
    def add(self,x, y):
        """Add Function"""
        return x + y


    def subtract(self,x, y):
        """Subtract Function"""
        return x - y


    def multiply(self,x, y):
        """Multiply Function"""
        return x * y


    def divide(self,x, y):
        """Divide Function"""
        if y == 0:
            raise ValueError('Can not divide by zero!')
        return x / y
    
    def integer_divide(self,x,y):
        """Interger Division Function"""
        if y == 0:
            raise ValueError('Can not divide by zero!')
        return x //y

    def power(self, x,y):
        """Power of number Function"""
        return x**y

    def root(self, x):
        """square root Function"""
        if x<0:
            raise ValueError('Cant find square root of negative number')
    
        return x**(0.5)
    def square(self,x):
        """square Function"""
        return x**2

    def factorial(self,x):
        """Function to find factorial"""
        fact=1
        if(x==0 or x==1):
            return 1
        else:
            for i in range (x,1,-1):
                fact=fact*i
            return fact

        



    

    
    
