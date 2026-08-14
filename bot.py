def bot_javob(xabar):
    xabar = xabar.lower()
    if "salom" in xabar:
        return "Salom! Sizga qanday yordam bera olaman?"
    elif "ism" in xabar:
        return "Men oddiy Python botman!"
    elif "xayr" in xabar:
        return "Xayr, ko'rishguncha!"
    else:
        return "Kechirasiz, tushunmadim. Boshqacha yozib ko'ring."

print("Bot ishga tushdi! Chiqish uchun 'xayr' deb yozing.")

while True:
    foydalanuvchi = input("Siz: ")
    javob = bot_javob(foydalanuvchi)
    print("Bot:", javob)
    if "xayr" in foydalanuvchi.lower():
        break