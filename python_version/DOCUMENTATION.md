# Myanmar Astro Horo - Python Version Documentation
# မြန်မာ ရိုးရာ ဇာတာဖွဲ့ - Python ဗားရှင်း စာရွက်စာတမ်းများ

## Overview

This is a complete Python rewrite of the Myanmar Astronomy Horoscope App, originally developed in Visual Basic 6 by Kaung Paing in 2002/2003. The application is based on the ancient astronomical theory of **Surya Siddhanta** (သူရိယသိဒ္ဓန္တ) and provides comprehensive horoscope generation with traditional Myanmar astrological calculations.

## Project Structure

```
python_version/
├── main.py                 # Main application entry point
├── requirements.txt        # Python dependencies
├── README.md              # Project overview
├── DOCUMENTATION.md       # This file
├── core/                  # Core calculation modules
│   ├── __init__.py
│   ├── astronomical_calculations.py    # Basic astronomical functions
│   ├── calendar_system.py             # Myanmar calendar system
│   ├── nakshatra_system.py           # Nakshatra calculations
│   └── horoscope_generator.py        # Complete horoscope generation
├── data/                  # Data files and mappings
│   ├── __init__.py
│   ├── cities.py          # Myanmar cities database
│   └── myanmar_data.py    # Myanmar astrological data
├── gui/                   # User interface modules
│   ├── __init__.py
│   └── main_window.py     # Main GUI application
└── tests/                 # Unit tests
    ├── __init__.py
    ├── run_tests.py       # Test runner
    ├── test_astronomical_calculations.py
    ├── test_myanmar_calendar.py
    └── test_horoscope_generator.py
```

## Core Modules

### 1. Astronomical Calculations (`core/astronomical_calculations.py`)

**Purpose**: Implements fundamental astronomical calculations based on Surya Siddhanta theory.

**Key Classes**:
- `AstronomicalCalculations`: Main class for astronomical computations

**Key Methods**:
- `julian_day_number(date)`: Convert Gregorian date to Julian Day Number
- `mean_longitude_sun(jd)`: Calculate mean longitude of the Sun
- `true_longitude_sun(jd)`: Calculate true longitude of the Sun
- `mean_longitude_moon(jd)`: Calculate mean longitude of the Moon
- `planetary_positions(jd)`: Calculate positions of all planets
- `sunrise_sunset(jd, lat, lon)`: Calculate sunrise and sunset times
- `get_rashi(longitude)`: Get zodiac sign from longitude
- `normalize_angle(angle)`: Normalize angle to 0-360 degrees

**Usage Example**:
```python
from core.astronomical_calculations import AstronomicalCalculations

astro = AstronomicalCalculations()
jd = astro.julian_day_number(datetime(2023, 6, 21, 12, 0))
sun_longitude = astro.true_longitude_sun(jd)
sign_en, sign_mm = astro.get_rashi(sun_longitude)
```

### 2. Myanmar Calendar System (`core/calendar_system.py`)

**Purpose**: Handles Myanmar traditional calendar conversions and lunar calculations.

**Key Classes**:
- `MyanmarCalendarSystem`: Myanmar calendar conversion and calculations

**Key Methods**:
- `gregorian_to_myanmar(date)`: Convert Gregorian to Myanmar calendar
- `calculate_lunar_info(jd)`: Calculate lunar month and day information
- `get_auspicious_times(date, lat, lon)`: Calculate traditional time periods
- `calculate_lunar_mansion(jd)`: Calculate Nakshatra for given date
- `get_year_animal(myanmar_year)`: Get animal year for Myanmar calendar

**Usage Example**:
```python
from core.calendar_system import MyanmarCalendarSystem

calendar = MyanmarCalendarSystem()
myanmar_date = calendar.gregorian_to_myanmar(datetime(2023, 4, 17))
print(f"Myanmar Date: {myanmar_date['year']} {myanmar_date['month_name']} {myanmar_date['day']}")
```

### 3. Nakshatra System (`core/nakshatra_system.py`)

**Purpose**: Implements the 27 Nakshatra (lunar mansion) system used in Myanmar astrology.

**Key Classes**:
- `NakshatraSystem`: Nakshatra calculations and analysis

**Key Methods**:
- `calculate_nakshatra(jd)`: Calculate current Nakshatra
- `calculate_birth_nakshatra(birth_datetime)`: Calculate birth Nakshatra with analysis
- `calculate_nakshatra_compatibility(n1, n2)`: Marriage compatibility analysis
- `get_favorable_periods(birth_nakshatra, current_date)`: Find favorable periods

**Usage Example**:
```python
from core.nakshatra_system import NakshatraSystem

nakshatra_sys = NakshatraSystem()
birth_nakshatra = nakshatra_sys.calculate_birth_nakshatra(datetime(1990, 4, 17, 6, 30))
print(f"Birth Nakshatra: {birth_nakshatra['name_en']} ({birth_nakshatra['name_mm']})")
```

### 4. Horoscope Generator (`core/horoscope_generator.py`)

**Purpose**: Main horoscope generation engine that combines all calculations.

**Key Classes**:
- `HoroscopeGenerator`: Complete horoscope generation system

**Key Methods**:
- `generate_complete_horoscope(birth_datetime, birth_place, lat, lon)`: Generate full horoscope
- `calculate_ascendant(jd, lat, lon)`: Calculate rising sign
- `calculate_all_planetary_positions(jd)`: Calculate all planetary positions
- `calculate_houses(ascendant_longitude, planets)`: Calculate 12 houses
- `calculate_dasha_periods(birth_nakshatra, birth_date)`: Calculate planetary periods

**Usage Example**:
```python
from core.horoscope_generator import HoroscopeGenerator

horoscope_gen = HoroscopeGenerator()
horoscope = horoscope_gen.generate_complete_horoscope(
    datetime(1990, 4, 17, 6, 30), "Yangon"
)
```

## Data Modules

### 1. Cities Database (`data/cities.py`)

**Purpose**: Contains geographical coordinates for major Myanmar cities.

**Key Classes**:
- `MyanmarCities`: Database of Myanmar cities with coordinates

**Features**:
- 50+ major Myanmar cities with coordinates
- Search by English or Myanmar names
- Timezone and elevation information
- Distance calculations between cities

### 2. Myanmar Astrological Data (`data/myanmar_data.py`)

**Purpose**: Contains all Myanmar-specific astrological data and mappings.

**Key Classes**:
- `MyanmarAstrologicalData`: Myanmar astrological data and mappings

**Features**:
- Zodiac signs in English and Myanmar
- 27 Nakshatras with properties
- Myanmar calendar months and days
- Planetary relationships and strengths
- Traditional time periods and directions

## GUI Module

### Main Window (`gui/main_window.py`)

**Purpose**: Provides the main graphical user interface.

**Key Classes**:
- `MyanmarAstroHoroGUI`: Main application window

**Features**:
- Tabbed interface with input, horoscope, calendar, and about sections
- Birth data input with date, time, and location
- Complete horoscope display with Myanmar translations
- Export functionality (text and JSON formats)
- Myanmar calendar information display

## Installation and Usage

### Requirements

- Python 3.7 or higher
- tkinter (usually included with Python)
- Standard Python libraries: math, datetime, json, csv

### Installation

1. Clone or download the project
2. Navigate to the `python_version` directory
3. Install dependencies (if needed):
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

**GUI Mode** (default):
```bash
python main.py
```

**Command Line Mode**:
```bash
python main.py --cli
```

**Help**:
```bash
python main.py --help
```

## Testing

The project includes comprehensive unit tests to verify correctness against astronomical calculations.

### Running Tests

**All tests**:
```bash
cd tests
python run_tests.py
```

**Specific test modules**:
```bash
python run_tests.py astro      # Astronomical calculations
python run_tests.py calendar   # Myanmar calendar system
python run_tests.py horoscope  # Horoscope generation
```

**Individual test files**:
```bash
python -m unittest test_astronomical_calculations.py -v
python -m unittest test_myanmar_calendar.py -v
python -m unittest test_horoscope_generator.py -v
```

## API Reference

### Core Functions

#### Astronomical Calculations

```python
# Basic astronomical functions
jd = julian_day_number(datetime_obj)
sun_longitude = mean_longitude_sun(jd)
moon_longitude = mean_longitude_moon(jd)
planets = planetary_positions(jd)

# Coordinate conversions
degrees, minutes, seconds = degrees_to_dms(decimal_degrees)
decimal_degrees = dms_to_degrees(degrees, minutes, seconds)

# Zodiac calculations
sign_en, sign_mm = get_rashi(longitude)
sidereal_longitude = tropical_to_sidereal(tropical_longitude, jd)
```

#### Myanmar Calendar

```python
# Calendar conversions
myanmar_date = gregorian_to_myanmar(gregorian_date)
lunar_info = calculate_lunar_info(julian_day)
nakshatra_en, nakshatra_mm = calculate_lunar_mansion(julian_day)

# Traditional calculations
auspicious_times = get_auspicious_times(date, latitude, longitude)
animal_en, animal_mm = get_year_animal(myanmar_year)
myanmar_numeral = get_myanmar_numeral(arabic_number)
```

#### Horoscope Generation

```python
# Complete horoscope
horoscope = generate_complete_horoscope(birth_datetime, birth_place, lat, lon)

# Individual components
ascendant = calculate_ascendant(jd, latitude, longitude)
planets = calculate_all_planetary_positions(jd)
houses = calculate_houses(ascendant_longitude, planets)
dasha_periods = calculate_dasha_periods(birth_nakshatra, birth_date)
```

## Data Formats

### Horoscope Output Structure

```python
{
    'birth_info': {
        'datetime': datetime_object,
        'place': 'City Name',
        'latitude': float,
        'longitude': float,
        'julian_day': float
    },
    'myanmar_calendar': {
        'year': int,
        'month': int,
        'month_name': 'Myanmar Month Name',
        'day': int,
        'lunar_phase': 'လဆန်း or လဆုတ်',
        'waxing': boolean,
        'day_of_week': 'Myanmar Day Name'
    },
    'ascendant': {
        'longitude': float,
        'sign_en': 'English Sign',
        'sign_mm': 'Myanmar Sign',
        'degree_in_sign': float
    },
    'planets': {
        'Planet Name': {
            'longitude': float,
            'sign_en': 'English Sign',
            'sign_mm': 'Myanmar Sign',
            'degree_in_sign': float,
            'retrograde': boolean
        }
    },
    'houses': {
        house_number: {
            'start_longitude': float,
            'end_longitude': float,
            'sign_en': 'English Sign',
            'sign_mm': 'Myanmar Sign',
            'planets': ['List of planets in house'],
            'house_name_en': 'English House Name',
            'house_name_mm': 'Myanmar House Name'
        }
    },
    'birth_nakshatra': {
        'name_en': 'English Nakshatra',
        'name_mm': 'Myanmar Nakshatra',
        'lord': 'Ruling Planet',
        'lord_mm': 'Myanmar Planet Name',
        'index': int,
        'pada': int,
        'position_percent': float
    }
}
```

## Customization and Extension

### Adding New Cities

To add new cities to the database:

```python
# In data/cities.py, add to the cities dictionary:
"New City": {
    "name_mm": "မြန်မာ မြို့နာမည်",
    "latitude": float,
    "longitude": float,
    "timezone_offset": 6.5,
    "elevation": int,
    "region": "Region Name"
}
```

### Adding New Calculations

To add new astronomical calculations:

1. Add methods to `AstronomicalCalculations` class
2. Update `HoroscopeGenerator` to use new calculations
3. Add corresponding unit tests
4. Update documentation

### Customizing GUI

The GUI can be customized by modifying `gui/main_window.py`:

- Change colors and fonts
- Add new tabs or sections
- Modify export formats
- Add new input fields

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all files are in correct directories and `__init__.py` files exist
2. **GUI Not Starting**: Check if tkinter is installed (`python -m tkinter`)
3. **Calculation Errors**: Run unit tests to verify calculations
4. **City Not Found**: Check spelling or add city to database

### Debug Mode

To enable debug output, modify the main application:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Contributing

To contribute to the project:

1. Follow the existing code structure and naming conventions
2. Add unit tests for new functionality
3. Update documentation for changes
4. Ensure all tests pass before submitting

## License

MIT License with restriction: "It is strictly prohibited to publish and sell Chanditha calendars generated by this software."

## Credits

- **Original Developer**: Kaung Paing (2002/2003)
- **VB6 Maintainer**: kokoye2007
- **Python Rewrite**: FOSS Myanmar Community
- **Based on**: Surya Siddhanta astronomical theory

## Version History

- **v2.0**: Complete Python rewrite with GUI and CLI interfaces
- **v1.1**: VB6 version with FOSS designation
- **v1.0**: VB6 structure refactor
- **v0.1**: VB6 ownership transfer
- **v0.0**: Original VB6 implementation (2002/2003)
