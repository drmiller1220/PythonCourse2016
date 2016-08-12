import unittest #You need this module
from ordinal_drm import * #This is the script you want to test


class ordinal_drm_test(unittest.TestCase):

  def identical_test(self):
	self.assertEqual("1st", ordinalize(1))
	self.assertEqual("2nd", ordinalize(2))
	self.assertEqual("3rd", ordinalize(3))
	self.assertEqual("8th", ordinalize(8))
	self.assertEqual("11th", ordinalize(11))
	self.assertEqual("12th", ordinalize(12))
	self.assertEqual("13th", ordinalize(13))
	self.assertEqual("18th", ordinalize(18))
	self.assertEqual("21st", ordinalize(21))
	self.assertEqual("22nd", ordinalize(22))
	self.assertEqual("23rd", ordinalize(23))
	self.assertEqual("28th", ordinalize(28))
    
  def not_identical_test(self):
  	thing1=ordinalize(1)
  	thing2=ordinalize(10)
	self.assertNotEqual(thing1, thing2)
	
  def integer_test(self):
	self.assertEqual("Must enter an integer!", ordinalize("three"))
	self.assertEqual("Must enter an integer!", ordinalize("third"))
	self.assertEqual("Must enter an integer!", ordinalize("3rd"))

if __name__ == '__main__': #Add this if you want to run the test with this script.
  unittest.main()


