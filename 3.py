"""
This is just a very simple class of the basics and intuition for combining infinitesimals
to form a whole in calculus (of course, here we use a very small number, which is dx = 1e-7).

This class works for almost any mathematical function, but it is neither fast nor accurate.
This is just an exercise.
"""




class Integrate:
	def __init__(self, a: int, b: int, function = lambda x: x, dx: float = 1e-7):
		self.__a = a
		self.__b = b
        self.__dx = dx
        self.__function = function


    def __performing_consolidation_operations(self):
        while self.__a <= self.__b:
            yield self.__function(self.__a)
            self.__a += self.__dx


    def get(self) -> float:
        return sum(self.__performing_consolidation_operations()) * self.__dx


"""
for example:

>>> import math
>>> print(Integrate(0, 10, lambda x: math.sin(x), 1e-7).get())

Output: 1.8390715096288854

The real and of course approximate answer to
the integration of the sine function in mathematics: 1.83907152907645



That is, with an accuracy of 7 decimal places.
But it is slow.
So we can increase the speed by decreasing the precision of this function, which is running with an accuracy of 1e-7.
If we make it 10 times larger (i.e., farther from zero), we can expect to get the answer about 10 times faster.

Such as:

>>> print(Integrate(0, 10, lambda x: math.sin(x), 1e-6).get())

Output: 1.8390712580925284

The real and of course approximate answer to
the integration of the sine function in mathematics: 1.83907152907645




Output (1e-6): 		1.839 071 258 092 5284
Output (1e-7): 		1.839 071 509 628 8854
Mathematics: 		1.839 071 529 076 45



