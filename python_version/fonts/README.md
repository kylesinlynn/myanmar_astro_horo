# Font Directory

Place your TTF font files in this directory.

## Recommended Myanmar Fonts

For best Myanmar text display, consider these fonts:
- **Padauk** - Free Myanmar Unicode font
- **Myanmar Text** - Windows system font
- **Noto Sans Myanmar** - Google Noto font family
- **Zawgyi-One** - Popular Myanmar font (legacy encoding)

## Usage in GUI Code

```python
from gui.font_manager import font_manager

# Load a custom TTF font
font_manager.load_font('Pyidaungsu-2.5.3_Regular.ttf', 'Pyidaungsu')

# Use the font in your GUI
myanmar_font = font_manager.get_myanmar_font(size=14)
pyidaungsu_font = font_manager.get_font('Pyidaungsu', size=16, weight='bold')

# Apply to tkinter widgets
label = tk.Label(root, text="မြန်မာ ရိုးရာ ဇာတာဖွဲ့", font=myanmar_font)
title = tk.Label(root, text="Title", font=pyidaungsu_font)
```

## Font Files to Add

1. Download your preferred Myanmar TTF fonts
2. Copy them to this directory
3. Use the font_manager to load and apply them in your GUI

Example font files:
- `Pyidaungsu-2.5.3_Regular.ttf`
