#!/usr/bin/env python3
"""
PWA Icon Generator Script
This script generates all required PWA icon sizes from your existing icon.png
"""

import os
from PIL import Image
import sys

def generate_pwa_icons():
    """Generate all required PWA icon sizes"""
    
    # Icon sizes required for PWA
    icon_sizes = [72, 96, 128, 144, 152, 192, 384, 512]
    
    # Source icon path
    source_icon = "static/images/icon.png"
    output_dir = "static/images/icons"
    
    if not os.path.exists(source_icon):
        print(f"Error: Source icon not found at {source_icon}")
        return False
    
    try:
        # Open source image
        with Image.open(source_icon) as img:
            # Convert to RGBA if not already
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            
            print(f"Source image size: {img.size}")
            
            # Generate each required size
            for size in icon_sizes:
                # Resize image
                resized_img = img.resize((size, size), Image.Resampling.LANCZOS)
                
                # Save icon
                output_path = os.path.join(output_dir, f"icon-{size}x{size}.png")
                resized_img.save(output_path, "PNG", optimize=True)
                print(f"Generated: {output_path}")
            
            print("\nAll PWA icons generated successfully!")
            return True
            
    except Exception as e:
        print(f"Error generating icons: {e}")
        return False

def create_favicon():
    """Create favicon.ico from the source icon"""
    source_icon = "static/images/icon.png"
    favicon_path = "static/favicon.ico"
    
    try:
        with Image.open(source_icon) as img:
            # Create multiple sizes for favicon
            favicon_sizes = [(16, 16), (32, 32), (48, 48)]
            favicon_images = []
            
            for size in favicon_sizes:
                resized = img.resize(size, Image.Resampling.LANCZOS)
                favicon_images.append(resized)
            
            # Save as ICO file
            favicon_images[0].save(
                favicon_path,
                format='ICO',
                sizes=[(16, 16), (32, 32), (48, 48)]
            )
            print(f"Generated favicon: {favicon_path}")
            
    except Exception as e:
        print(f"Error creating favicon: {e}")

if __name__ == "__main__":
    print("PWA Icon Generator")
    print("==================")
    
    # Check if PIL is available
    try:
        from PIL import Image
    except ImportError:
        print("Error: Pillow library not found.")
        print("Install it with: pip install Pillow")
        sys.exit(1)
    
    # Create output directory if it doesn't exist
    os.makedirs("static/images/icons", exist_ok=True)
    
    # Generate icons
    if generate_pwa_icons():
        create_favicon()
        print("\n✅ PWA setup complete!")
        print("\nNext steps:")
        print("1. Test your PWA at: https://web.dev/measure/")
        print("2. Verify manifest at: /manifest.json")
        print("3. Check service worker at: /static/js/sw.js")
    else:
        print("\n❌ Icon generation failed!")
        sys.exit(1)