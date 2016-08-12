import unittest #You need this module
import ordinal_drm #This is the script you want to test


class ordinal_drm_test(unittest.TestCase):

  def identical_test(self):
	self.assertEqual("1st", myscript.myfunction(1))
	self.assertEqual("2nd", myscript.myfunction(2))
	self.assertEqual("3rd", myscript.myfunction(3))
	self.assertEqual("8th", myscript.myfunction(8))
	self.assertEqual("11th", myscript.myfunction(11))
	self.assertEqual("12th", myscript.myfunction(12))
	self.assertEqual("13th", myscript.myfunction(13))
	self.assertEqual("18th", myscript.myfunction(18))
	self.assertEqual("21st", myscript.myfunction(21))
	self.assertEqual("22nd", myscript.myfunction(22))
	self.assertEqual("23rd", myscript.myfunction(23))
	self.assertEqual("28th", myscript.myfunction(28))
    
  def not_identical_test(self):
  	thing1=myscript.myfunction(1)
  	thing2=myscript.myfunction(10)
	self.assertNotEqual(thing1, thing2)
	
  def integer_test(self):
	self.assertEqual("Must enter an integer!", myscript.myfunction("three"))
	self.assertEqual("Must enter an integer!", myscript.myfunction("third"))
	self.assertEqual("Must enter an integer to produce ordinal!", myscript.myfunction("3rd"))

if __name__ == '__main__': #Add this if you want to run the test with this script.
  unittest.main()


