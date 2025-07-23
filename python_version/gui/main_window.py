"""
Main GUI Window for Myanmar Astro Horo
Based on the original VB6 forms (KDATA.frm, KOUTB.frm, etc.)

This module provides the main user interface for horoscope generation
with traditional Myanmar styling and functionality.
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from datetime import datetime, date
import json
from typing import Dict, Any

from ..core.horoscope_generator import HoroscopeGenerator
from ..data.cities import myanmar_cities


class MyanmarAstroHoroGUI:
    """Main application window"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Myanmar Astro Horo - မြန်မာ ရိုးရာ ဇာတာဖွဲ့")
        self.root.geometry("1000x700")
        self.root.configure(bg='#f0f0f0')
        
        # Initialize horoscope generator
        self.horoscope_gen = HoroscopeGenerator()
        
        # Current horoscope data
        self.current_horoscope = None
        
        self.setup_gui()
        
    def setup_gui(self):
        """Setup the main GUI components"""
        # Create main notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create tabs
        self.create_input_tab()
        self.create_horoscope_tab()
        self.create_calendar_tab()
        self.create_about_tab()
        
    def create_input_tab(self):
        """Create the birth data input tab"""
        input_frame = ttk.Frame(self.notebook)
        self.notebook.add(input_frame, text="Birth Data / မွေးဖွားချိန်")
        
        # Title
        title_label = tk.Label(input_frame, 
                              text="Myanmar Astro Horo\nမြန်မာ ရိုးရာ ဇာတာဖွဲ့",
                              font=('Arial', 16, 'bold'),
                              bg='#f0f0f0')
        title_label.pack(pady=20)
        
        # Main input frame
        main_frame = ttk.Frame(input_frame)
        main_frame.pack(padx=20, pady=20, fill='both', expand=True)
        
        # Birth date and time section
        datetime_frame = ttk.LabelFrame(main_frame, text="Birth Date & Time / မွေးဖွားရက်စွဲနှင့်အချိန်")
        datetime_frame.pack(fill='x', pady=10)
        
        # Date inputs
        date_frame = ttk.Frame(datetime_frame)
        date_frame.pack(pady=10)
        
        ttk.Label(date_frame, text="Date / ရက်စွဲ:").grid(row=0, column=0, padx=5, sticky='e')
        
        self.day_var = tk.StringVar(value=str(datetime.now().day))
        self.month_var = tk.StringVar(value=str(datetime.now().month))
        self.year_var = tk.StringVar(value=str(datetime.now().year))
        
        ttk.Entry(date_frame, textvariable=self.day_var, width=5).grid(row=0, column=1, padx=2)
        ttk.Label(date_frame, text="/").grid(row=0, column=2)
        ttk.Entry(date_frame, textvariable=self.month_var, width=5).grid(row=0, column=3, padx=2)
        ttk.Label(date_frame, text="/").grid(row=0, column=4)
        ttk.Entry(date_frame, textvariable=self.year_var, width=8).grid(row=0, column=5, padx=2)
        
        # Time inputs
        time_frame = ttk.Frame(datetime_frame)
        time_frame.pack(pady=10)
        
        ttk.Label(time_frame, text="Time / အချိန်:").grid(row=0, column=0, padx=5, sticky='e')
        
        self.hour_var = tk.StringVar(value="12")
        self.minute_var = tk.StringVar(value="00")
        
        ttk.Entry(time_frame, textvariable=self.hour_var, width=5).grid(row=0, column=1, padx=2)
        ttk.Label(time_frame, text=":").grid(row=0, column=2)
        ttk.Entry(time_frame, textvariable=self.minute_var, width=5).grid(row=0, column=3, padx=2)
        
        # Location section
        location_frame = ttk.LabelFrame(main_frame, text="Birth Place / မွေးဖွားရာနေရာ")
        location_frame.pack(fill='x', pady=10)
        
        loc_frame = ttk.Frame(location_frame)
        loc_frame.pack(pady=10)
        
        ttk.Label(loc_frame, text="City / မြို့:").grid(row=0, column=0, padx=5, sticky='e')
        
        self.city_var = tk.StringVar(value="Yangon")
        city_combo = ttk.Combobox(loc_frame, textvariable=self.city_var, width=20)
        city_combo['values'] = myanmar_cities.get_all_cities()
        city_combo.grid(row=0, column=1, padx=5)
        
        # Manual coordinates (optional)
        coord_frame = ttk.Frame(location_frame)
        coord_frame.pack(pady=5)
        
        ttk.Label(coord_frame, text="Latitude / လတ္တီကျု:").grid(row=0, column=0, padx=5, sticky='e')
        self.lat_var = tk.StringVar()
        ttk.Entry(coord_frame, textvariable=self.lat_var, width=12).grid(row=0, column=1, padx=2)
        
        ttk.Label(coord_frame, text="Longitude / လောင်ဂျီကျု:").grid(row=0, column=2, padx=5, sticky='e')
        self.lon_var = tk.StringVar()
        ttk.Entry(coord_frame, textvariable=self.lon_var, width=12).grid(row=0, column=3, padx=2)
        
        # Generate button
        generate_btn = tk.Button(main_frame, 
                               text="Generate Horoscope\nဇာတာဖွဲ့ရန်",
                               font=('Arial', 12, 'bold'),
                               bg='#4CAF50',
                               fg='white',
                               command=self.generate_horoscope)
        generate_btn.pack(pady=20)
        
        # Status label
        self.status_label = tk.Label(main_frame, text="Ready / အဆင်သင့်", bg='#f0f0f0')
        self.status_label.pack(pady=10)
        
    def create_horoscope_tab(self):
        """Create the horoscope display tab"""
        horoscope_frame = ttk.Frame(self.notebook)
        self.notebook.add(horoscope_frame, text="Horoscope / ဇာတာ")
        
        # Create scrollable text area for horoscope display
        self.horoscope_text = scrolledtext.ScrolledText(horoscope_frame, 
                                                       wrap=tk.WORD,
                                                       font=('Arial', 10),
                                                       height=35)
        self.horoscope_text.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Export buttons frame
        export_frame = ttk.Frame(horoscope_frame)
        export_frame.pack(fill='x', padx=10, pady=5)
        
        ttk.Button(export_frame, text="Export to Text", 
                  command=self.export_to_text).pack(side='left', padx=5)
        ttk.Button(export_frame, text="Export to JSON", 
                  command=self.export_to_json).pack(side='left', padx=5)
        
    def create_calendar_tab(self):
        """Create the Myanmar calendar tab"""
        calendar_frame = ttk.Frame(self.notebook)
        self.notebook.add(calendar_frame, text="Myanmar Calendar / မြန်မာပြက္ခဒိန်")
        
        # Calendar display area
        self.calendar_text = scrolledtext.ScrolledText(calendar_frame,
                                                      wrap=tk.WORD,
                                                      font=('Arial', 10),
                                                      height=30)
        self.calendar_text.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Show current Myanmar date
        self.show_myanmar_calendar()
        
    def create_about_tab(self):
        """Create the about tab"""
        about_frame = ttk.Frame(self.notebook)
        self.notebook.add(about_frame, text="About / အကြောင်း")
        
        about_text = """
Myanmar Astro Horo - Python Version
မြန်မာ ရိုးရာ ဇာတာဖွဲ့ - Python ဗားရှင်း

Based on Surya Siddhanta Theory
သူရိယသိဒ္ဓန္တ သီအိုရီအပေါ် အခြေခံ၍

Original Developer: Kaung Paing (2002/2003)
VB6 Maintainer: kokoye2007
Python Rewrite: FOSS Myanmar Community

Features:
• Complete horoscope generation
• Myanmar calendar system
• Nakshatra calculations
• Planetary positions
• Dasha periods
• Astrological predictions

License: MIT with restriction
"It is strictly prohibited to publish and sell 
Chanditha calendars generated by this software."

Version: 2.0 (Python)
        """
        
        about_label = tk.Label(about_frame, text=about_text, 
                              justify='left', font=('Arial', 10),
                              bg='#f0f0f0')
        about_label.pack(padx=20, pady=20)
        
    def generate_horoscope(self):
        """Generate horoscope based on input data"""
        try:
            # Validate inputs
            day = int(self.day_var.get())
            month = int(self.month_var.get())
            year = int(self.year_var.get())
            hour = int(self.hour_var.get())
            minute = int(self.minute_var.get())
            
            # Create datetime object
            birth_datetime = datetime(year, month, day, hour, minute)
            
            # Get location
            city = self.city_var.get()
            lat = float(self.lat_var.get()) if self.lat_var.get() else None
            lon = float(self.lon_var.get()) if self.lon_var.get() else None
            
            # Update status
            self.status_label.config(text="Generating horoscope... / ဇာတာဖွဲ့နေသည်...")
            self.root.update()
            
            # Generate horoscope
            self.current_horoscope = self.horoscope_gen.generate_complete_horoscope(
                birth_datetime, city, lat, lon
            )
            
            # Display horoscope
            self.display_horoscope()
            
            # Switch to horoscope tab
            self.notebook.select(1)
            
            self.status_label.config(text="Horoscope generated successfully! / ဇာတာဖွဲ့ပြီးပါပြီ!")
            
        except ValueError as e:
            messagebox.showerror("Input Error", f"Please check your input values: {str(e)}")
            self.status_label.config(text="Error in input / ထည့်သွင်းမှုတွင် အမှား")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.status_label.config(text="Error occurred / အမှားဖြစ်ပွားခဲ့သည်")
    
    def display_horoscope(self):
        """Display the generated horoscope"""
        if not self.current_horoscope:
            return
        
        self.horoscope_text.delete(1.0, tk.END)
        
        horoscope = self.current_horoscope
        
        # Header
        header = f"""
{'='*60}
MYANMAR ASTRO HORO - COMPLETE HOROSCOPE
မြန်မာ ရိုးရာ ဇာတာဖွဲ့ - ပြည့်စုံသော ဇာတာ
{'='*60}

"""
        self.horoscope_text.insert(tk.END, header)
        
        # Birth Information
        birth_info = horoscope['birth_info']
        myanmar_cal = horoscope['myanmar_calendar']
        
        birth_section = f"""
BIRTH INFORMATION / မွေးဖွားချိန် အချက်အလက်များ
{'-'*50}
Date & Time: {birth_info['datetime'].strftime('%Y-%m-%d %H:%M')}
Place: {birth_info['place']}
Coordinates: {birth_info['latitude']:.4f}°N, {birth_info['longitude']:.4f}°E
Julian Day: {birth_info['julian_day']:.2f}

Myanmar Calendar: {myanmar_cal['year']} {myanmar_cal['month_name']} {myanmar_cal['day']} {myanmar_cal['lunar_phase']}
Day of Week: {myanmar_cal['day_of_week']}
Animal Year: {horoscope.get('animal_year', 'N/A')}

"""
        self.horoscope_text.insert(tk.END, birth_section)
        
        # Ascendant
        ascendant = horoscope['ascendant']
        ascendant_section = f"""
ASCENDANT (LAGNA) / လဂ်နာ
{'-'*30}
Sign: {ascendant['sign_en']} ({ascendant['sign_mm']})
Degree: {ascendant['degree_in_sign']:.2f}°
Longitude: {ascendant['longitude']:.2f}°

"""
        self.horoscope_text.insert(tk.END, ascendant_section)
        
        # Planetary Positions
        planets_section = "PLANETARY POSITIONS / ဂြိုလ်များ၏ အနေအထား\n" + "-"*50 + "\n"
        
        for planet, data in horoscope['planets'].items():
            planet_mm = self.horoscope_gen.planets.get(planet, planet)
            retrograde = " (R)" if data['retrograde'] else ""
            planets_section += f"{planet} ({planet_mm}){retrograde}: {data['sign_en']} ({data['sign_mm']}) {data['degree_in_sign']:.2f}°\n"
        
        planets_section += "\n"
        self.horoscope_text.insert(tk.END, planets_section)
        
        # Houses
        houses_section = "HOUSE POSITIONS / အိမ်များ၏ အနေအထား\n" + "-"*40 + "\n"
        
        for house_num, house_data in horoscope['houses'].items():
            planets_in_house = ", ".join(house_data['planets']) if house_data['planets'] else "Empty"
            houses_section += f"House {house_num} ({house_data['house_name_mm']}): {house_data['sign_en']} - {planets_in_house}\n"
        
        houses_section += "\n"
        self.horoscope_text.insert(tk.END, houses_section)
        
        # Birth Nakshatra
        nakshatra = horoscope['birth_nakshatra']
        nakshatra_section = f"""
BIRTH NAKSHATRA / မွေးဖွားနက္ခတ်
{'-'*35}
Nakshatra: {nakshatra['name_en']} ({nakshatra['name_mm']})
Lord: {nakshatra['lord']} ({nakshatra['lord_mm']})
Pada: {nakshatra['pada']}
Position: {nakshatra['position_percent']:.1f}%

"""
        self.horoscope_text.insert(tk.END, nakshatra_section)
        
        # Dasha Periods
        if 'dasha_periods' in horoscope:
            dasha_section = "DASHA PERIODS / ဒသာကာလများ\n" + "-"*30 + "\n"
            current_dasha = horoscope['dasha_periods']['current_dasha']
            dasha_section += f"Current Dasha: {current_dasha['dasha']} ({current_dasha['dasha_mm']})\n"
            dasha_section += f"Period: {current_dasha['start_date'].strftime('%Y-%m-%d')} to {current_dasha['end_date'].strftime('%Y-%m-%d')}\n\n"
            
            dasha_section += "All Dasha Periods:\n"
            for period in horoscope['dasha_periods']['periods'][:5]:  # Show first 5
                dasha_section += f"{period['dasha']} ({period['dasha_mm']}): {period['years']:.1f} years\n"
            
            dasha_section += "\n"
            self.horoscope_text.insert(tk.END, dasha_section)
        
        # Yogas
        if 'yogas' in horoscope and horoscope['yogas']:
            yoga_section = "SPECIAL YOGAS / အထူးယောဂများ\n" + "-"*30 + "\n"
            for yoga in horoscope['yogas']:
                yoga_section += f"{yoga['name_en']} ({yoga['name_mm']})\n"
                yoga_section += f"Description: {yoga['description']}\n\n"
            
            self.horoscope_text.insert(tk.END, yoga_section)
        
        # Predictions
        if 'predictions' in horoscope:
            predictions = horoscope['predictions']
            pred_section = "ASTROLOGICAL PREDICTIONS / ဗေဒင်ဟောစာများ\n" + "-"*45 + "\n"
            
            for category, preds in predictions.items():
                if preds:
                    pred_section += f"{category.title()}:\n"
                    for pred in preds:
                        pred_section += f"• {pred}\n"
                    pred_section += "\n"
            
            self.horoscope_text.insert(tk.END, pred_section)
        
        # Footer
        footer = f"""
{'='*60}
Generated by Myanmar Astro Horo (Python Version)
Based on Surya Siddhanta Theory
မြန်မာ ရိုးရာ ဇာတာဖွဲ့ (Python ဗားရှင်း)
သူရိယသိဒ္ဓန္တ သီအိုရီအပေါ် အခြေခံ၍
{'='*60}
        """
        self.horoscope_text.insert(tk.END, footer)
    
    def show_myanmar_calendar(self):
        """Show current Myanmar calendar information"""
        current_date = datetime.now()
        myanmar_cal = self.horoscope_gen.calendar.gregorian_to_myanmar(current_date)
        
        calendar_info = f"""
MYANMAR CALENDAR INFORMATION
မြန်မာပြက္ခဒိန် အချက်အလက်များ

Today's Date: {current_date.strftime('%Y-%m-%d')}
Myanmar Date: {myanmar_cal['year']} {myanmar_cal['month_name']} {myanmar_cal['day']} {myanmar_cal['lunar_phase']}
Day of Week: {myanmar_cal['day_of_week']}

Myanmar Months:
တန်ခူး, ကဆုန်, နယုန်, ဝါဆို, ဝါခေါင်, တော်သလင်း,
သီတင်းကျွတ်, တန်ဆောင်မုန်း, နတ်တော်, ပြာသို, တပေါင်း, တပေါင်းလဆန်း

Days of Week:
တနင်္လာ (Monday), တနင်ဂါ (Tuesday), ဗုဒ္ဓဟူး (Wednesday),
ကြာသပတေး (Thursday), သောကြာ (Friday), စနေ (Saturday), တနင်္ဂနွေ (Sunday)
        """
        
        self.calendar_text.delete(1.0, tk.END)
        self.calendar_text.insert(tk.END, calendar_info)
    
    def export_to_text(self):
        """Export horoscope to text file"""
        if not self.current_horoscope:
            messagebox.showwarning("No Data", "Please generate a horoscope first.")
            return
        
        from tkinter import filedialog
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(self.horoscope_text.get(1.0, tk.END))
                messagebox.showinfo("Success", f"Horoscope exported to {filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to export: {str(e)}")
    
    def export_to_json(self):
        """Export horoscope data to JSON file"""
        if not self.current_horoscope:
            messagebox.showwarning("No Data", "Please generate a horoscope first.")
            return
        
        from tkinter import filedialog
        filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if filename:
            try:
                # Convert datetime objects to strings for JSON serialization
                exportable_data = self.make_json_serializable(self.current_horoscope)
                
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(exportable_data, f, indent=2, ensure_ascii=False)
                messagebox.showinfo("Success", f"Horoscope data exported to {filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to export: {str(e)}")
    
    def make_json_serializable(self, obj):
        """Convert datetime objects to strings for JSON serialization"""
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, date):
            return obj.isoformat()
        elif isinstance(obj, dict):
            return {key: self.make_json_serializable(value) for key, value in obj.items()}
        elif isinstance(obj, list):
            return [self.make_json_serializable(item) for item in obj]
        else:
            return obj
    
    def run(self):
        """Start the GUI application"""
        self.root.mainloop()


def main():
    """Main function to run the application"""
    app = MyanmarAstroHoroGUI()
    app.run()


if __name__ == "__main__":
    main()
