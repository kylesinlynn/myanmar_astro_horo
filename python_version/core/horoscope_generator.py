"""
Horoscope Generation Engine
Based on traditional Myanmar astrology and Surya Siddhanta calculations

This module generates complete horoscopes with planetary positions,
house calculations, and astrological interpretations.
"""

import math
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Any
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from core.astronomical_calculations import AstronomicalCalculations
from core.calendar_system import MyanmarCalendarSystem
from core.nakshatra_system import NakshatraSystem
from data.cities import myanmar_cities


class HoroscopeGenerator:
    """Complete horoscope generation system"""
    
    def __init__(self):
        self.astro_calc = AstronomicalCalculations()
        self.calendar = MyanmarCalendarSystem()
        self.nakshatra = NakshatraSystem()
        
        # House system (12 houses in Vedic astrology)
        self.house_names = [
            "First House (Ascendant)", "Second House", "Third House",
            "Fourth House", "Fifth House", "Sixth House",
            "Seventh House", "Eighth House", "Ninth House",
            "Tenth House", "Eleventh House", "Twelfth House"
        ]
        
        self.house_names_mm = [
            "ပထမအိမ် (လဂ်နာ)", "ဒုတိယအိမ်", "တတိယအိမ်",
            "စတုတ္ထအိမ်", "ပဉ္စမအိမ်", "ဆဋ္ဌမအိမ်",
            "သတ္တမအိမ်", "အဋ္ဌမအိမ်", "နဝမအိမ်",
            "ဒသမအိမ်", "ဧကာဒသမအိမ်", "ဒွါဒသမအိမ်"
        ]
        
        # Planet names in English and Myanmar
        self.planets = {
            'Sun': 'နေ', 'Moon': 'လ', 'Mars': 'အင်္ဂါ', 'Mercury': 'ဗုဒ္ဓဟူး',
            'Jupiter': 'ကြာသပတေး', 'Venus': 'သုကြ', 'Saturn': 'စနေ',
            'Rahu': 'ရာဟု', 'Ketu': 'ကေတု'
        }
    
    def generate_complete_horoscope(self, 
                                  birth_datetime: datetime,
                                  birth_place: str,
                                  latitude: float = None,
                                  longitude: float = None) -> Dict[str, Any]:
        """
        Generate a complete horoscope chart
        Equivalent to the main VB6 horoscope generation functions
        """
        # Get location coordinates
        if latitude is None or longitude is None:
            city_info = myanmar_cities.get_city_info(birth_place)
            if city_info:
                latitude = city_info['latitude']
                longitude = city_info['longitude']
            else:
                # Default to Yangon if city not found
                latitude, longitude = 16.8661, 96.1951
        
        jd = self.astro_calc.julian_day_number(birth_datetime)
        
        # Basic information
        horoscope = {
            'birth_info': {
                'datetime': birth_datetime,
                'place': birth_place,
                'latitude': latitude,
                'longitude': longitude,
                'julian_day': jd
            }
        }
        
        # Myanmar calendar information
        horoscope['myanmar_calendar'] = self.calendar.gregorian_to_myanmar(birth_datetime)
        
        # Calculate Ascendant (Rising Sign)
        ascendant = self.calculate_ascendant(jd, latitude, longitude)
        horoscope['ascendant'] = ascendant
        
        # Calculate planetary positions
        horoscope['planets'] = self.calculate_all_planetary_positions(jd)
        
        # Calculate houses
        horoscope['houses'] = self.calculate_houses(ascendant['longitude'], horoscope['planets'])
        
        # Birth nakshatra
        horoscope['birth_nakshatra'] = self.nakshatra.calculate_birth_nakshatra(birth_datetime)
        
        # Lunar mansion at birth
        horoscope['lunar_mansion'] = self.calendar.calculate_lunar_mansion(jd)
        
        # Auspicious times for birth date
        horoscope['auspicious_times'] = self.calendar.get_auspicious_times(
            birth_datetime, latitude, longitude
        )
        
        # Dasha periods (planetary periods)
        horoscope['dasha_periods'] = self.calculate_dasha_periods(
            horoscope['birth_nakshatra'], birth_datetime
        )
        
        # Yogas (special combinations)
        horoscope['yogas'] = self.calculate_yogas(horoscope['planets'], ascendant)
        
        # Strength analysis
        horoscope['planetary_strength'] = self.calculate_planetary_strength(
            horoscope['planets'], jd
        )
        
        # Generate predictions
        horoscope['predictions'] = self.generate_predictions(horoscope)
        
        return horoscope
    
    def calculate_ascendant(self, jd: float, latitude: float, longitude: float) -> Dict[str, Any]:
        """Calculate the Ascendant (Lagna) - the rising sign at birth"""
        # Calculate local sidereal time
        lst = self.astro_calc.sidereal_time(jd, longitude)
        
        # Calculate ascendant longitude
        lat_rad = math.radians(latitude)
        lst_rad = math.radians(lst)
        
        # Simplified ascendant calculation
        # In practice, this requires more complex spherical trigonometry
        ascendant_longitude = (lst + 180) % 360
        
        # Get sign information
        sign_en, sign_mm = self.astro_calc.get_rashi(ascendant_longitude)
        
        return {
            'longitude': ascendant_longitude,
            'sign_en': sign_en,
            'sign_mm': sign_mm,
            'degree_in_sign': ascendant_longitude % 30,
            'local_sidereal_time': lst
        }
    
    def calculate_all_planetary_positions(self, jd: float) -> Dict[str, Dict[str, Any]]:
        """Calculate positions of all planets"""
        positions = {}
        
        # Sun
        sun_longitude = self.astro_calc.true_longitude_sun(jd)
        sun_sign_en, sun_sign_mm = self.astro_calc.get_rashi(sun_longitude)
        positions['Sun'] = {
            'longitude': sun_longitude,
            'sign_en': sun_sign_en,
            'sign_mm': sun_sign_mm,
            'degree_in_sign': sun_longitude % 30,
            'retrograde': False
        }
        
        # Moon
        moon_longitude = self.astro_calc.mean_longitude_moon(jd)
        moon_sign_en, moon_sign_mm = self.astro_calc.get_rashi(moon_longitude)
        positions['Moon'] = {
            'longitude': moon_longitude,
            'sign_en': moon_sign_en,
            'sign_mm': moon_sign_mm,
            'degree_in_sign': moon_longitude % 30,
            'retrograde': False
        }
        
        # Other planets (simplified calculations)
        planetary_positions = self.astro_calc.planetary_positions(jd)
        
        for planet, longitude in planetary_positions.items():
            sign_en, sign_mm = self.astro_calc.get_rashi(longitude)
            positions[planet] = {
                'longitude': longitude,
                'sign_en': sign_en,
                'sign_mm': sign_mm,
                'degree_in_sign': longitude % 30,
                'retrograde': self.is_planet_retrograde(planet, jd)
            }
        
        # Calculate Rahu and Ketu (lunar nodes)
        rahu_longitude = self.calculate_rahu_position(jd)
        ketu_longitude = (rahu_longitude + 180) % 360
        
        for node, longitude in [('Rahu', rahu_longitude), ('Ketu', ketu_longitude)]:
            sign_en, sign_mm = self.astro_calc.get_rashi(longitude)
            positions[node] = {
                'longitude': longitude,
                'sign_en': sign_en,
                'sign_mm': sign_mm,
                'degree_in_sign': longitude % 30,
                'retrograde': True  # Nodes are always retrograde
            }
        
        return positions
    
    def calculate_rahu_position(self, jd: float) -> float:
        """Calculate Rahu (North Lunar Node) position"""
        t = (jd - 2451545.0) / 36525.0
        
        # Mean longitude of ascending node
        omega = 125.0445479 - 1934.1362891 * t + 0.0020754 * t * t
        omega += 0.00000165 * t * t * t
        
        return self.astro_calc.normalize_angle(omega)
    
    def is_planet_retrograde(self, planet: str, jd: float) -> bool:
        """Check if planet is retrograde (simplified)"""
        # This is a simplified check - actual retrograde calculation is complex
        if planet in ['Sun', 'Moon']:
            return False
        
        # Check motion by comparing positions over small time interval
        pos1 = self.astro_calc.planetary_positions(jd - 1).get(planet, 0)
        pos2 = self.astro_calc.planetary_positions(jd + 1).get(planet, 0)
        
        # Handle 360-degree wraparound
        diff = pos2 - pos1
        if diff > 180:
            diff -= 360
        elif diff < -180:
            diff += 360
        
        return diff < 0
    
    def calculate_houses(self, ascendant_longitude: float, planets: Dict[str, Dict[str, Any]]) -> Dict[int, Dict[str, Any]]:
        """Calculate the 12 houses and their occupants"""
        houses = {}
        
        for house_num in range(1, 13):
            # Each house spans 30 degrees from ascendant
            house_start = (ascendant_longitude + (house_num - 1) * 30) % 360
            house_end = (house_start + 30) % 360
            
            # Find planets in this house
            planets_in_house = []
            for planet_name, planet_data in planets.items():
                planet_longitude = planet_data['longitude']
                
                # Check if planet is in this house
                if house_start <= house_end:
                    if house_start <= planet_longitude < house_end:
                        planets_in_house.append(planet_name)
                else:  # Handle wraparound at 360 degrees
                    if planet_longitude >= house_start or planet_longitude < house_end:
                        planets_in_house.append(planet_name)
            
            # Get house sign
            house_sign_en, house_sign_mm = self.astro_calc.get_rashi(house_start)
            
            houses[house_num] = {
                'start_longitude': house_start,
                'end_longitude': house_end,
                'sign_en': house_sign_en,
                'sign_mm': house_sign_mm,
                'planets': planets_in_house,
                'house_name_en': self.house_names[house_num - 1],
                'house_name_mm': self.house_names_mm[house_num - 1]
            }
        
        return houses
    
    def calculate_dasha_periods(self, birth_nakshatra: Dict[str, Any], birth_date: datetime) -> Dict[str, Any]:
        """
        Calculate Vimshottari Dasha periods
        Based on birth nakshatra and traditional 120-year cycle
        """
        nakshatra_index = birth_nakshatra['index']
        position_percent = birth_nakshatra['position_percent']
        
        # Dasha sequence and years
        dasha_sequence = ['Ketu', 'Venus', 'Sun', 'Moon', 'Mars', 'Rahu', 'Jupiter', 'Saturn', 'Mercury']
        dasha_years = {'Ketu': 7, 'Venus': 20, 'Sun': 6, 'Moon': 10, 'Mars': 7, 'Rahu': 18, 'Jupiter': 16, 'Saturn': 19, 'Mercury': 17}
        
        # Find starting dasha based on nakshatra
        starting_dasha_index = (nakshatra_index - 1) % 9
        starting_dasha = dasha_sequence[starting_dasha_index]
        
        # Calculate remaining years in starting dasha
        remaining_years = dasha_years[starting_dasha] * (100 - position_percent) / 100
        
        # Generate dasha periods
        periods = []
        current_date = birth_date
        
        # Add remaining period of birth dasha
        if remaining_years > 0:
            end_date = current_date + timedelta(days=remaining_years * 365.25)
            periods.append({
                'dasha': starting_dasha,
                'dasha_mm': self.planets.get(starting_dasha, starting_dasha),
                'start_date': current_date,
                'end_date': end_date,
                'years': remaining_years
            })
            current_date = end_date
        
        # Add subsequent dashas
        for i in range(1, 9):
            dasha_index = (starting_dasha_index + i) % 9
            dasha = dasha_sequence[dasha_index]
            years = dasha_years[dasha]
            
            end_date = current_date + timedelta(days=years * 365.25)
            periods.append({
                'dasha': dasha,
                'dasha_mm': self.planets.get(dasha, dasha),
                'start_date': current_date,
                'end_date': end_date,
                'years': years
            })
            current_date = end_date
        
        return {
            'periods': periods,
            'current_dasha': self.get_current_dasha(periods, datetime.now())
        }
    
    def get_current_dasha(self, periods: List[Dict[str, Any]], current_date: datetime) -> Dict[str, Any]:
        """Find the current dasha period"""
        for period in periods:
            if period['start_date'] <= current_date <= period['end_date']:
                return period
        return periods[0]  # Default to first period
    
    def calculate_yogas(self, planets: Dict[str, Dict[str, Any]], ascendant: Dict[str, Any]) -> List[Dict[str, str]]:
        """
        Calculate special yogas (planetary combinations)
        Based on traditional Vedic astrology
        """
        yogas = []
        
        # Raja Yoga - benefic planets in kendras and trikonas
        kendras = [1, 4, 7, 10]  # Angular houses
        trikonas = [1, 5, 9]     # Trinal houses
        
        # Check for Gaja Kesari Yoga (Moon-Jupiter combination)
        moon_sign = int(planets['Moon']['longitude'] / 30)
        jupiter_sign = int(planets['Jupiter']['longitude'] / 30)
        
        if abs(moon_sign - jupiter_sign) in [0, 3, 6, 9]:
            yogas.append({
                'name_en': 'Gaja Kesari Yoga',
                'name_mm': 'ဂဇကေသရီယောဂ',
                'description': 'Auspicious combination of Moon and Jupiter',
                'description_mm': 'လနှင့် ကြာသပတေး၏ မင်္ဂလာရှိသော ပေါင်းစပ်မှု'
            })
        
        # Check for Chandra Mangal Yoga (Moon-Mars combination)
        mars_sign = int(planets['Mars']['longitude'] / 30)
        if abs(moon_sign - mars_sign) in [0, 6]:
            yogas.append({
                'name_en': 'Chandra Mangal Yoga',
                'name_mm': 'စန္ဒြမင်္ဂလယောဂ',
                'description': 'Moon-Mars combination for wealth',
                'description_mm': 'လနှင့် အင်္ဂါ၏ ကြွယ်ဝမှုအတွက် ပေါင်းစပ်မှု'
            })
        
        # Add more yoga calculations as needed
        
        return yogas
    
    def calculate_planetary_strength(self, planets: Dict[str, Dict[str, Any]], jd: float) -> Dict[str, Dict[str, float]]:
        """Calculate strength of planets (Shadbala)"""
        strength = {}
        
        for planet_name, planet_data in planets.items():
            if planet_name in ['Rahu', 'Ketu']:
                continue  # Skip nodes for strength calculation
            
            longitude = planet_data['longitude']
            sign_index = int(longitude / 30)
            
            # Positional strength (simplified)
            positional_strength = 50.0  # Base strength
            
            # Exaltation/Debilitation strength
            exaltation_signs = {
                'Sun': 0, 'Moon': 1, 'Mars': 9, 'Mercury': 5,
                'Jupiter': 3, 'Venus': 11, 'Saturn': 6
            }
            
            if planet_name in exaltation_signs:
                if sign_index == exaltation_signs[planet_name]:
                    positional_strength += 30  # Exalted
                elif sign_index == (exaltation_signs[planet_name] + 6) % 12:
                    positional_strength -= 30  # Debilitated
            
            # Directional strength (simplified)
            directional_strength = 25.0
            
            # Temporal strength (day/night)
            temporal_strength = 25.0
            
            strength[planet_name] = {
                'positional': positional_strength,
                'directional': directional_strength,
                'temporal': temporal_strength,
                'total': positional_strength + directional_strength + temporal_strength
            }
        
        return strength
    
    def generate_predictions(self, horoscope: Dict[str, Any]) -> Dict[str, List[str]]:
        """Generate basic astrological predictions"""
        predictions = {
            'personality': [],
            'career': [],
            'relationships': [],
            'health': [],
            'general': []
        }
        
        # Ascendant-based predictions
        ascendant_sign = horoscope['ascendant']['sign_en']
        
        personality_traits = {
            'Aries': ['Dynamic and energetic', 'Natural leader', 'Quick decision maker'],
            'Taurus': ['Stable and reliable', 'Practical approach', 'Strong determination'],
            'Gemini': ['Communicative and versatile', 'Quick learner', 'Adaptable nature'],
            'Cancer': ['Emotional and intuitive', 'Caring personality', 'Strong family bonds'],
            'Leo': ['Confident and generous', 'Creative abilities', 'Natural performer'],
            'Virgo': ['Analytical and detail-oriented', 'Helpful nature', 'Perfectionist tendencies'],
            'Libra': ['Balanced and diplomatic', 'Artistic inclinations', 'Harmony seeker'],
            'Scorpio': ['Intense and mysterious', 'Strong willpower', 'Transformative nature'],
            'Sagittarius': ['Optimistic and adventurous', 'Philosophical mind', 'Freedom lover'],
            'Capricorn': ['Ambitious and disciplined', 'Practical goals', 'Strong work ethic'],
            'Aquarius': ['Independent and innovative', 'Humanitarian ideals', 'Unique perspective'],
            'Pisces': ['Compassionate and intuitive', 'Artistic talents', 'Spiritual inclinations']
        }
        
        if ascendant_sign in personality_traits:
            predictions['personality'] = personality_traits[ascendant_sign]
        
        # Add more prediction logic based on planetary positions, yogas, etc.
        
        return predictions
