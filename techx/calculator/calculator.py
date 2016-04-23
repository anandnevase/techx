class TechxCalculator:
    @staticmethod
    def add(a,b):
        return a+b
    
    @staticmethod
    def subtract(a,b):
        return a-b
    @staticmethod
    def multiply(a,b):
        return a*b

if __name__ == '__main__':
    print dir(TechxCalculator)
    operation= [name for name in dir(TechxCalculator) if not name.startswith('_')]
    print operation
    
    methodToCall = getattr(TechxCalculator, 'add')
    result = methodToCall(3,4)
    print "Add :", result
    
    methodToCall = getattr(TechxCalculator, 'add')
    result = methodToCall('anand',4)
    print "Add :", result
