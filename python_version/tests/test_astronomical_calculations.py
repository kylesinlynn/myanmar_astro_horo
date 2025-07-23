"""
Unit tests for astronomical calculations
Tests the core astronomical functions against known values and expected results
"""

import unittest
import math
from datetime import datetime
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from core.astronomical_calculations import AstronomicalCalculations


class TestAstronomicalCalculations(unittest.TestCase):
    """Test cases for astronomical calculations"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.astro_calc = AstronomicalCalculations()
        
        # Test dates with known astronomical data
        self.test_date_1 = datetime(2000, 1, 1, 12, 0, 0)  # J2000.0 epoch
        self.test_date_2 = datetime(2023, 6, 21, 12, 0, 0)  # Summer solstice 2023
        self.test_date_3 = datetime(1990, 4, 17, 6, 30, 0)  # Myanmar New Year example
        
    def test_julian_day_number(self):
        """Test Julian Day Number calculations"""
        # J2000.0 epoch should be JD 2451545.0
        jd_2000 = self.astro_calc.julian_day_number(self.test_date_1)
        self.assertAlmostEqual(jd_2000, 2451545.0, places=1)
        
        # Test another known date
        test_date = datetime(1858, 11, 17, 0, 0, 0)  # Modified Julian Day epoch
        jd = self.astro_calc.julian_day_number(test_date)
        self.assertAlmostEqual(jd, 2400000.5, places=1)
        
    def test_mean_longitude_sun(self):
        """Test mean longitude of the Sun"""
        jd_2000 = self.astro_calc.julian_day_number(self.test_date_1)
        mean_long = self.astro_calc.mean_longitude_sun(jd_2000)
        
        # Should be around 280 degrees for J2000.0
        self.assertTrue(270 <= mean_long <= 290)
        
    def test_normalize_angle(self):
        """Test angle normalization function"""
        self.assertEqual(self.astro_calc.normalize_angle(0), 0)
        self.assertEqual(self.astro_calc.normalize_angle(360), 0)
        self.assertEqual(self.astro_calc.normalize_angle(450), 90)
        self.assertEqual(self.astro_calc.normalize_angle(-90), 270)
        
    def test_degrees_to_dms(self):
        """Test degrees to degrees-minutes-seconds conversion"""
        d, m, s = self.astro_calc.degrees_to_dms(123.456789)
        self.assertEqual(d, 123)
        self.assertEqual(m, 27)
        self.assertAlmostEqual(s, 24.44, places=1)
        
    def test_dms_to_degrees(self):
        """Test degrees-minutes-seconds to degrees conversion"""
        degrees = self.astro_calc.dms_to_degrees(123, 27, 24.44)
        self.assertAlmostEqual(degrees, 123.456789, places=5)
        
    def test_get_rashi(self):
        """Test zodiac sign calculation"""
        # Test known longitudes
        sign_en, sign_mm = self.astro_calc.get_rashi(0)
        self.assertEqual(sign_en, "Aries")
        self.assertEqual(sign_mm, "မိဿ")
        
        sign_en, sign_mm = self.astro_calc.get_rashi(90)
        self.assertEqual(sign_en, "Cancer")
        self.assertEqual(sign_mm, "ကရကဋ်")
        
        sign_en, sign_mm = self.astro_calc.get_rashi(180)
        self.assertEqual(sign_en, "Libra")
        self.assertEqual(sign_mm, "တူ")
        
    def test_lunar_phase(self):
        """Test lunar phase calculation"""
        jd = self.astro_calc.julian_day_number(self.test_date_1)
        phase, illumination = self.astro_calc.lunar_phase(jd)
        
        # Should return valid phase name and illumination percentage
        valid_phases = ["New Moon", "First Quarter", "Full Moon", "Last Quarter"]
        self.assertIn(phase, valid_phases)
        self.assertTrue(0 <= illumination <= 100)
        
    def test_planetary_positions(self):
        """Test planetary position calculations"""
        jd = self.astro_calc.julian_day_number(self.test_date_1)
        positions = self.astro_calc.planetary_positions(jd)
        
        # Should have positions for all planets
        expected_planets = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn']
        for planet in expected_planets:
            self.assertIn(planet, positions)
            self.assertTrue(0 <= positions[planet] < 360)
            
    def test_sunrise_sunset(self):
        """Test sunrise and sunset calculations"""
        jd = self.astro_calc.julian_day_number(self.test_date_1)
        
        # Test for Yangon coordinates
        latitude, longitude = 16.8661, 96.1951
        sunrise, sunset = self.astro_calc.sunrise_sunset(jd, latitude, longitude)
        
        # Sunrise should be before sunset and both should be reasonable times
        self.assertTrue(0 <= sunrise < 24)
        self.assertTrue(0 <= sunset < 24)
        self.assertTrue(sunrise < sunset)
        
        # For tropical location, day length should be around 12 hours
        day_length = sunset - sunrise
        self.assertTrue(10 < day_length < 14)


class TestAstronomicalAccuracy(unittest.TestCase):
    """Test astronomical calculation accuracy against known values"""
    
    def setUp(self):
        self.astro_calc = AstronomicalCalculations()
        
    def test_known_eclipse_dates(self):
        """Test calculations against known eclipse dates"""
        # Solar eclipse on 2017-08-21
        eclipse_date = datetime(2017, 8, 21, 18, 26, 0)  # Maximum eclipse time
        jd = self.astro_calc.julian_day_number(eclipse_date)
        
        # During solar eclipse, Moon should be close to Sun
        sun_long = self.astro_calc.true_longitude_sun(jd)
        moon_long = self.astro_calc.mean_longitude_moon(jd)
        
        # Angular difference should be small (within a few degrees)
        diff = abs(sun_long - moon_long)
        if diff > 180:
            diff = 360 - diff
        
        self.assertTrue(diff < 10, f"Sun-Moon difference too large: {diff} degrees")
        
    def test_seasonal_accuracy(self):
        """Test seasonal calculations"""
        # Summer solstice 2023 - Sun should be around 90 degrees
        summer_solstice = datetime(2023, 6, 21, 12, 0, 0)
        jd = self.astro_calc.julian_day_number(summer_solstice)
        sun_long = self.astro_calc.true_longitude_sun(jd)
        
        # Sun should be around 90 degrees (Cancer) at summer solstice
        self.assertTrue(85 <= sun_long <= 95, f"Summer solstice Sun longitude: {sun_long}")
        
        # Winter solstice 2023 - Sun should be around 270 degrees
        winter_solstice = datetime(2023, 12, 21, 12, 0, 0)
        jd = self.astro_calc.julian_day_number(winter_solstice)
        sun_long = self.astro_calc.true_longitude_sun(jd)
        
        # Sun should be around 270 degrees (Capricorn) at winter solstice
        self.assertTrue(265 <= sun_long <= 275, f"Winter solstice Sun longitude: {sun_long}")


if __name__ == '__main__':
    # Run the tests
    unittest.main(verbosity=2)
