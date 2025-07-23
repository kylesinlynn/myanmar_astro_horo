"""
Nakshatra (Lunar Mansion) System Implementation
Based on traditional Myanmar/Indian astronomical calculations

This module handles the 27 Nakshatra system used in Myanmar astrology,
including calculations for lunar mansions, their properties, and influences.
"""

import math
from datetime import datetime
from typing import Tuple, Dict, List
from .astronomical_calculations import AstronomicalCalculations


class NakshatraSystem:
    """Nakshatra (နက္ခတ်) calculation and analysis system"""
    
    def __init__(self):
        self.astro_calc = AstronomicalCalculations()
        
        # 27 Nakshatras with their properties
        self.nakshatras = [
            {
                'name_en': 'Ashwini',
                'name_mm': 'အဿဝဏီ',
                'lord': 'Ketu',
                'lord_mm': 'ကေတု',
                'nature': 'Swift',
                'nature_mm': 'မြန်ဆန်',
                'symbol': 'Horse Head',
                'symbol_mm': 'မြင်းခေါင်း',
                'deity': 'Ashwini Kumaras',
                'deity_mm': 'အဿဝဏီကုမာရ',
                'gana': 'Deva',
                'element': 'Earth'
            },
            {
                'name_en': 'Bharani',
                'name_mm': 'ဘရဏီ',
                'lord': 'Venus',
                'lord_mm': 'သုကြ',
                'nature': 'Fierce',
                'nature_mm': 'ကြမ်းတမ်း',
                'symbol': 'Yoni',
                'symbol_mm': 'ယောနိ',
                'deity': 'Yama',
                'deity_mm': 'ယမ',
                'gana': 'Manushya',
                'element': 'Earth'
            },
            {
                'name_en': 'Krittika',
                'name_mm': 'ကြတ္တိကာ',
                'lord': 'Sun',
                'lord_mm': 'နေ',
                'nature': 'Sharp',
                'nature_mm': 'ထက်မြက်',
                'symbol': 'Knife',
                'symbol_mm': 'ဓား',
                'deity': 'Agni',
                'deity_mm': 'အဂ္ဂိ',
                'gana': 'Rakshasa',
                'element': 'Fire'
            },
            {
                'name_en': 'Rohini',
                'name_mm': 'ရောဟဏီ',
                'lord': 'Moon',
                'lord_mm': 'လ',
                'nature': 'Fixed',
                'nature_mm': 'တည်ငြိမ်',
                'symbol': 'Cart',
                'symbol_mm': 'လှည်း',
                'deity': 'Brahma',
                'deity_mm': 'ဗြဟ္မာ',
                'gana': 'Manushya',
                'element': 'Earth'
            },
            {
                'name_en': 'Mrigashira',
                'name_mm': 'မိဂသီ',
                'lord': 'Mars',
                'lord_mm': 'အင်္ဂါ',
                'nature': 'Soft',
                'nature_mm': 'နူးညံ့',
                'symbol': 'Deer Head',
                'symbol_mm': 'သမင်ခေါင်း',
                'deity': 'Soma',
                'deity_mm': 'သောမ',
                'gana': 'Deva',
                'element': 'Earth'
            },
            {
                'name_en': 'Ardra',
                'name_mm': 'အဒြ',
                'lord': 'Rahu',
                'lord_mm': 'ရာဟု',
                'nature': 'Sharp',
                'nature_mm': 'ထက်မြက်',
                'symbol': 'Teardrop',
                'symbol_mm': 'မျက်ရည်',
                'deity': 'Rudra',
                'deity_mm': 'ရုဒြ',
                'gana': 'Manushya',
                'element': 'Water'
            }
            # ... continuing with all 27 nakshatras
        ]
        
        # Complete the nakshatra list (abbreviated for space)
        self._complete_nakshatra_data()
        
    def _complete_nakshatra_data(self):
        """Complete the nakshatra data with remaining 21 nakshatras"""
        remaining_nakshatras = [
            ('Punarvasu', 'ပုဏ္ဏဖုသျှု', 'Jupiter', 'ကြာသပတေး'),
            ('Pushya', 'ဖုသျှ', 'Saturn', 'စနေ'),
            ('Ashlesha', 'အသလိဿ', 'Mercury', 'ဗုဒ္ဓဟူး'),
            ('Magha', 'မာဃ', 'Ketu', 'ကေတု'),
            ('Purva Phalguni', 'ပြုဗ္ဗာဘရဂုဏ္ဏီ', 'Venus', 'သုကြ'),
            ('Uttara Phalguni', 'ဥတ္တရာဘရဂုဏ္ဏီ', 'Sun', 'နေ'),
            ('Hasta', 'ဟဿဒ', 'Moon', 'လ'),
            ('Chitra', 'စိတြ', 'Mars', 'အင်္ဂါ'),
            ('Swati', 'သွာတိ', 'Rahu', 'ရာဟု'),
            ('Vishakha', 'ဝိသာခါ', 'Jupiter', 'ကြာသပတေး'),
            ('Anuradha', 'အနုရာဓ', 'Saturn', 'စနေ'),
            ('Jyeshtha', 'ဇေဋ္ဌ', 'Mercury', 'ဗုဒ္ဓဟူး'),
            ('Mula', 'မူလ', 'Ketu', 'ကေတု'),
            ('Purva Ashadha', 'ပြုဗ္ဗာသဠ်', 'Venus', 'သုကြ'),
            ('Uttara Ashadha', 'ဥတ္တရာသဠ်', 'Sun', 'နေ'),
            ('Shravana', 'သရဝဏ်', 'Moon', 'လ'),
            ('Dhanishta', 'ဓနသိဒ္ဓ', 'Mars', 'အင်္ဂါ'),
            ('Shatabhisha', 'သတ္တဘိသျှ', 'Rahu', 'ရာဟု'),
            ('Purva Bhadrapada', 'ပြုဗ္ဗာပုရပိုက်', 'Jupiter', 'ကြာသပတေး'),
            ('Uttara Bhadrapada', 'ဥတ္တရာပုရပိုက်', 'Saturn', 'စနေ'),
            ('Revati', 'ရေဝတီ', 'Mercury', 'ဗုဒ္ဓဟူး')
        ]
        
        # Add remaining nakshatras with basic properties
        for i, (name_en, name_mm, lord_en, lord_mm) in enumerate(remaining_nakshatras, 6):
            self.nakshatras.append({
                'name_en': name_en,
                'name_mm': name_mm,
                'lord': lord_en,
                'lord_mm': lord_mm,
                'nature': 'Mixed',
                'nature_mm': 'ရောနှော',
                'gana': 'Deva' if i % 3 == 0 else 'Manushya' if i % 3 == 1 else 'Rakshasa',
                'element': 'Earth'
            })
    
    def calculate_nakshatra(self, jd: float) -> Dict[str, any]:
        """
        Calculate current Nakshatra for given Julian Day
        Returns comprehensive nakshatra information
        """
        # Get Moon's sidereal longitude
        moon_longitude = self.astro_calc.mean_longitude_moon(jd)
        sidereal_longitude = self.astro_calc.tropical_to_sidereal(moon_longitude, jd)
        
        # Each nakshatra spans 13°20' (13.333...)
        nakshatra_span = 360.0 / 27.0
        nakshatra_index = int(sidereal_longitude / nakshatra_span)
        
        # Calculate position within nakshatra (0-100%)
        position_in_nakshatra = (sidereal_longitude % nakshatra_span) / nakshatra_span * 100
        
        # Get nakshatra data
        nakshatra_data = self.nakshatras[nakshatra_index].copy()
        nakshatra_data['index'] = nakshatra_index + 1
        nakshatra_data['position_percent'] = position_in_nakshatra
        nakshatra_data['longitude'] = sidereal_longitude
        
        # Calculate pada (quarter) - each nakshatra has 4 padas
        pada = int(position_in_nakshatra / 25) + 1
        nakshatra_data['pada'] = pada
        
        return nakshatra_data
    
    def calculate_birth_nakshatra(self, birth_datetime: datetime) -> Dict[str, any]:
        """Calculate birth nakshatra with detailed analysis"""
        jd = self.astro_calc.julian_day_number(birth_datetime)
        nakshatra_info = self.calculate_nakshatra(jd)
        
        # Add birth-specific calculations
        nakshatra_info['birth_datetime'] = birth_datetime
        nakshatra_info['dasha_years'] = self.get_nakshatra_dasha_years(nakshatra_info['index'])
        nakshatra_info['characteristics'] = self.get_nakshatra_characteristics(nakshatra_info['index'])
        
        return nakshatra_info
    
    def get_nakshatra_dasha_years(self, nakshatra_index: int) -> int:
        """
        Get Vimshottari Dasha years for nakshatra lord
        Based on traditional Vedic astrology system
        """
        dasha_years = {
            'Sun': 6, 'Moon': 10, 'Mars': 7, 'Rahu': 18,
            'Jupiter': 16, 'Saturn': 19, 'Mercury': 17,
            'Ketu': 7, 'Venus': 20
        }
        
        nakshatra = self.nakshatras[nakshatra_index - 1]
        return dasha_years.get(nakshatra['lord'], 0)
    
    def get_nakshatra_characteristics(self, nakshatra_index: int) -> Dict[str, str]:
        """Get personality characteristics based on birth nakshatra"""
        characteristics = {
            1: {  # Ashwini
                'positive': 'Quick, energetic, healing abilities',
                'positive_mm': 'မြန်ဆန်၊ စွမ်းအင်ပြည့်၊ ကုသနိုင်စွမ်း',
                'negative': 'Impatient, restless',
                'negative_mm': 'မစိုးရိမ်၊ မငြိမ်မသက်'
            },
            2: {  # Bharani
                'positive': 'Creative, nurturing, responsible',
                'positive_mm': 'ဖန်တီးမှု၊ ပြုစုစောင့်ရှောက်မှု၊ တာဝန်ယူမှု',
                'negative': 'Stubborn, jealous',
                'negative_mm': 'ခေါင်းမာ၊ မနာလိုမှု'
            }
            # Add more characteristics for other nakshatras
        }
        
        return characteristics.get(nakshatra_index, {
            'positive': 'Balanced nature',
            'positive_mm': 'ဟန်ချက်ညီသော သဘာဝ',
            'negative': 'Variable traits',
            'negative_mm': 'ပြောင်းလဲနိုင်သော လက္ခဏာများ'
        })
    
    def calculate_nakshatra_compatibility(self, nakshatra1: int, nakshatra2: int) -> Dict[str, any]:
        """
        Calculate compatibility between two nakshatras
        Used for marriage compatibility analysis
        """
        # Simplified compatibility calculation
        # In practice, this involves complex rules from classical texts
        
        compatibility_score = 0
        factors = {}
        
        # Varna (caste) compatibility
        varna_score = self._calculate_varna_compatibility(nakshatra1, nakshatra2)
        compatibility_score += varna_score
        factors['varna'] = varna_score
        
        # Vasya (dominance) compatibility
        vasya_score = self._calculate_vasya_compatibility(nakshatra1, nakshatra2)
        compatibility_score += vasya_score
        factors['vasya'] = vasya_score
        
        # Tara (birth star) compatibility
        tara_score = self._calculate_tara_compatibility(nakshatra1, nakshatra2)
        compatibility_score += tara_score
        factors['tara'] = tara_score
        
        # Yoni (nature) compatibility
        yoni_score = self._calculate_yoni_compatibility(nakshatra1, nakshatra2)
        compatibility_score += yoni_score
        factors['yoni'] = yoni_score
        
        # Graha Maitri (planetary friendship)
        graha_score = self._calculate_graha_maitri(nakshatra1, nakshatra2)
        compatibility_score += graha_score
        factors['graha_maitri'] = graha_score
        
        # Gana (temperament) compatibility
        gana_score = self._calculate_gana_compatibility(nakshatra1, nakshatra2)
        compatibility_score += gana_score
        factors['gana'] = gana_score
        
        # Bhakoot (sign) compatibility
        bhakoot_score = self._calculate_bhakoot_compatibility(nakshatra1, nakshatra2)
        compatibility_score += bhakoot_score
        factors['bhakoot'] = bhakoot_score
        
        # Nadi (pulse) compatibility
        nadi_score = self._calculate_nadi_compatibility(nakshatra1, nakshatra2)
        compatibility_score += nadi_score
        factors['nadi'] = nadi_score
        
        total_score = compatibility_score
        percentage = (total_score / 36) * 100  # Maximum possible score is 36
        
        return {
            'total_score': total_score,
            'percentage': percentage,
            'factors': factors,
            'compatibility_level': self._get_compatibility_level(percentage)
        }
    
    def _calculate_varna_compatibility(self, n1: int, n2: int) -> int:
        """Calculate Varna compatibility (4 points max)"""
        # Simplified varna calculation
        varna1 = (n1 - 1) % 4
        varna2 = (n2 - 1) % 4
        
        if varna1 == varna2:
            return 4
        elif abs(varna1 - varna2) == 1:
            return 2
        else:
            return 1
    
    def _calculate_vasya_compatibility(self, n1: int, n2: int) -> int:
        """Calculate Vasya compatibility (2 points max)"""
        # Simplified calculation
        return 2 if (n1 + n2) % 2 == 0 else 1
    
    def _calculate_tara_compatibility(self, n1: int, n2: int) -> int:
        """Calculate Tara compatibility (3 points max)"""
        diff = abs(n1 - n2)
        if diff in [0, 9, 18]:
            return 3
        elif diff in [2, 4, 6, 8, 11, 13, 15, 17, 20, 22, 24, 26]:
            return 1.5
        else:
            return 3
    
    def _calculate_yoni_compatibility(self, n1: int, n2: int) -> int:
        """Calculate Yoni compatibility (4 points max)"""
        # Simplified yoni compatibility
        yoni1 = (n1 - 1) % 14
        yoni2 = (n2 - 1) % 14
        
        if yoni1 == yoni2:
            return 4
        else:
            return 2
    
    def _calculate_graha_maitri(self, n1: int, n2: int) -> int:
        """Calculate Graha Maitri (5 points max)"""
        lord1 = self.nakshatras[n1 - 1]['lord']
        lord2 = self.nakshatras[n2 - 1]['lord']
        
        # Simplified planetary friendship
        if lord1 == lord2:
            return 5
        else:
            return 3  # Neutral
    
    def _calculate_gana_compatibility(self, n1: int, n2: int) -> int:
        """Calculate Gana compatibility (6 points max)"""
        gana1 = self.nakshatras[n1 - 1]['gana']
        gana2 = self.nakshatras[n2 - 1]['gana']
        
        if gana1 == gana2:
            return 6
        elif (gana1 == 'Deva' and gana2 == 'Manushya') or (gana1 == 'Manushya' and gana2 == 'Deva'):
            return 5
        else:
            return 1
    
    def _calculate_bhakoot_compatibility(self, n1: int, n2: int) -> int:
        """Calculate Bhakoot compatibility (7 points max)"""
        # Based on rashi positions
        rashi1 = ((n1 - 1) * 13.333) // 30
        rashi2 = ((n2 - 1) * 13.333) // 30
        
        diff = abs(rashi1 - rashi2)
        if diff in [0, 6]:
            return 0  # Not compatible
        else:
            return 7
    
    def _calculate_nadi_compatibility(self, n1: int, n2: int) -> int:
        """Calculate Nadi compatibility (8 points max)"""
        nadi1 = (n1 - 1) % 3
        nadi2 = (n2 - 1) % 3
        
        if nadi1 != nadi2:
            return 8
        else:
            return 0  # Same nadi is not compatible
    
    def _get_compatibility_level(self, percentage: float) -> str:
        """Get compatibility level description"""
        if percentage >= 80:
            return "Excellent"
        elif percentage >= 60:
            return "Good"
        elif percentage >= 40:
            return "Average"
        else:
            return "Poor"
    
    def get_favorable_periods(self, birth_nakshatra: int, current_date: datetime) -> Dict[str, List[datetime]]:
        """
        Calculate favorable periods based on nakshatra transits
        """
        jd = self.astro_calc.julian_day_number(current_date)
        
        favorable_dates = []
        unfavorable_dates = []
        
        # Check next 30 days
        for i in range(30):
            check_date = current_date + timedelta(days=i)
            check_jd = self.astro_calc.julian_day_number(check_date)
            current_nakshatra = self.calculate_nakshatra(check_jd)['index']
            
            # Favorable nakshatras (trine positions)
            if (current_nakshatra - birth_nakshatra) % 27 in [0, 9, 18]:
                favorable_dates.append(check_date)
            # Unfavorable nakshatras
            elif (current_nakshatra - birth_nakshatra) % 27 in [3, 5, 7]:
                unfavorable_dates.append(check_date)
        
        return {
            'favorable': favorable_dates,
            'unfavorable': unfavorable_dates
        }
