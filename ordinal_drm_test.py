import unittest #You need this module
import ordinal_drm #This is the script you want to test


class ordinal_drm_test(unittest.TestCase):

	def test_identical_test(self):
		self.assertEqual("1st", ordinal_drm.ordinalize(1))
		self.assertEqual("2nd", ordinal_drm.ordinalize(2))
		self.assertEqual("3rd", ordinal_drm.ordinalize(3))
		self.assertEqual("8th", ordinal_drm.ordinalize(8))
		self.assertEqual("11th", ordinal_drm.ordinalize(11))
		self.assertEqual("12th", ordinal_drm.ordinalize(12))
		self.assertEqual("13th", ordinal_drm.ordinalize(13))
		self.assertEqual("18th", ordinal_drm.ordinalize(18))
		self.assertEqual("21st", ordinal_drm.ordinalize(21))
		self.assertEqual("22nd", ordinal_drm.ordinalize(22))
		self.assertEqual("23rd", ordinal_drm.ordinalize(23))
		self.assertEqual("28th", ordinal_drm.ordinalize(28))

	def test_not_identical_test(self):
		thing1=ordinal_drm.ordinalize(1)
		thing2=ordinal_drm.ordinalize(10)
		self.assertNotEqual(thing1, thing2)

	def test_integer_test(self):
		self.assertEqual("The function ordinalize has been executed.", ordinal_drm.ordinalize("three"))
		self.assertEqual("The function ordinalize has been executed.", ordinal_drm.ordinalize("third"))
		self.assertEqual("The function ordinalize has been executed.", ordinal_drm.ordinalize("3rd"))

if __name__ == '__main__': #Add this if you want to run the test with this script.
	unittest.main()

