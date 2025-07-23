"""
Myanmar Astro Horo - Core Astronomical Calculations
Based on Surya Siddhanta theory and original VB6 implementation

This module contains the core astronomical calculation functions
translated from the original VB6 modules (Kdata1.bas through Kdata7.bas)
"""

import math
from datetime import datetime, timedelta
from typing import Tuple, Dict, List


class AstronomicalCalculations:
    """Core astronomical calculations based on Surya Siddhanta"""
    
    def __init__(self):
        # Constants from Surya Siddhanta
        self.SIDEREAL_YEAR = 365.25636  # Sidereal year in days
        self.TROPICAL_YEAR = 365.24219  # Tropical year in days
        self.LUNAR_MONTH = 29.53059     # Synodic month in days
        self.EARTH_RADIUS = 6371.0      # Earth radius in km
        
        # Myanmar specific constants
        self.MYANMAR_EPOCH = datetime(638, 3, 22)  # Myanmar calendar epoch
        # Note: Kali Yuga start is before datetime range, use Julian Day Number instead
        self.KALI_YUGA_START_JD = 588465.5  # Kali Yuga start as Julian Day Number
        
    def julian_day_number(self, date: datetime) -> float:
        """
        Calculate Julian Day Number for given date
        Equivalent to VB6 Kp() function
        """
        year = date.year
        month = date.month
        day = date.day
        hour = date.hour
        minute = date.minute
        second = date.second
        
        # Convert to Julian calendar if before 1582
        if year < 1582 or (year == 1582 and month < 10) or (year == 1582 and month == 10 and day < 15):
            # Julian calendar
            a = (14 - month) // 12
            y = year - a
            m = month + 12 * a - 3
            jdn = day + (153 * m + 2) // 5 + 365 * y + y // 4 - 32083
        else:
            # Gregorian calendar
            a = (14 - month) // 12
            y = year - a
            m = month + 12 * a - 3
            jdn = day + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045
        
        # Add fractional day
        fraction = (hour + minute / 60.0 + second / 3600.0) / 24.0
        return jdn + fraction
    
    def mean_longitude_sun(self, jd: float) -> float:
        """
        Calculate mean longitude of the Sun
        Based on Surya Siddhanta calculations
        """
        t = (jd - 2451545.0) / 36525.0  # Julian centuries from J2000.0
        
        # Mean longitude in degrees
        l0 = 280.46646 + 36000.76983 * t + 0.0003032 * t * t
        return self.normalize_angle(l0)
    
    def mean_anomaly_sun(self, jd: float) -> float:
        """Calculate mean anomaly of the Sun"""
        t = (jd - 2451545.0) / 36525.0
        m = 357.52911 + 35999.05029 * t - 0.0001537 * t * t
        return self.normalize_angle(m)
    
    def equation_of_center_sun(self, mean_anomaly: float) -> float:
        """Calculate equation of center for the Sun"""
        m_rad = math.radians(mean_anomaly)
        c = (1.914602 - 0.004817 * 0 - 0.000014 * 0 * 0) * math.sin(m_rad)
        c += (0.019993 - 0.000101 * 0) * math.sin(2 * m_rad)
        c += 0.000289 * math.sin(3 * m_rad)
        return c
    
    def true_longitude_sun(self, jd: float) -> float:
        """Calculate true longitude of the Sun"""
        mean_long = self.mean_longitude_sun(jd)
        mean_anom = self.mean_anomaly_sun(jd)
        equation_center = self.equation_of_center_sun(mean_anom)
        return self.normalize_angle(mean_long + equation_center)
    
    def mean_longitude_moon(self, jd: float) -> float:
        """Calculate mean longitude of the Moon"""
        t = (jd - 2451545.0) / 36525.0
        l = 218.3164477 + 481267.88123421 * t - 0.0015786 * t * t
        l += 0.00000538 * t * t * t - 0.00000006 * t * t * t * t
        return self.normalize_angle(l)
    
    def lunar_elongation(self, jd: float) -> float:
        """Calculate lunar elongation (distance from Sun)"""
        sun_long = self.true_longitude_sun(jd)
        moon_long = self.mean_longitude_moon(jd)
        elongation = moon_long - sun_long
        return self.normalize_angle(elongation)
    
    def lunar_phase(self, jd: float) -> Tuple[str, float]:
        """
        Calculate lunar phase
        Returns phase name and illumination percentage
        """
        elongation = self.lunar_elongation(jd)
        
        # Calculate illumination percentage
        illumination = (1 + math.cos(math.radians(elongation))) / 2 * 100
        
        # Determine phase name
        if elongation < 45 or elongation > 315:
            phase = "New Moon"
        elif 45 <= elongation < 135:
            phase = "First Quarter"
        elif 135 <= elongation < 225:
            phase = "Full Moon"
        else:
            phase = "Last Quarter"
        
        return phase, illumination
    
    def sidereal_time(self, jd: float, longitude: float = 0) -> float:
        """
        Calculate sidereal time for given JD and longitude
        Equivalent to VB6 time calculation functions
        """
        t = (jd - 2451545.0) / 36525.0
        
        # Greenwich Mean Sidereal Time
        gmst = 280.46061837 + 360.98564736629 * (jd - 2451545.0)
        gmst += 0.000387933 * t * t - t * t * t / 38710000.0
        
        # Local sidereal time
        lst = gmst + longitude
        return self.normalize_angle(lst)
    
    def planetary_positions(self, jd: float) -> Dict[str, float]:
        """
        Calculate positions of planets
        Based on simplified planetary theory from Surya Siddhanta
        """
        t = (jd - 2451545.0) / 36525.0
        
        positions = {}
        
        # Mercury
        positions['Mercury'] = self.normalize_angle(252.25032 + 149472.67411 * t)
        
        # Venus  
        positions['Venus'] = self.normalize_angle(181.97973 + 58517.81539 * t)
        
        # Mars
        positions['Mars'] = self.normalize_angle(355.43299 + 19140.30268 * t)
        
        # Jupiter
        positions['Jupiter'] = self.normalize_angle(34.35151 + 3034.74612 * t)
        
        # Saturn
        positions['Saturn'] = self.normalize_angle(50.07744 + 1222.49362 * t)
        
        return positions
    
    def normalize_angle(self, angle: float) -> float:
        """Normalize angle to 0-360 degrees"""
        while angle < 0:
            angle += 360
        while angle >= 360:
            angle -= 360
        return angle
    
    def degrees_to_dms(self, degrees: float) -> Tuple[int, int, float]:
        """
        Convert decimal degrees to degrees, minutes, seconds
        Equivalent to VB6 DMS() function
        """
        d = int(degrees)
        m = int((degrees - d) * 60)
        s = ((degrees - d) * 60 - m) * 60
        return d, m, s
    
    def dms_to_degrees(self, degrees: int, minutes: int, seconds: float) -> float:
        """Convert degrees, minutes, seconds to decimal degrees"""
        return degrees + minutes / 60.0 + seconds / 3600.0
    
    def calculate_ayanamsa(self, jd: float) -> float:
        """
        Calculate Ayanamsa (precession correction)
        Based on Lahiri Ayanamsa system
        """
        t = (jd - 2451545.0) / 36525.0
        ayanamsa = 23.85 + 0.0139 * t
        return ayanamsa
    
    def tropical_to_sidereal(self, tropical_longitude: float, jd: float) -> float:
        """Convert tropical longitude to sidereal longitude"""
        ayanamsa = self.calculate_ayanamsa(jd)
        sidereal = tropical_longitude - ayanamsa
        return self.normalize_angle(sidereal)
    
    def get_rashi(self, longitude: float) -> Tuple[str, str]:
        """
        Get Rashi (zodiac sign) from longitude
        Returns English and Myanmar names
        """
        rashi_names_en = [
            "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
            "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
        ]
        
        rashi_names_mm = [
            "မိဿ", "ပြိဿ", "မေထုံ", "ကရကဋ်", "သိဟ်", "ကန်",
            "တူ", "ဗြိစ္ဆာ", "ဓနု", "မကာရ", "ကုံ", "မိန်"
        ]
        
        rashi_index = int(longitude / 30)
        return rashi_names_en[rashi_index], rashi_names_mm[rashi_index]
    
    def sunrise_sunset(self, jd: float, latitude: float, longitude: float) -> Tuple[float, float]:
        """
        Calculate sunrise and sunset times
        Based on astronomical algorithms
        """
        # Solar declination
        sun_long = self.true_longitude_sun(jd)
        declination = math.asin(math.sin(math.radians(23.45)) * 
                               math.sin(math.radians(sun_long)))
        
        # Hour angle
        lat_rad = math.radians(latitude)
        hour_angle = math.acos(-math.tan(lat_rad) * math.tan(declination))
        
        # Convert to hours
        sunrise = 12 - hour_angle * 12 / math.pi
        sunset = 12 + hour_angle * 12 / math.pi
        
        # Adjust for longitude
        time_correction = longitude / 15.0
        sunrise -= time_correction
        sunset -= time_correction
        
        return sunrise, sunset
