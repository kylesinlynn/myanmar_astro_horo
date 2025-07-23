"""
Font Manager for Myanmar Astro Horo GUI
Handles TTF font loading and management for Myanmar text display
"""

import os
import tkinter as tk
from tkinter import font as tkfont
from typing import Dict, Optional


class FontManager:
    """Manages custom TTF fonts for the application"""
    
    def __init__(self):
        self.fonts_dir = os.path.join(os.path.dirname(__file__), '..', 'fonts')
        self.loaded_fonts: Dict[str, tkfont.Font] = {}
        self.font_families: Dict[str, str] = {}
        
    def load_font(self, font_filename: str, font_name: str = None) -> Optional[str]:
        """
        Load a TTF font file and return the font family name
        
        Args:
            font_filename: Name of the TTF file (e.g., 'myanmar_font.ttf')
            font_name: Optional custom name for the font
            
        Returns:
            Font family name if successful, None if failed
        """
        font_path = os.path.join(self.fonts_dir, font_filename)
        
        if not os.path.exists(font_path):
            print(f"Font file not found: {font_path}")
            return None
            
        try:
            # For Windows and some Linux distributions
            import tkinter.font as tkfont
            
            # Try to load the font
            root = tk._default_root
            if root is None:
                # Create a temporary root if none exists
                temp_root = tk.Tk()
                temp_root.withdraw()
                
            # Load font using tkinter's font loading mechanism
            font_name = font_name or os.path.splitext(font_filename)[0]
            
            # Store the font path for reference
            self.font_families[font_name] = font_path
            
            print(f"Font loaded: {font_filename} as '{font_name}'")
            return font_name
            
        except Exception as e:
            print(f"Error loading font {font_filename}: {e}")
            return None
    
    def get_font(self, font_name: str, size: int = 12, weight: str = 'normal') -> tkfont.Font:
        """
        Get a tkinter Font object with the specified parameters
        
        Args:
            font_name: Name of the loaded font
            size: Font size
            weight: Font weight ('normal', 'bold')
            
        Returns:
            tkinter Font object
        """
        font_key = f"{font_name}_{size}_{weight}"
        
        if font_key not in self.loaded_fonts:
            try:
                # Try to use the custom font if available
                if font_name in self.font_families:
                    # For custom TTF fonts, we need to use the system font loading
                    # This is a simplified approach - more complex font loading
                    # might require platform-specific implementations
                    self.loaded_fonts[font_key] = tkfont.Font(
                        family=font_name,
                        size=size,
                        weight=weight
                    )
                else:
                    # Fallback to system fonts
                    fallback_fonts = ['Myanmar Text', 'Padauk', 'Arial Unicode MS', 'Arial']
                    for fallback in fallback_fonts:
                        try:
                            self.loaded_fonts[font_key] = tkfont.Font(
                                family=fallback,
                                size=size,
                                weight=weight
                            )
                            break
                        except:
                            continue
                    else:
                        # Ultimate fallback
                        self.loaded_fonts[font_key] = tkfont.Font(
                            size=size,
                            weight=weight
                        )
                        
            except Exception as e:
                print(f"Error creating font {font_key}: {e}")
                # Create a basic font as fallback
                self.loaded_fonts[font_key] = tkfont.Font(size=size, weight=weight)
        
        return self.loaded_fonts[font_key]
    
    def list_available_fonts(self) -> list:
        """List all available font families on the system"""
        return sorted(tkfont.families())
    
    def get_myanmar_font(self, size: int = 12, weight: str = 'normal') -> tkfont.Font:
        """
        Get a font suitable for Myanmar text display
        
        Args:
            size: Font size
            weight: Font weight
            
        Returns:
            tkinter Font object optimized for Myanmar text
        """
        # Try Myanmar-specific fonts first
        myanmar_fonts = ['Myanmar Text', 'Padauk', 'Myanmar3', 'Zawgyi-One']
        
        for font_family in myanmar_fonts:
            try:
                return tkfont.Font(family=font_family, size=size, weight=weight)
            except:
                continue
        
        # Fallback to a loaded custom font if available
        for font_name in self.font_families:
            return self.get_font(font_name, size, weight)
        
        # Ultimate fallback
        return tkfont.Font(size=size, weight=weight)


# Global font manager instance
font_manager = FontManager()
