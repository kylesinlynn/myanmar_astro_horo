"""
Unit tests for Myanmar calendar system
Tests the Myanmar calendar calculations and conversions
"""

import unittest
from datetime import datetime
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from core.calendar_system import MyanmarCalendarSystem
from core.astronomical_calculations import AstronomicalCalculations


class TestMyanmarCalendarSystem(unittest.TestCase):
    """Test cases for Myanmar calendar system"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.calendar = MyanmarCalendarSystem()
        self.astro_calc = AstronomicalCalculations()
        
        # Test dates
        self.test_date_1 = datetime(2023, 4, 17)  # Myanmar New Year 2023
        self.test_date_2 = datetime(2000, 1, 1)   # Y2K
        self.test_date_3 = datetime(1990, 4, 17)  # Historical Myanmar New Year
        
    def test_gregorian_to_myanmar_conversion(self):
        """Test Gregorian to Myanmar calendar conversion"""
        myanmar_date = self.calendar.gregorian_to_myanmar(self.test_date_1)
        
        # Should have all required fields
        required_fields = ['year', 'month', 'month_name', 'day', 'lunar_phase', 'waxing', 'day_of_week']
        for field in required_fields:
            self.assertIn(field, myanmar_date)
        
        # Year should be reasonable (Myanmar era started in 638 CE)
        self.assertTrue(myanmar_date['year'] > 1000)
        
        # Month should be 1-12
        self.assertTrue(1 <= myanmar_date['month'] <= 12)
        
        # Day should be reasonable
        self.assertTrue(1 <= myanmar_date['day'] <= 30)
        
        # Month name should be in Myanmar months list
        self.assertIn(myanmar_date['month_name'], self.calendar.MYANMAR_MONTHS)
        
    def test_myanmar_month_names(self):
        """Test Myanmar month names"""
        self.assertEqual(len(self.calendar.MYANMAR_MONTHS), 12)
        
        # Check specific months
        self.assertEqual(self.calendar.MYANMAR_MONTHS[0], "တန်ခူး")  # Tagu
        self.assertEqual(self.calendar.MYANMAR_MONTHS[3], "ဝါဆို")   # Waso
        
    def test_myanmar_day_names(self):
        """Test Myanmar day names"""
        self.assertEqual(len(self.calendar.MYANMAR_DAYS), 7)
        
        # Check specific days
        self.assertEqual(self.calendar.MYANMAR_DAYS[0], "တနင်ဂါ")    # Tuesday
        self.assertEqual(self.calendar.MYANMAR_DAYS[6], "တနင်္လာ")   # Monday
        
    def test_lunar_mansion_calculation(self):
        """Test lunar mansion (nakshatra) calculation"""
        jd = self.astro_calc.julian_day_number(self.test_date_1)
        nakshatra_en, nakshatra_mm = self.calendar.calculate_lunar_mansion(jd)
        
        # Should return valid nakshatra names
        self.assertIsInstance(nakshatra_en, str)
        self.assertIsInstance(nakshatra_mm, str)
        self.assertTrue(len(nakshatra_en) > 0)
        self.assertTrue(len(nakshatra_mm) > 0)
        
    def test_myanmar_numerals(self):
        """Test Myanmar numeral conversion"""
        # Test basic numbers
        self.assertEqual(self.calendar.get_myanmar_numeral(0), "၀")
        self.assertEqual(self.calendar.get_myanmar_numeral(1), "၁")
        self.assertEqual(self.calendar.get_myanmar_numeral(9), "၉")
        
        # Test multi-digit numbers
        self.assertEqual(self.calendar.get_myanmar_numeral(12), "၁၂")
        self.assertEqual(self.calendar.get_myanmar_numeral(2023), "၂၀၂၃")
        
    def test_auspicious_times(self):
        """Test auspicious time calculations"""
        # Test for Yangon coordinates
        latitude, longitude = 16.8661, 96.1951
        auspicious_times = self.calendar.get_auspicious_times(
            self.test_date_1, latitude, longitude
        )
        
        # Should have all 8 traditional time periods
        expected_periods = ['နေထွက်', 'နေတက်', 'မွန်းတည့်', 'နေလွဲ', 'နေဝင်', 'ညည့်', 'သန်းခေါင်', 'သန်းလွဲ']
        
        for period in expected_periods:
            self.assertIn(period, auspicious_times)
            # Each time should be in HH:MM format
            time_str = auspicious_times[period]
            self.assertRegex(time_str, r'\d{2}:\d{2}')
            
    def test_sabbath_days(self):
        """Test Uposatha (sabbath) day calculations"""
        sabbath_days = self.calendar.calculate_sabbath_days(1385, 1)  # Myanmar year and month
        
        # Should return list of days
        self.assertIsInstance(sabbath_days, list)
        self.assertEqual(len(sabbath_days), 4)  # 4 sabbath days per month
        
        # All days should be valid (1-30)
        for day in sabbath_days:
            self.assertTrue(1 <= day <= 30)
            
    def test_year_animal(self):
        """Test animal year calculation"""
        animal_en, animal_mm = self.calendar.get_year_animal(1385)  # Myanmar year
        
        # Should return valid animal names
        self.assertIsInstance(animal_en, str)
        self.assertIsInstance(animal_mm, str)
        
        # Should be one of the 12 animals
        animals_en = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake",
                     "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
        animals_mm = ["ကြွက်", "နွား", "ကျား", "ယုန်", "နဂါး", "မြွေ",
                     "မြင်း", "ဆိတ်", "မျောက်", "ကြက်", "ခွေး", "ဝက်"]
        
        self.assertIn(animal_en, animals_en)
        self.assertIn(animal_mm, animals_mm)


class TestMyanmarCalendarAccuracy(unittest.TestCase):
    """Test Myanmar calendar accuracy against known dates"""
    
    def setUp(self):
        self.calendar = MyanmarCalendarSystem()
        
    def test_thingyan_calculation(self):
        """Test Thingyan (Myanmar New Year) calculation"""
        # Test for a known year
        thingyan_info = self.calendar.calculate_thingyan(1385)  # Myanmar year
        
        # Should have all required dates
        self.assertIn('thingyan_start', thingyan_info)
        self.assertIn('thingyan_end', thingyan_info)
        self.assertIn('new_year', thingyan_info)
        
        # Dates should be in April
        for date_key in thingyan_info:
            date_obj = thingyan_info[date_key]
            self.assertEqual(date_obj.month, 4)
            self.assertTrue(10 <= date_obj.day <= 20)  # Usually mid-April
            
    def test_lunar_phase_consistency(self):
        """Test lunar phase calculation consistency"""
        # Test multiple dates to ensure consistency
        test_dates = [
            datetime(2023, 1, 1),
            datetime(2023, 6, 15),
            datetime(2023, 12, 31)
        ]
        
        for test_date in test_dates:
            myanmar_date = self.calendar.gregorian_to_myanmar(test_date)
            
            # Lunar phase should be either လဆန်း or လဆုတ်
            self.assertIn(myanmar_date['lunar_phase'], ['လဆန်း', 'လဆုတ်'])
            
            # Waxing should be boolean
            self.assertIsInstance(myanmar_date['waxing'], bool)
            
            # If waxing, phase should be လဆန်း
            if myanmar_date['waxing']:
                self.assertEqual(myanmar_date['lunar_phase'], 'လဆန်း')
            else:
                self.assertEqual(myanmar_date['lunar_phase'], 'လဆုတ်')


if __name__ == '__main__':
    unittest.main(verbosity=2)
