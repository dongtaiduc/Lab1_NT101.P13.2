def toCharCode(char):
    return ord(char) - ord('a')

def toChar(charCode):
    char = charCode + ord('a')
    return chr(char)

# Nhập text và key từ người dùng
text = input("Nhập văn bản cần mã hóa hoặc giải mã: ").strip().lower()
key = input("Nhập khóa (key): ").strip().lower()
operation = input("Bạn muốn mã hóa (e) hay giải mã (d)? ").strip().lower()

keyStep = []

# Chuyển đổi key thành danh sách các bước mã hóa/giải mã
for char in key:
    charCode = toCharCode(char)
    keyStep.append(charCode)

keySize = len(keyStep)
keyStepIdx = 0
resultMessage = ""

# Mã hóa hoặc giải mã văn bản
for char in text:
    if char.isalpha():
        charCode = toCharCode(char)
        if operation == 'e':  # Mã hóa
            charCode += keyStep[keyStepIdx % keySize]
        elif operation == 'd':  # Giải mã
            charCode -= keyStep[keyStepIdx % keySize]
        resultMessage += toChar(charCode % 26)
        keyStepIdx += 1
    else:
        resultMessage += char

if operation == 'e':
    print(f"Văn bản đã mã hóa: {resultMessage}")
elif operation == 'd':
    print(f"Văn bản đã giải mã: {resultMessage}")
else:
    print("Thao tác không hợp lệ! Hãy nhập 'e' để mã hóa hoặc 'd' để giải mã.")
