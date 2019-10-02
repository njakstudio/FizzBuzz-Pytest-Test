# Importing the function fizzbuzz() from the file fizzbuzz.py
from fizzbuzz import fizzbuzz


class TestFizzBuzz:
	# When I fizzbuzz number 1, I get back a string representing it

	def test_answerFor1(self):
		assert fizzbuzz(1) == 1

	# When I fizzbuzz number 2, I get back a string representing it

	def test_answerFor2(self):
		assert fizzbuzz(2) == 2

	# When I fizzbuzz number 4, I get back a string representing it

	def test_answerFor4(self):
		assert fizzbuzz(4) == 4

	# When I fizzbuzz number 3, I get back "fizz"

	def test_answerFor3(self):
		assert fizzbuzz(3) == "fizz"

	# When I fizzbuzz a multiple of 3, I get back "fizz". Testing 6 and 9.

	def test_answerFor6(self):
		assert fizzbuzz(6) == "fizz"

	def test_answerFor9(self):
		assert fizzbuzz(9) == "fizz"

	# When I fizzbuzz number 5, I get back "buzz"

	def test_answerFor5(self):
		assert fizzbuzz(5) == "buzz"

	# When I fizzbuzz a multiple of 5, I get back "buzz". Testing 10 and 20.

	def test_answerFor10(self):
		assert fizzbuzz(10) == "buzz"

	def test_answerFor20(self):
		assert fizzbuzz(20) == "buzz"

	# When I fizzbuzz number 15, I get back "fizzbuzz"

	def test_answerFor15(self):
		assert fizzbuzz(15) == "fizzbuzz"

	# When I fizzbuzz a multiple of both 3 and 5, I get back "fizzbuzz". Testing 30 and 60.

	def test_answerFor30(self):
		assert fizzbuzz(30) == "fizzbuzz"

	def test_answerFor60(self):
		assert fizzbuzz(60) == "fizzbuzz"
