#!/usr/bin/env python3
"""
Myanmar Astro Horo - Main Application Entry Point
မြန်မာ ရိုးရာ ဇာတာဖွဲ့ - အဓိက အပလီကေးရှင်း

Complete Python rewrite of the original VB6 Myanmar Astro Horo application
Based on Surya Siddhanta astronomical theory

Original Developer: Kaung Paing (2002/2003)
VB6 Maintainer: kokoye2007
Python Rewrite: FOSS Myanmar Community

Usage:
    python main.py              # Launch GUI application
    python main.py --cli        # Command line interface
    python main.py --help       # Show help information
"""

import sys
import argparse
from datetime import datetime
from pathlib import Path

# Add the current directory to Python path for imports
sys.path.insert(0, str(Path(__file__).parent))

from gui.main_window import MyanmarAstroHoroGUI
from core.horoscope_generator import HoroscopeGenerator
from data.cities import myanmar_cities


def cli_mode():
    """Command line interface for horoscope generation"""
    print("Myanmar Astro Horo - Command Line Interface")
    print("မြန်မာ ရိုးရာ ဇာတာဖွဲ့ - ကွန်မန်းလိုင်း အင်တာဖေ့စ်")
    print("=" * 50)
    
    try:
        # Get birth information from user
        print("\nEnter birth information:")
        
        # Date input
        while True:
            try:
                date_str = input("Birth date (YYYY-MM-DD): ")
                year, month, day = map(int, date_str.split('-'))
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD")
        
        # Time input
        while True:
            try:
                time_str = input("Birth time (HH:MM, 24-hour format): ")
                hour, minute = map(int, time_str.split(':'))
                if 0 <= hour <= 23 and 0 <= minute <= 59:
                    break
                else:
                    print("Invalid time. Hour should be 0-23, minute 0-59")
            except ValueError:
                print("Invalid time format. Please use HH:MM")
        
        # Location input
        print("\nAvailable cities:")
        cities = myanmar_cities.get_all_cities()
        for i, city in enumerate(cities[:10]):  # Show first 10 cities
            print(f"{i+1}. {city}")
        print("... and more")
        
        city = input("Birth city (or type city name): ").strip()
        if city.isdigit() and 1 <= int(city) <= len(cities):
            city = cities[int(city) - 1]
        
        # Create birth datetime
        birth_datetime = datetime(year, month, day, hour, minute)
        
        print(f"\nGenerating horoscope for:")
        print(f"Date: {birth_datetime.strftime('%Y-%m-%d %H:%M')}")
        print(f"Place: {city}")
        print("Please wait...")
        
        # Generate horoscope
        horoscope_gen = HoroscopeGenerator()
        horoscope = horoscope_gen.generate_complete_horoscope(birth_datetime, city)
        
        # Display results
        print("\n" + "=" * 60)
        print("MYANMAR ASTRO HORO - HOROSCOPE RESULTS")
        print("=" * 60)
        
        # Basic information
        birth_info = horoscope['birth_info']
        myanmar_cal = horoscope['myanmar_calendar']
        
        print(f"\nBirth Information:")
        print(f"Date & Time: {birth_info['datetime'].strftime('%Y-%m-%d %H:%M')}")
        print(f"Place: {birth_info['place']}")
        print(f"Coordinates: {birth_info['latitude']:.4f}°N, {birth_info['longitude']:.4f}°E")
        print(f"Myanmar Date: {myanmar_cal['year']} {myanmar_cal['month_name']} {myanmar_cal['day']} {myanmar_cal['lunar_phase']}")
        
        # Ascendant
        ascendant = horoscope['ascendant']
        print(f"\nAscendant (Lagna): {ascendant['sign_en']} ({ascendant['sign_mm']}) {ascendant['degree_in_sign']:.2f}°")
        
        # Planetary positions
        print(f"\nPlanetary Positions:")
        for planet, data in horoscope['planets'].items():
            planet_mm = horoscope_gen.planets.get(planet, planet)
            retrograde = " (R)" if data['retrograde'] else ""
            print(f"{planet} ({planet_mm}){retrograde}: {data['sign_en']} ({data['sign_mm']}) {data['degree_in_sign']:.2f}°")
        
        # Birth nakshatra
        nakshatra = horoscope['birth_nakshatra']
        print(f"\nBirth Nakshatra: {nakshatra['name_en']} ({nakshatra['name_mm']})")
        print(f"Lord: {nakshatra['lord']} ({nakshatra['lord_mm']})")
        print(f"Pada: {nakshatra['pada']}")
        
        # Current dasha
        if 'dasha_periods' in horoscope:
            current_dasha = horoscope['dasha_periods']['current_dasha']
            print(f"\nCurrent Dasha: {current_dasha['dasha']} ({current_dasha['dasha_mm']})")
            print(f"Period: {current_dasha['start_date'].strftime('%Y-%m-%d')} to {current_dasha['end_date'].strftime('%Y-%m-%d')}")
        
        # Yogas
        if 'yogas' in horoscope and horoscope['yogas']:
            print(f"\nSpecial Yogas:")
            for yoga in horoscope['yogas']:
                print(f"• {yoga['name_en']} ({yoga['name_mm']}): {yoga['description']}")
        
        print("\n" + "=" * 60)
        print("Horoscope generation completed successfully!")
        
        # Ask if user wants to save
        save = input("\nSave horoscope to file? (y/n): ").lower().strip()
        if save == 'y':
            filename = f"horoscope_{birth_datetime.strftime('%Y%m%d_%H%M')}_{city.replace(' ', '_')}.txt"
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("MYANMAR ASTRO HORO - COMPLETE HOROSCOPE\n")
                f.write("မြန်မာ ရိုးရာ ဇာတာဖွဲ့ - ပြည့်စုံသော ဇာတာ\n")
                f.write("=" * 60 + "\n\n")
                
                f.write(f"Birth Information:\n")
                f.write(f"Date & Time: {birth_info['datetime'].strftime('%Y-%m-%d %H:%M')}\n")
                f.write(f"Place: {birth_info['place']}\n")
                f.write(f"Myanmar Date: {myanmar_cal['year']} {myanmar_cal['month_name']} {myanmar_cal['day']} {myanmar_cal['lunar_phase']}\n\n")
                
                f.write(f"Ascendant: {ascendant['sign_en']} ({ascendant['sign_mm']}) {ascendant['degree_in_sign']:.2f}°\n\n")
                
                f.write("Planetary Positions:\n")
                for planet, data in horoscope['planets'].items():
                    planet_mm = horoscope_gen.planets.get(planet, planet)
                    retrograde = " (R)" if data['retrograde'] else ""
                    f.write(f"{planet} ({planet_mm}){retrograde}: {data['sign_en']} ({data['sign_mm']}) {data['degree_in_sign']:.2f}°\n")
                
                f.write(f"\nBirth Nakshatra: {nakshatra['name_en']} ({nakshatra['name_mm']})\n")
                
                if 'yogas' in horoscope and horoscope['yogas']:
                    f.write(f"\nSpecial Yogas:\n")
                    for yoga in horoscope['yogas']:
                        f.write(f"• {yoga['name_en']} ({yoga['name_mm']}): {yoga['description']}\n")
            
            print(f"Horoscope saved to: {filename}")
        
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
    except Exception as e:
        print(f"\nError: {str(e)}")
        print("Please check your input and try again.")


def show_help():
    """Show help information"""
    help_text = """
Myanmar Astro Horo - Python Version
မြန်မာ ရိုးရာ ဇာတာဖွဲ့ - Python ဗားရှင်း

DESCRIPTION:
    Complete Python rewrite of the Myanmar Astronomy Horoscope App
    Based on Surya Siddhanta theory and traditional Myanmar astrology
    
    Original VB6 application by Kaung Paing (2002/2003)
    Maintained by kokoye2007, rewritten in Python by FOSS Myanmar Community

USAGE:
    python main.py              Launch GUI application
    python main.py --cli        Command line interface
    python main.py --help       Show this help message

FEATURES:
    • Complete horoscope generation based on Surya Siddhanta
    • Myanmar calendar system with lunar calculations
    • Nakshatra (နက္ခတ်) calculations and analysis
    • Planetary positions and house calculations
    • Dasha periods (ဒသာကာလ) calculation
    • Special yoga combinations detection
    • Traditional Myanmar astrological predictions
    • Support for major Myanmar cities
    • Export to text and JSON formats

SUPPORTED CITIES:
    Yangon, Mandalay, Naypyidaw, Bagan, Mawlamyine, Sittwe,
    Myitkyina, Taunggyi, Hakha, Loikaw, Hpa-an, Dawei,
    Pathein, Magway, Sagaing, and many more...

LICENSE:
    MIT License with restriction:
    "It is strictly prohibited to publish and sell Chanditha 
    calendars generated by this software."

VERSION: 2.0 (Python)
    """
    print(help_text)


def main():
    """Main application entry point"""
    parser = argparse.ArgumentParser(
        description="Myanmar Astro Horo - Traditional Myanmar Horoscope Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('--cli', action='store_true',
                       help='Run in command line interface mode')
    parser.add_argument('--version', action='version', version='Myanmar Astro Horo 2.0 (Python)')
    
    args = parser.parse_args()
    
    if args.cli:
        cli_mode()
    elif len(sys.argv) == 1:
        # No arguments, launch GUI
        try:
            app = MyanmarAstroHoroGUI()
            app.run()
        except ImportError as e:
            print("Error: GUI dependencies not available.")
            print("Please install tkinter or run with --cli for command line interface.")
            print(f"Error details: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Error launching GUI: {e}")
            print("Try running with --cli for command line interface.")
            sys.exit(1)
    else:
        show_help()


if __name__ == "__main__":
    main()
