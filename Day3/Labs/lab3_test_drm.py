import unittest #You need this module
import lab3_drm #This is the script you want to test

class mytest(unittest.TestCase):

  def test_shout(self):
	self.assertEqual("JERRY", lab3_drm.shout("jerry"))
	self.assertEqual("HELLO", lab3_drm.shout("hello"))
	self.assertEqual("UNCLE LEO", lab3_drm.shout("uncle leo"))
	self.assertEqual("7", lab3_drm.shout("7"))
	self.assertEqual("DO NOT YELL", lab3_drm.shout("do not yell"))
	with self.assertRaises(AttributeError): lab3_drm.shout(7)
    
  def test_reverse(self):
  	self.assertEqual("yrrej", lab3_drm.reverse("jerry"))
	self.assertEqual("olleh", lab3_drm.reverse("hello"))
	self.assertEqual("oel elcnu", lab3_drm.reverse("uncle leo"))
	self.assertEqual("987", lab3_drm.reverse("789"))

  def test_reversewords(self):
  	self.assertEqual("hello jerry", lab3_drm.reversewords("jerry hello"))
	self.assertEqual("leo uncle", lab3_drm.reversewords("uncle leo"))
	self.assertEqual("87 98", lab3_drm.reversewords("98 87"))
	
  def test_reversewordletters(self):
  	self.assertEqual("yrrej olleh", lab3_drm.reversewordletters("jerry hello"))
	self.assertEqual("elcnu oel", lab3_drm.reversewordletters("uncle leo"))
	self.assertEqual("89 78", lab3_drm.reversewordletters("98 87"))

  def test_piglatin(self):
	self.assertEqual("eseayth etzelsaypr areay akingaym eaym irstyayth", lab3_drm.piglatin("these pretzels are making me thirsty"))

if __name__ == '__main__': #Add this if you want to run the test with this script.
  unittest.main()
  
  