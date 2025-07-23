"""
Myanmar-specific astronomical and astrological data
Based on the original VB6 data dictionary files and traditional Myanmar astrology

This module contains all the Myanmar-specific data mappings, translations,
and astronomical constants used in traditional Myanmar horoscope calculations.
"""

from typing import Dict, List, Tuple


class MyanmarAstrologicalData:
    """Myanmar astrological data and mappings"""
    
    def __init__(self):
        # Zodiac signs in Myanmar (12 signs)
        self.rashi_names = {
            'en': ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
                   "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"],
            'mm': ["မိဿ", "ပြိဿ", "မေထုံ", "ကရကဋ်", "သိဟ်", "ကန်",
                   "တူ", "ဗြိစ္ဆာ", "ဓနု", "မကာရ", "ကုံ", "မိန်"]
        }
        
        # Days of the week
        self.weekdays = {
            'en': ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            'mm': ["တနင်္လာ", "တနင်ဂါ", "ဗုဒ္ဓဟူး", "ကြာသပတေး", "သောကြာ", "စနေ", "တနင်္ဂနွေ"]
        }
        
        # Planets in Myanmar astrology
        self.planets = {
            'en': ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn", "Rahu", "Ketu"],
            'mm': ["နေ", "လ", "အင်္ဂါ", "ဗုဒ္ဓဟူး", "ကြာသပတေး", "သုကြ", "စနေ", "ရာဟု", "ကေတု"]
        }
        
        # 27 Nakshatras (Lunar Mansions)
        self.nakshatras = {
            'en': [
                "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra",
                "Punarvasu", "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni",
                "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha", "Jyeshtha",
                "Mula", "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishta",
                "Shatabhisha", "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
            ],
            'mm': [
                "အဿဝဏီ", "ဘရဏီ", "ကြတ္တိကာ", "ရောဟဏီ", "မိဂသီ", "အဒြ",
                "ပုဏ္ဏဖုသျှု", "ဖုသျှ", "အသလိဿ", "မာဃ", "ပြုဗ္ဗာဘရဂုဏ္ဏီ", "ဥတ္တရာဘရဂုဏ္ဏီ",
                "ဟဿဒ", "စိတြ", "သွာတိ", "ဝိသာခါ", "အနုရာဓ", "ဇေဋ္ဌ",
                "မူလ", "ပြုဗ္ဗာသဠ်", "ဥတ္တရာသဠ်", "သရဝဏ်", "ဓနသိဒ္ဓ",
                "သတ္တဘိသျှ", "ပြုဗ္ဗာပုရပိုက်", "ဥတ္တရာပုရပိုက်", "ရေဝတီ"
            ]
        }
        
        # Myanmar months
        self.myanmar_months = [
            "တန်ခူး", "ကဆုန်", "နယုန်", "ဝါဆို", "ဝါခေါင်", "တော်သလင်း",
            "သီတင်းကျွတ်", "တန်ဆောင်မုန်း", "နတ်တော်", "ပြာသို", "တပေါင်း", "တပေါင်းလဆန်း"
        ]
        
        # Myanmar numerals
        self.myanmar_numerals = ["၀", "၁", "၂", "၃", "၄", "၅", "၆", "၇", "၈", "၉"]
        
        # Traditional time periods (8 periods of the day)
        self.time_periods = {
            'en': [
                "Sunrise", "Morning", "Noon", "Afternoon", 
                "Sunset", "Night", "Midnight", "Dawn"
            ],
            'mm': [
                "နေထွက်", "နေတက်", "မွန်းတည့်", "နေလွဲ",
                "နေဝင်", "ညည့်", "သန်းခေါင်", "သန်းလွဲ"
            ]
        }
        
        # Directions
        self.directions = {
            'en': ["East", "West", "North", "South"],
            'mm': ["အရှေ့", "အနောက်", "မြောက်", "တောင်"]
        }
        
        # Animal years (12-year cycle)
        self.animal_years = {
            'en': [
                "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake",
                "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"
            ],
            'mm': [
                "ကြွက်", "နွား", "ကျား", "ယုန်", "နဂါး", "မြွေ",
                "မြင်း", "ဆိတ်", "မျောက်", "ကြက်", "ခွေး", "ဝက်"
            ]
        }
        
        # Lunar phases
        self.lunar_phases = {
            'en': ["New Moon", "Waxing Crescent", "First Quarter", "Waxing Gibbous",
                   "Full Moon", "Waning Gibbous", "Last Quarter", "Waning Crescent"],
            'mm': ["လဆန်း", "လဆန်းပိုင်း", "လပြည့်ဝက်", "လပြည့်နီး",
                   "လပြည့်", "လဆုတ်နီး", "လဆုတ်ဝက်", "လဆုတ်ပိုင်း"]
        }
        
        # House names (12 houses in Vedic astrology)
        self.house_names = {
            'en': [
                "First House (Ascendant)", "Second House", "Third House",
                "Fourth House", "Fifth House", "Sixth House",
                "Seventh House", "Eighth House", "Ninth House",
                "Tenth House", "Eleventh House", "Twelfth House"
            ],
            'mm': [
                "ပထမအိမ် (လဂ်နာ)", "ဒုတိယအိမ်", "တတိယအိမ်",
                "စတုတ္ထအိမ်", "ပဉ္စမအိမ်", "ဆဋ္ဌမအိမ်",
                "သတ္တမအိမ်", "အဋ္ဌမအိမ်", "နဝမအိမ်",
                "ဒသမအိမ်", "ဧကာဒသမအိမ်", "ဒွါဒသမအိမ်"
            ]
        }
        
        # Planetary lordships for nakshatras
        self.nakshatra_lords = [
            "Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu", "Jupiter", "Saturn", "Mercury",
            "Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu", "Jupiter", "Saturn", "Mercury",
            "Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu", "Jupiter", "Saturn", "Mercury"
        ]
        
        # Dasha sequence and years
        self.dasha_sequence = ["Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu", "Jupiter", "Saturn", "Mercury"]
        self.dasha_years = {
            "Ketu": 7, "Venus": 20, "Sun": 6, "Moon": 10, "Mars": 7,
            "Rahu": 18, "Jupiter": 16, "Saturn": 19, "Mercury": 17
        }
        
        # Exaltation and debilitation signs for planets
        self.exaltation_signs = {
            "Sun": 0,      # Aries
            "Moon": 1,     # Taurus  
            "Mars": 9,     # Capricorn
            "Mercury": 5,  # Virgo
            "Jupiter": 3,  # Cancer
            "Venus": 11,   # Pisces
            "Saturn": 6    # Libra
        }
        
        self.debilitation_signs = {
            "Sun": 6,      # Libra
            "Moon": 7,     # Scorpio
            "Mars": 3,     # Cancer
            "Mercury": 11, # Pisces
            "Jupiter": 9,  # Capricorn
            "Venus": 5,    # Virgo
            "Saturn": 0    # Aries
        }
        
        # Own signs for planets
        self.own_signs = {
            "Sun": [4],           # Leo
            "Moon": [3],          # Cancer
            "Mars": [0, 7],       # Aries, Scorpio
            "Mercury": [2, 5],    # Gemini, Virgo
            "Jupiter": [8, 11],   # Sagittarius, Pisces
            "Venus": [1, 6],      # Taurus, Libra
            "Saturn": [9, 10]     # Capricorn, Aquarius
        }
        
        # Friendly, neutral, and enemy relationships between planets
        self.planetary_relationships = {
            "Sun": {"friends": ["Moon", "Mars", "Jupiter"], "enemies": ["Venus", "Saturn"], "neutral": ["Mercury"]},
            "Moon": {"friends": ["Sun", "Mercury"], "enemies": [], "neutral": ["Mars", "Jupiter", "Venus", "Saturn"]},
            "Mars": {"friends": ["Sun", "Moon", "Jupiter"], "enemies": ["Mercury"], "neutral": ["Venus", "Saturn"]},
            "Mercury": {"friends": ["Sun", "Venus"], "enemies": ["Moon"], "neutral": ["Mars", "Jupiter", "Saturn"]},
            "Jupiter": {"friends": ["Sun", "Moon", "Mars"], "enemies": ["Mercury", "Venus"], "neutral": ["Saturn"]},
            "Venus": {"friends": ["Mercury", "Saturn"], "enemies": ["Sun", "Moon"], "neutral": ["Mars", "Jupiter"]},
            "Saturn": {"friends": ["Mercury", "Venus"], "enemies": ["Sun", "Moon", "Mars"], "neutral": ["Jupiter"]}
        }
    
    def get_rashi_name(self, index: int, language: str = 'en') -> str:
        """Get rashi name by index (0-11)"""
        if 0 <= index < 12:
            return self.rashi_names[language][index]
        return ""
    
    def get_planet_name(self, planet: str, language: str = 'mm') -> str:
        """Get planet name in specified language"""
        try:
            en_index = self.planets['en'].index(planet)
            return self.planets[language][en_index]
        except (ValueError, KeyError):
            return planet
    
    def get_nakshatra_name(self, index: int, language: str = 'en') -> str:
        """Get nakshatra name by index (0-26)"""
        if 0 <= index < 27:
            return self.nakshatras[language][index]
        return ""
    
    def get_nakshatra_lord(self, nakshatra_index: int) -> str:
        """Get the ruling planet for a nakshatra"""
        if 0 <= nakshatra_index < 27:
            return self.nakshatra_lords[nakshatra_index]
        return ""
    
    def convert_to_myanmar_numerals(self, number: int) -> str:
        """Convert Arabic numerals to Myanmar numerals"""
        result = ""
        for digit in str(number):
            result += self.myanmar_numerals[int(digit)]
        return result
    
    def get_weekday_name(self, weekday: int, language: str = 'en') -> str:
        """Get weekday name (0=Monday, 6=Sunday)"""
        if 0 <= weekday < 7:
            return self.weekdays[language][weekday]
        return ""
    
    def get_myanmar_month_name(self, month_index: int) -> str:
        """Get Myanmar month name (0-11)"""
        if 0 <= month_index < 12:
            return self.myanmar_months[month_index]
        return ""
    
    def get_animal_year(self, year: int, language: str = 'en') -> str:
        """Get animal year for Myanmar year"""
        animal_index = year % 12
        return self.animal_years[language][animal_index]
    
    def is_planet_exalted(self, planet: str, sign_index: int) -> bool:
        """Check if planet is exalted in given sign"""
        return self.exaltation_signs.get(planet) == sign_index
    
    def is_planet_debilitated(self, planet: str, sign_index: int) -> bool:
        """Check if planet is debilitated in given sign"""
        return self.debilitation_signs.get(planet) == sign_index
    
    def is_planet_in_own_sign(self, planet: str, sign_index: int) -> bool:
        """Check if planet is in its own sign"""
        own_signs = self.own_signs.get(planet, [])
        return sign_index in own_signs
    
    def get_planetary_relationship(self, planet1: str, planet2: str) -> str:
        """Get relationship between two planets"""
        if planet1 not in self.planetary_relationships:
            return "neutral"
        
        relationships = self.planetary_relationships[planet1]
        if planet2 in relationships["friends"]:
            return "friend"
        elif planet2 in relationships["enemies"]:
            return "enemy"
        else:
            return "neutral"
    
    def get_house_significance(self, house_number: int) -> Dict[str, str]:
        """Get the significance and meaning of a house"""
        house_meanings = {
            1: {"significance": "Self, personality, appearance", "mm": "ကိုယ်တိုင်၊ ကိုယ်ရည်ကိုယ်သွေး၊ အသွင်အပြင်"},
            2: {"significance": "Wealth, family, speech", "mm": "စည်းစိမ်၊ မိသားစု၊ စကားပြောဆိုမှု"},
            3: {"significance": "Siblings, courage, communication", "mm": "မောင်နှမများ၊ ရဲစွမ်းသတ္တိ၊ ဆက်သွယ်ရေး"},
            4: {"significance": "Home, mother, property", "mm": "အိမ်၊ မိခင်၊ ပိုင်ဆိုင်မှု"},
            5: {"significance": "Children, education, creativity", "mm": "သားသမီး၊ ပညာရေး၊ ဖန်တီးမှု"},
            6: {"significance": "Health, enemies, service", "mm": "ကျန်းမာရေး၊ ရန်သူများ၊ ဝန်ဆောင်မှု"},
            7: {"significance": "Marriage, partnerships", "mm": "အိမ်ထောင်ရေး၊ လုပ်ဖော်ကိုင်ဖက်"},
            8: {"significance": "Longevity, transformation", "mm": "အသက်ရှည်မှု၊ အပြောင်းအလဲ"},
            9: {"significance": "Fortune, religion, father", "mm": "ကံကြမ္မာ၊ ဘာသာရေး၊ ဖခင်"},
            10: {"significance": "Career, reputation, status", "mm": "အသက်မွေးဝမ်း၊ ဂုဏ်သတင်း၊ အဆင့်အတန်း"},
            11: {"significance": "Gains, friends, aspirations", "mm": "အမြတ်အစွန်း၊ မိတ်ဆွေများ၊ မျှော်လင့်ချက်"},
            12: {"significance": "Loss, spirituality, foreign", "mm": "ဆုံးရှုံးမှု၊ ဝိညာဏရေး၊ နိုင်ငံခြား"}
        }
        
        return house_meanings.get(house_number, {"significance": "Unknown", "mm": "မသိ"})


# Global instance for easy access
myanmar_data = MyanmarAstrologicalData()
