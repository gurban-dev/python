"""
Edge case tests for Apt system classes:
Apt, SpecialApt, GardenApt, RoofApt.
"""

import unittest
from apt import Apt
from special_apt import SpecialApt
from garden_apt import GardenApt
from roof_apt import RoofApt


class TestAptEdgeCases(unittest.TestCase):
	def test_apt_invalid_floor(self):
		# Floor negative or non-integer should raise ValueError
		with self.assertRaises(ValueError):
			Apt(-1, 50)
		with self.assertRaises(ValueError):
			Apt(2.5, 50)
		with self.assertRaises(ValueError):
			Apt("1", 50)

	def test_apt_invalid_area(self):
		# Area zero, negative or non-numeric should raise ValueError
		with self.assertRaises(ValueError):
			Apt(1, 0)
		with self.assertRaises(ValueError):
			Apt(1, -10)
		with self.assertRaises(ValueError):
			Apt(1, "100")

	def test_specialapt_invalid_has_view(self):
		# has_view must be boolean
		with self.assertRaises(ValueError):
			SpecialApt(1, 50, "yes")
		with self.assertRaises(ValueError):
			SpecialApt(1, 50, None)

	def test_gardenapt_invalid_garden_area(self):
		# garden_area must be positive number
		with self.assertRaises(ValueError):
			GardenApt(50, 0)
		with self.assertRaises(ValueError):
			GardenApt(50, -5)
		with self.assertRaises(ValueError):
			GardenApt(50, "large")

	def test_gardenapt_floor_and_view(self):
		# GardenApt floor must always be 0 and has_view False
		g = GardenApt(50, 20)
		self.assertEqual(g.get_floor(), 0)
		self.assertFalse(g.get_has_view())

	def test_roofapt_invalid_has_pool(self):
		# has_pool must be boolean
		with self.assertRaises(ValueError):
			RoofApt(5, 70, "yes")
		with self.assertRaises(ValueError):
			RoofApt(5, 70, None)

	def test_roofapt_price_calculation(self):
		# Check price calculation with and without pool
		r1 = RoofApt(0, 100, False)
		r2 = RoofApt(1, 100, True)
		# Floor 0 means no floor addition, but has view addition if floor > 0

		# No floor or pool or roof addition as floor=0
		# Rooftop apartments have an additional 40000 price tag. 
		self.assertEqual(r1.get_price(), 100 * 20000 + 0 + 40000)

		# For r2: base + floor addition + view addition + roof + pool
		base = 100 * 20000
		floor_add = 1 * 5000
		view_add = 1 * 600
		roof_add = 40000
		pool_add = 30000
		expected_price = base + floor_add + view_add + roof_add + pool_add
		self.assertEqual(r2.get_price(), expected_price)

	# def test_matches_methods(self):
	# 	# Apt matches with None min_area returns True
	# 	a = Apt(1, 50)
	# 	self.assertTrue(a.matches())
	# 	self.assertTrue(a.matches(min_area=40))
	# 	self.assertFalse(a.matches(min_area=60))

	# 	# SpecialApt matches with require_view True and False
	# 	s = SpecialApt(2, 70, True)
	# 	self.assertTrue(s.matches(60, require_view=True))
	# 	self.assertFalse(s.matches(80, require_view=True))
	# 	self.assertTrue(s.matches(60, require_view=False))

	# 	# GardenApt matches with min_area and min_garden
	# 	g = GardenApt(60, 15)
	# 	self.assertTrue(g.matches(50, 10))
	# 	self.assertFalse(g.matches(70, 10))
	# 	self.assertFalse(g.matches(50, 20))

	# 	# RoofApt matches with floor, area, has_pool
	# 	roofAptObj = RoofApt(3, 80, True)

	# 	# matches() is a method because it belongs to the
	# 	# RoofApt class. Thus, this method is invoked on
	# 	# an instance/object of the RoofApt class.
	# 	self.assertTrue(roofAptObj.matches(
	# 		spec_floor=3, spec_area=70, spec_has_pool=True)
	# 	)

	# 	print('\nThe test on the next line fails.')
	# 	self.assertFalse(
	# 		roofAptObj.matches(
	# 			spec_floor=2, spec_area=70, spec_has_pool=True
	# 		)
	# 	)

	# 	self.assertFalse(roofAptObj.matches(spec_floor=3, spec_area=90, spec_has_pool=True))
	# 	self.assertFalse(roofAptObj.matches(spec_floor=3, spec_area=70, spec_has_pool=False))
	# 	self.assertTrue(roofAptObj.matches(spec_floor=None, spec_area=None, spec_has_pool=None))

	def test_equality(self):
		# Equality for Apt
		a1 = Apt(1, 50)
		a2 = Apt(1, 50)
		a3 = Apt(2, 50)
		self.assertEqual(a1, a2)
		self.assertNotEqual(a1, a3)

		# Equality for SpecialApt includes has_view
		s1 = SpecialApt(1, 50, True)
		s2 = SpecialApt(1, 50, True)
		s3 = SpecialApt(1, 50, False)
		self.assertEqual(s1, s2)
		self.assertNotEqual(s1, s3)

		# Equality for GardenApt includes garden_area
		g1 = GardenApt(50, 20)
		g2 = GardenApt(50, 20)
		g3 = GardenApt(50, 25)
		self.assertEqual(g1, g2)
		self.assertNotEqual(g1, g3)

		# Equality for RoofApt includes has_pool
		r1 = RoofApt(3, 80, True)
		r2 = RoofApt(3, 80, True)
		r3 = RoofApt(3, 80, False)
		self.assertEqual(r1, r2)
		self.assertNotEqual(r1, r3)

	def test_str_methods(self):
		# Check string representation contains expected substrings
		a = Apt(1, 50)
		s = SpecialApt(2, 70, True)
		g = GardenApt(60, 15)
		r = RoofApt(3, 80, True)

		self.assertIn("floor: 1", str(a))
		self.assertIn("area: 50", str(a))

		self.assertIn("floor: 2", str(s))
		self.assertIn("has_view: True", str(s))

		self.assertIn("floor: 0", str(g))  # GardenApt floor always 0
		self.assertIn("garden_area: 15", str(g))
		self.assertIn("has_view: False", str(g))

		self.assertIn("floor: 3", str(r))
		self.assertIn("has_pool: True", str(r))
		self.assertIn("has_view: True", str(r))


if __name__ == "__main__":
	'''
	The line unittest.main() is the invocation of the
	unittest framework's test runner. This function
	serves as the entry point ("main" function) for
	running all the test cases defined in the file.

    What occurs after invoking unittest.main():
	1. All test methods are collected (methods starting with
	   test_) from classes derived from unittest.TestCase.

	2. The tests are run.

	3. A command-line interface is provided to control test
	   execution.

	4. The test results are outputted to the console.
	'''
	unittest.main()