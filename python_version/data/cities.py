"""
Myanmar Cities Database
Contains geographical coordinates and time zone information for major Myanmar cities
Based on the original VB6 Cities() functions from Kdata4.bas, Kdata5.bas, etc.
"""

from typing import Dict, List, Tuple


class MyanmarCities:
    """Database of Myanmar cities with coordinates and astronomical data"""
    
    def __init__(self):
        # Major Myanmar cities with coordinates (latitude, longitude, timezone_offset)
        self.cities = {
            # Major Cities
            "Yangon": {
                "name_mm": "ရန်ကုန်",
                "latitude": 16.8661,
                "longitude": 96.1951,
                "timezone_offset": 6.5,
                "elevation": 43,
                "region": "Yangon Region"
            },
            "Mandalay": {
                "name_mm": "မန္တလေး",
                "latitude": 21.9588,
                "longitude": 96.0891,
                "timezone_offset": 6.5,
                "elevation": 76,
                "region": "Mandalay Region"
            },
            "Naypyidaw": {
                "name_mm": "နေပြည်တော်",
                "latitude": 19.7633,
                "longitude": 96.0785,
                "timezone_offset": 6.5,
                "elevation": 115,
                "region": "Naypyidaw Union Territory"
            },
            "Bagan": {
                "name_mm": "ပုဂံ",
                "latitude": 21.1717,
                "longitude": 94.8574,
                "timezone_offset": 6.5,
                "elevation": 58,
                "region": "Mandalay Region"
            },
            "Mawlamyine": {
                "name_mm": "မော်လမြိုင်",
                "latitude": 16.4919,
                "longitude": 97.6278,
                "timezone_offset": 6.5,
                "elevation": 16,
                "region": "Mon State"
            },
            
            # Regional Capitals
            "Sittwe": {
                "name_mm": "စစ်တွေ",
                "latitude": 20.1500,
                "longitude": 92.8833,
                "timezone_offset": 6.5,
                "elevation": 9,
                "region": "Rakhine State"
            },
            "Myitkyina": {
                "name_mm": "မြစ်ကြီးနား",
                "latitude": 25.3833,
                "longitude": 97.4000,
                "timezone_offset": 6.5,
                "elevation": 145,
                "region": "Kachin State"
            },
            "Taunggyi": {
                "name_mm": "တောင်ကြီး",
                "latitude": 20.7833,
                "longitude": 97.0333,
                "timezone_offset": 6.5,
                "elevation": 1436,
                "region": "Shan State"
            },
            "Hakha": {
                "name_mm": "ဟားခါး",
                "latitude": 22.6500,
                "longitude": 93.6167,
                "timezone_offset": 6.5,
                "elevation": 1867,
                "region": "Chin State"
            },
            "Loikaw": {
                "name_mm": "လွိုင်ကော်",
                "latitude": 19.6833,
                "longitude": 97.2167,
                "timezone_offset": 6.5,
                "elevation": 1200,
                "region": "Kayah State"
            },
            "Hpa-an": {
                "name_mm": "ဘားအံ",
                "latitude": 16.8833,
                "longitude": 97.6333,
                "timezone_offset": 6.5,
                "elevation": 72,
                "region": "Kayin State"
            },
            "Dawei": {
                "name_mm": "ထားဝယ်",
                "latitude": 14.0833,
                "longitude": 98.2000,
                "timezone_offset": 6.5,
                "elevation": 20,
                "region": "Tanintharyi Region"
            },
            "Pathein": {
                "name_mm": "ပုသိမ်",
                "latitude": 16.7833,
                "longitude": 94.7333,
                "timezone_offset": 6.5,
                "elevation": 12,
                "region": "Ayeyarwady Region"
            },
            "Magway": {
                "name_mm": "မကွေး",
                "latitude": 20.1500,
                "longitude": 94.9333,
                "timezone_offset": 6.5,
                "elevation": 57,
                "region": "Magway Region"
            },
            "Sagaing": {
                "name_mm": "စစ်ကိုင်း",
                "latitude": 21.8833,
                "longitude": 95.9833,
                "timezone_offset": 6.5,
                "elevation": 76,
                "region": "Sagaing Region"
            },
            
            # Important Historical/Religious Cities
            "Mrauk-U": {
                "name_mm": "မြောက်ဦး",
                "latitude": 20.5833,
                "longitude": 93.2000,
                "timezone_offset": 6.5,
                "elevation": 30,
                "region": "Rakhine State"
            },
            "Inle Lake": {
                "name_mm": "အင်းလေးကန်",
                "latitude": 20.5500,
                "longitude": 96.9000,
                "timezone_offset": 6.5,
                "elevation": 884,
                "region": "Shan State"
            },
            "Golden Rock": {
                "name_mm": "ကျိုက်ထီးရိုး",
                "latitude": 17.4833,
                "longitude": 97.1167,
                "timezone_offset": 6.5,
                "elevation": 1100,
                "region": "Mon State"
            },
            
            # Border Towns
            "Myawaddy": {
                "name_mm": "မြဝတီ",
                "latitude": 16.6833,
                "longitude": 98.5167,
                "timezone_offset": 6.5,
                "elevation": 200,
                "region": "Kayin State"
            },
            "Tachileik": {
                "name_mm": "တာချီလိတ်",
                "latitude": 20.4500,
                "longitude": 99.8833,
                "timezone_offset": 6.5,
                "elevation": 390,
                "region": "Shan State"
            },
            "Muse": {
                "name_mm": "မူဆယ်",
                "latitude": 23.9667,
                "longitude": 97.8667,
                "timezone_offset": 6.5,
                "elevation": 1050,
                "region": "Shan State"
            }
        }
        
        # Additional smaller towns and villages (abbreviated list)
        self.towns = {
            "Pyin Oo Lwin": {
                "name_mm": "ပြင်ဦးလွင်",
                "latitude": 22.0333,
                "longitude": 96.4667,
                "timezone_offset": 6.5,
                "elevation": 1070,
                "region": "Mandalay Region"
            },
            "Kalaw": {
                "name_mm": "ကလော",
                "latitude": 20.6333,
                "longitude": 96.5667,
                "timezone_offset": 6.5,
                "elevation": 1320,
                "region": "Shan State"
            },
            "Hsipaw": {
                "name_mm": "သီပေါ",
                "latitude": 22.6167,
                "longitude": 97.3000,
                "timezone_offset": 6.5,
                "elevation": 200,
                "region": "Shan State"
            }
        }
    
    def get_city_info(self, city_name: str) -> Dict[str, any]:
        """Get complete information for a city"""
        city_name_clean = city_name.strip().title()
        
        if city_name_clean in self.cities:
            return self.cities[city_name_clean]
        elif city_name_clean in self.towns:
            return self.towns[city_name_clean]
        else:
            return None
    
    def search_city_by_myanmar_name(self, myanmar_name: str) -> Dict[str, any]:
        """Search city by Myanmar name"""
        for city_name, city_data in {**self.cities, **self.towns}.items():
            if city_data["name_mm"] == myanmar_name:
                result = city_data.copy()
                result["name_en"] = city_name
                return result
        return None
    
    def get_cities_by_region(self, region: str) -> List[Dict[str, any]]:
        """Get all cities in a specific region"""
        result = []
        for city_name, city_data in {**self.cities, **self.towns}.items():
            if city_data["region"] == region:
                city_info = city_data.copy()
                city_info["name_en"] = city_name
                result.append(city_info)
        return result
    
    def get_all_cities(self) -> List[str]:
        """Get list of all available city names"""
        return list(self.cities.keys()) + list(self.towns.keys())
    
    def get_nearest_city(self, latitude: float, longitude: float) -> Tuple[str, Dict[str, any]]:
        """Find the nearest city to given coordinates"""
        min_distance = float('inf')
        nearest_city = None
        nearest_info = None
        
        for city_name, city_data in {**self.cities, **self.towns}.items():
            # Calculate approximate distance using Haversine formula
            distance = self._calculate_distance(
                latitude, longitude,
                city_data["latitude"], city_data["longitude"]
            )
            
            if distance < min_distance:
                min_distance = distance
                nearest_city = city_name
                nearest_info = city_data
        
        return nearest_city, nearest_info
    
    def _calculate_distance(self, lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """Calculate distance between two points using Haversine formula"""
        import math
        
        # Convert to radians
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        
        # Haversine formula
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.asin(math.sqrt(a))
        
        # Earth's radius in kilometers
        r = 6371
        
        return c * r
    
    def get_timezone_offset(self, city_name: str) -> float:
        """Get timezone offset for a city"""
        city_info = self.get_city_info(city_name)
        if city_info:
            return city_info["timezone_offset"]
        return 6.5  # Default Myanmar timezone
    
    def validate_coordinates(self, latitude: float, longitude: float) -> bool:
        """Validate if coordinates are within Myanmar boundaries"""
        # Myanmar approximate boundaries
        min_lat, max_lat = 9.5, 28.5
        min_lon, max_lon = 92.0, 101.0
        
        return (min_lat <= latitude <= max_lat and 
                min_lon <= longitude <= max_lon)


# Global instance for easy access
myanmar_cities = MyanmarCities()
