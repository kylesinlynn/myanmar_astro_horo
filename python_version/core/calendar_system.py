"""
Myanmar Calendar System Implementation
Based on traditional Myanmar calendar calculations from the original VB6 code

This module handles Myanmar calendar conversions, lunar calculations,
and traditional time systems used in Myanmar astrology.
"""

import math
from datetime import datetime, timedelta
from typing import Tuple, Dict, List
from .astronomical_calculations import AstronomicalCalculations


class MyanmarCalendarSystem:
    """Myanmar traditional calendar system implementation"""
    
    def __init__(self):
        self.astro_calc = AstronomicalCalculations()
        
        # Myanmar calendar constants
        self.MYANMAR_EPOCH = datetime(638, 3, 22)  # Myanmar Era start
        self.MYANMAR_MONTHS = [
            "တန်ခူး", "ကဆုန်", "နယုန်", "ဝါဆို", "ဝါခေါင်", "တော်သလင်း",
            "သီတင်းကျွတ်", "တန်ဆောင်မုန်း", "နတ်တော်", "ပြာသို", "တပေါင်း", "တပေါင်းလဆန်း"
        ]
        
        # Days of the week in Myanmar
        self.MYANMAR_DAYS = [
            "တနင်ဂါ", "ဗုဒ္ဓဟူး", "ကြာသပတေး", "သောကြာ", 
            "စနေ", "တနင်္ဂနွေ", "တနင်္လာ"
        ]
        
        # Myanmar numerals
        self.MYANMAR_NUMERALS = ["၀", "၁", "၂", "၃", "၄", "၅", "၆", "၇", "၈", "၉"]
        
    def gregorian_to_myanmar(self, date: datetime) -> Dict[str, any]:
        """
        Convert Gregorian date to Myanmar calendar
        Equivalent to VB6 calendar conversion functions
        """
        jd = self.astro_calc.julian_day_number(date)
        
        # Calculate Myanmar year
        myanmar_epoch_jd = self.astro_calc.julian_day_number(self.MYANMAR_EPOCH)
        days_since_epoch = jd - myanmar_epoch_jd
        myanmar_year = int(days_since_epoch / 365.25636) + 1
        
        # Calculate lunar month and day
        lunar_info = self.calculate_lunar_info(jd)
        
        return {
            'year': myanmar_year,
            'month': lunar_info['month'],
            'month_name': self.MYANMAR_MONTHS[lunar_info['month'] - 1],
            'day': lunar_info['day'],
            'lunar_phase': lunar_info['phase'],
            'waxing': lunar_info['waxing'],
            'day_of_week': self.MYANMAR_DAYS[date.weekday()],
            'myanmar_day_name': self.get_myanmar_day_name(date.weekday())
        }
    
    def calculate_lunar_info(self, jd: float) -> Dict[str, any]:
        """
        Calculate lunar month and day information
        Based on traditional Myanmar lunar calendar
        """
        # New moon calculation
        new_moon_jd = self.find_new_moon(jd)
        days_from_new_moon = jd - new_moon_jd
        
        # Determine lunar day
        lunar_day = int(days_from_new_moon) + 1
        
        # Determine if waxing or waning
        if lunar_day <= 15:
            waxing = True
            phase = "လဆန်း"
        else:
            waxing = False
            phase = "လဆုတ်"
            lunar_day = 30 - lunar_day + 1
        
        # Calculate lunar month
        lunar_month = self.calculate_lunar_month(jd)
        
        return {
            'month': lunar_month,
            'day': lunar_day,
            'phase': phase,
            'waxing': waxing,
            'new_moon_jd': new_moon_jd
        }
    
    def find_new_moon(self, jd: float) -> float:
        """Find the Julian day of the most recent new moon"""
        # Start from current JD and work backwards
        test_jd = jd
        while True:
            elongation = self.astro_calc.lunar_elongation(test_jd)
            if abs(elongation) < 1.0 or abs(elongation - 360) < 1.0:
                return test_jd
            test_jd -= 1.0
            if jd - test_jd > 30:  # Safety check
                break
        return jd
    
    def calculate_lunar_month(self, jd: float) -> int:
        """Calculate Myanmar lunar month number (1-12)"""
        # Simplified calculation based on solar longitude
        sun_longitude = self.astro_calc.true_longitude_sun(jd)
        month = int(sun_longitude / 30) + 1
        
        # Adjust for Myanmar calendar system
        month = ((month - 4) % 12) + 1
        return month
    
    def get_myanmar_day_name(self, weekday: int) -> str:
        """Get Myanmar day name with additional traditional information"""
        day_names = [
            "တနင်ဂါ", "ဗုဒ္ဓဟူး", "ကြာသပတေး", "သောကြာ",
            "စနေ", "တနင်္ဂနွေ", "တနင်္လာ"
        ]
        return day_names[weekday]
    
    def calculate_thingyan(self, myanmar_year: int) -> Dict[str, datetime]:
        """
        Calculate Thingyan (Myanmar New Year) dates
        Based on astronomical calculations
        """
        # Convert Myanmar year to Gregorian
        gregorian_year = myanmar_year + 638
        
        # Thingyan usually falls in mid-April
        # This is a simplified calculation
        thingyan_start = datetime(gregorian_year, 4, 13)
        thingyan_end = datetime(gregorian_year, 4, 16)
        new_year = datetime(gregorian_year, 4, 17)
        
        return {
            'thingyan_start': thingyan_start,
            'thingyan_end': thingyan_end,
            'new_year': new_year
        }
    
    def get_myanmar_numeral(self, number: int) -> str:
        """Convert Arabic numeral to Myanmar numeral"""
        if number == 0:
            return self.MYANMAR_NUMERALS[0]
        
        result = ""
        for digit in str(number):
            result += self.MYANMAR_NUMERALS[int(digit)]
        return result
    
    def calculate_sabbath_days(self, myanmar_year: int, month: int) -> List[int]:
        """
        Calculate Uposatha (Sabbath) days for a Myanmar month
        These are the 8th and 15th days of waxing and waning moon
        """
        return [8, 15, 23, 30]  # Traditional sabbath days
    
    def get_auspicious_times(self, date: datetime, latitude: float, longitude: float) -> Dict[str, str]:
        """
        Calculate auspicious times for the given date
        Based on traditional Myanmar astrology
        """
        jd = self.astro_calc.julian_day_number(date)
        sunrise, sunset = self.astro_calc.sunrise_sunset(jd, latitude, longitude)
        
        # Calculate traditional time periods
        day_length = sunset - sunrise
        night_length = 24 - day_length
        
        # Eight traditional time periods
        periods = {
            'နေထွက်': self.format_time(sunrise),  # Sunrise
            'နေတက်': self.format_time(sunrise + day_length * 0.125),  # 1st period
            'မွန်းတည့်': self.format_time(12.0),  # Noon
            'နေလွဲ': self.format_time(12.0 + day_length * 0.125),  # Afternoon
            'နေဝင်': self.format_time(sunset),  # Sunset
            'ညည့်': self.format_time(0.0),  # Midnight
            'သန်းခေါင်': self.format_time(2.0),  # 2 AM
            'သန်းလွဲ': self.format_time(3.0)   # 3 AM
        }
        
        return periods
    
    def format_time(self, hour_decimal: float) -> str:
        """Format decimal hour to HH:MM format"""
        hours = int(hour_decimal)
        minutes = int((hour_decimal - hours) * 60)
        return f"{hours:02d}:{minutes:02d}"
    
    def calculate_lunar_mansion(self, jd: float) -> Tuple[str, str]:
        """
        Calculate Nakshatra (lunar mansion) for given Julian day
        Returns English and Myanmar names
        """
        # Get moon's longitude
        moon_longitude = self.astro_calc.mean_longitude_moon(jd)
        
        # Convert to sidereal
        sidereal_longitude = self.astro_calc.tropical_to_sidereal(moon_longitude, jd)
        
        # Calculate Nakshatra (27 divisions of 13.33 degrees each)
        nakshatra_index = int(sidereal_longitude / 13.333333)
        
        nakshatra_names_en = [
            "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra",
            "Punarvasu", "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni",
            "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha", "Jyeshtha",
            "Mula", "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishta",
            "Shatabhisha", "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
        ]
        
        nakshatra_names_mm = [
            "အဿဝဏီ", "ဘရဏီ", "ကြတ္တိကာ", "ရောဟဏီ", "မိဂသီ", "အဒြ",
            "ပုဏ္ဏဖုသျှု", "ဖုသျှ", "အသလိဿ", "မာဃ", "ပြုဗ္ဗာဘရဂုဏ္ဏီ", "ဥတ္တရာဘရဂုဏ္ဏီ",
            "ဟဿဒ", "စိတြ", "သွာတိ", "ဝိသာခါ", "အနုရာဓ", "ဇေဋ္ဌ",
            "မူလ", "ပြုဗ္ဗာသဠ်", "ဥတ္တရာသဠ်", "သရဝဏ်", "ဓနသိဒ္ဓ",
            "သတ္တဘိသျှ", "ပြုဗ္ဗာပုရပိုက်", "ဥတ္တရာပုရပိုက်", "ရေဝတီ"
        ]
        
        return nakshatra_names_en[nakshatra_index], nakshatra_names_mm[nakshatra_index]
    
    def get_year_animal(self, myanmar_year: int) -> Tuple[str, str]:
        """
        Get the animal year for Myanmar calendar
        12-year cycle of animals
        """
        animals_en = [
            "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake",
            "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"
        ]
        
        animals_mm = [
            "ကြွက်", "နွား", "ကျား", "ယုန်", "နဂါး", "မြွေ",
            "မြင်း", "ဆိတ်", "မျောက်", "ကြက်", "ခွေး", "ဝက်"
        ]
        
        animal_index = myanmar_year % 12
        return animals_en[animal_index], animals_mm[animal_index]
