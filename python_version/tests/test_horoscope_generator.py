"""
Unit tests for horoscope generation
Tests the complete horoscope generation functionality
"""

import unittest
from datetime import datetime
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from core.horoscope_generator import HoroscopeGenerator
from data.cities import myanmar_cities


class TestHoroscopeGenerator(unittest.TestCase):
    """Test cases for horoscope generation"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.horoscope_gen = HoroscopeGenerator()
        
        # Test birth data
        self.test_birth_date = datetime(1990, 4, 17, 6, 30, 0)
        self.test_birth_place = "Yangon"
        
    def test_complete_horoscope_generation(self):
        """Test complete horoscope generation"""
        horoscope = self.horoscope_gen.generate_complete_horoscope(
            self.test_birth_date, self.test_birth_place
        )
        
        # Should have all major sections
        required_sections = [
            'birth_info', 'myanmar_calendar', 'ascendant', 'planets',
            'houses', 'birth_nakshatra', 'lunar_mansion', 'auspicious_times'
        ]
        
        for section in required_sections:
            self.assertIn(section, horoscope)
            
    def test_birth_info_accuracy(self):
        """Test birth information accuracy"""
        horoscope = self.horoscope_gen.generate_complete_horoscope(
            self.test_birth_date, self.test_birth_place
        )
        
        birth_info = horoscope['birth_info']
        
        # Check basic information
        self.assertEqual(birth_info['datetime'], self.test_birth_date)
        self.assertEqual(birth_info['place'], self.test_birth_place)
        self.assertIsInstance(birth_info['latitude'], float)
        self.assertIsInstance(birth_info['longitude'], float)
        self.assertIsInstance(birth_info['julian_day'], float)
        
    def test_ascendant_calculation(self):
        """Test ascendant calculation"""
        horoscope = self.horoscope_gen.generate_complete_horoscope(
            self.test_birth_date, self.test_birth_place
        )
        
        ascendant = horoscope['ascendant']
        
        # Should have all required fields
        required_fields = ['longitude', 'sign_en', 'sign_mm', 'degree_in_sign', 'local_sidereal_time']
        for field in required_fields:
            self.assertIn(field, ascendant)
            
        # Longitude should be 0-360
        self.assertTrue(0 <= ascendant['longitude'] < 360)
        
        # Degree in sign should be 0-30
        self.assertTrue(0 <= ascendant['degree_in_sign'] < 30)
        
    def test_planetary_positions(self):
        """Test planetary position calculations"""
        horoscope = self.horoscope_gen.generate_complete_horoscope(
            self.test_birth_date, self.test_birth_place
        )
        
        planets = horoscope['planets']
        
        # Should have all 9 planets
        expected_planets = ['Sun', 'Moon', 'Mars', 'Mercury', 'Jupiter', 'Venus', 'Saturn', 'Rahu', 'Ketu']
        for planet in expected_planets:
            self.assertIn(planet, planets)
            
            planet_data = planets[planet]
            
            # Each planet should have required fields
            required_fields = ['longitude', 'sign_en', 'sign_mm', 'degree_in_sign', 'retrograde']
            for field in required_fields:
                self.assertIn(field, planet_data)
                
            # Longitude should be 0-360
            self.assertTrue(0 <= planet_data['longitude'] < 360)
            
            # Degree in sign should be 0-30
            self.assertTrue(0 <= planet_data['degree_in_sign'] < 30)
            
    def test_house_calculations(self):
        """Test house calculations"""
        horoscope = self.horoscope_gen.generate_complete_horoscope(
            self.test_birth_date, self.test_birth_place
        )
        
        houses = horoscope['houses']
        
        # Should have 12 houses
        self.assertEqual(len(houses), 12)
        
        for house_num in range(1, 13):
            self.assertIn(house_num, houses)
            
            house_data = houses[house_num]
            
            # Each house should have required fields
            required_fields = ['start_longitude', 'end_longitude', 'sign_en', 'sign_mm', 'planets', 'house_name_en', 'house_name_mm']
            for field in required_fields:
                self.assertIn(field, house_data)
                
            # Planets should be a list
            self.assertIsInstance(house_data['planets'], list)
            
    def test_nakshatra_calculation(self):
        """Test birth nakshatra calculation"""
        horoscope = self.horoscope_gen.generate_complete_horoscope(
            self.test_birth_date, self.test_birth_place
        )
        
        nakshatra = horoscope['birth_nakshatra']
        
        # Should have required fields
        required_fields = ['name_en', 'name_mm', 'lord', 'lord_mm', 'index', 'pada']
        for field in required_fields:
            self.assertIn(field, nakshatra)
            
        # Index should be 1-27
        self.assertTrue(1 <= nakshatra['index'] <= 27)
        
        # Pada should be 1-4
        self.assertTrue(1 <= nakshatra['pada'] <= 4)
        
    def test_dasha_periods(self):
        """Test dasha period calculations"""
        horoscope = self.horoscope_gen.generate_complete_horoscope(
            self.test_birth_date, self.test_birth_place
        )
        
        if 'dasha_periods' in horoscope:
            dasha_periods = horoscope['dasha_periods']
            
            # Should have periods and current_dasha
            self.assertIn('periods', dasha_periods)
            self.assertIn('current_dasha', dasha_periods)
            
            periods = dasha_periods['periods']
            self.assertIsInstance(periods, list)
            self.assertTrue(len(periods) > 0)
            
            # Each period should have required fields
            for period in periods:
                required_fields = ['dasha', 'dasha_mm', 'start_date', 'end_date', 'years']
                for field in required_fields:
                    self.assertIn(field, period)
                    
    def test_different_birth_locations(self):
        """Test horoscope generation for different locations"""
        cities_to_test = ['Yangon', 'Mandalay', 'Naypyidaw']
        
        for city in cities_to_test:
            horoscope = self.horoscope_gen.generate_complete_horoscope(
                self.test_birth_date, city
            )
            
            # Should successfully generate horoscope for each city
            self.assertIn('birth_info', horoscope)
            self.assertEqual(horoscope['birth_info']['place'], city)
            
    def test_custom_coordinates(self):
        """Test horoscope generation with custom coordinates"""
        # Test with Bagan coordinates
        latitude, longitude = 21.1717, 94.8574
        
        horoscope = self.horoscope_gen.generate_complete_horoscope(
            self.test_birth_date, "Custom Location", latitude, longitude
        )
        
        birth_info = horoscope['birth_info']
        self.assertAlmostEqual(birth_info['latitude'], latitude, places=4)
        self.assertAlmostEqual(birth_info['longitude'], longitude, places=4)


class TestHoroscopeAccuracy(unittest.TestCase):
    """Test horoscope accuracy and consistency"""
    
    def setUp(self):
        self.horoscope_gen = HoroscopeGenerator()
        
    def test_planetary_strength_calculation(self):
        """Test planetary strength calculations"""
        test_date = datetime(2000, 1, 1, 12, 0, 0)
        horoscope = self.horoscope_gen.generate_complete_horoscope(test_date, "Yangon")
        
        if 'planetary_strength' in horoscope:
            strength = horoscope['planetary_strength']
            
            # Should have strength for major planets
            for planet in ['Sun', 'Moon', 'Mars', 'Mercury', 'Jupiter', 'Venus', 'Saturn']:
                if planet in strength:
                    planet_strength = strength[planet]
                    
                    # Should have different strength components
                    self.assertIn('total', planet_strength)
                    self.assertIsInstance(planet_strength['total'], (int, float))
                    self.assertTrue(planet_strength['total'] > 0)
                    
    def test_yoga_detection(self):
        """Test yoga (special combination) detection"""
        test_date = datetime(1990, 4, 17, 6, 30, 0)
        horoscope = self.horoscope_gen.generate_complete_horoscope(test_date, "Yangon")
        
        if 'yogas' in horoscope:
            yogas = horoscope['yogas']
            self.assertIsInstance(yogas, list)
            
            # Each yoga should have required fields
            for yoga in yogas:
                required_fields = ['name_en', 'name_mm', 'description', 'description_mm']
                for field in required_fields:
                    self.assertIn(field, yoga)
                    
    def test_prediction_generation(self):
        """Test astrological prediction generation"""
        test_date = datetime(1990, 4, 17, 6, 30, 0)
        horoscope = self.horoscope_gen.generate_complete_horoscope(test_date, "Yangon")
        
        if 'predictions' in horoscope:
            predictions = horoscope['predictions']
            self.assertIsInstance(predictions, dict)
            
            # Should have different prediction categories
            expected_categories = ['personality', 'career', 'relationships', 'health', 'general']
            for category in expected_categories:
                if category in predictions:
                    self.assertIsInstance(predictions[category], list)
                    
    def test_consistency_across_time_zones(self):
        """Test consistency of calculations across different time zones"""
        # Same moment in time, different locations
        base_date = datetime(2000, 1, 1, 12, 0, 0)
        
        horoscope1 = self.horoscope_gen.generate_complete_horoscope(base_date, "Yangon")
        horoscope2 = self.horoscope_gen.generate_complete_horoscope(base_date, "Mandalay")
        
        # Planetary positions should be very similar (within 1 degree)
        for planet in horoscope1['planets']:
            if planet in horoscope2['planets']:
                long1 = horoscope1['planets'][planet]['longitude']
                long2 = horoscope2['planets'][planet]['longitude']
                
                diff = abs(long1 - long2)
                if diff > 180:
                    diff = 360 - diff
                    
                self.assertTrue(diff < 1, f"Planet {planet} position differs too much: {diff} degrees")


if __name__ == '__main__':
    unittest.main(verbosity=2)
