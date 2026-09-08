import os
from PIL import Image, ImageDraw

def process_image():
    print("\n--- قسم معالجة الصور بالذكاء الاصطناعي ---")
    
    img_path = "logo_test.jpg"
    img = Image.new('RGB', (800, 600), color = (73, 109, 137))
    d = ImageDraw.Draw(img)
    d.text((250, 280), "Al-Hamza Pro", fill=(255, 255, 0))
    img.save(img_path)
    print(f"[+] تم إنشاء صورة تجريبية باسم {img_path} بنجاح!")

    try:
        with Image.open(img_path) as img:
            print(f"[+] الأبعاد الحالية للصورة: {img.size}")
            
            width, height = img.size
            new_size = (width // 2, height // 2)
            resized_img = img.resize(new_size)
            
            output_name = "output_" + img_path
            resized_img.save(output_name)
            print(f"[✓] تم تصغير وحفظ الصورة الجديدة بنجاح باسم: {output_name}")
    except Exception as e:
        print(f"[!] حدث خطأ: {e}")

def main():
    while True:
        print("\n========================================")
        print("   Al-Hamza Pro - الحمزة برو")
        print("   Image & Video Editor App")
        print("========================================")
        print("1. Edit & Enhance Images")
        print("2. Cut & Edit Videos (قريباً)")
        print("3. Arabic Fonts & Text Effects (قريباً)")
        print("4. Exit (خروج)")
        
        choice = input("\nSelect an option (1-4): ")
        
        if choice == '1':
            process_image()
        elif choice == '2':
            print("\n[+] Video cutter feature is under development...")
        elif choice == '3':
            print("\n[+] Loading Arabic fonts manager...")
        elif choice == '4':
            print("\n[!] شكراً لاستخدامك الحمزة برو. إلى اللقاء!")
            break
        else:
            print("\n[!] Invalid choice, please try again.")

if __name__ == "__main__":
    main()
	

