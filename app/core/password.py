import bcrypt
import secrets
import string

def verify_password(plain_password: str, hashed_password: str, salt: str) -> bool:
    try:
        print(f"[DEBUG] Verifying password:")
        print(f"[DEBUG] Plain password: {plain_password}")
        print(f"[DEBUG] Hashed password: {hashed_password}")
        print(f"[DEBUG] Salt: {salt}")
        
        # Kết hợp password với salt
        password_with_salt = f'{plain_password}{salt}'
        print(f"[DEBUG] Password with salt: {password_with_salt}")
        
        # Chuyển đổi password_with_salt thành bytes
        password_bytes = password_with_salt.encode('utf-8')
        # Chuyển đổi hashed_password thành bytes
        hashed_bytes = hashed_password.encode('utf-8')
        # So sánh password
        result = bcrypt.checkpw(password_bytes, hashed_bytes)
        print(f"[DEBUG] Verification result: {result}")
        return result
    except Exception as e:
        print(f"[DEBUG] Error verifying password: {str(e)}")
        return False

def get_password_hash(password: str, salt: str) -> str:
    try:
        print(f"[DEBUG] Hashing password: {password}")
        print(f"[DEBUG] Using salt: {salt}")
        
        # Kết hợp password với salt
        password_with_salt = f'{password}{salt}'
        print(f"[DEBUG] Password with salt: {password_with_salt}")
        
        # Chuyển đổi password_with_salt thành bytes
        password_bytes = password_with_salt.encode('utf-8')
        # Tạo salt cho bcrypt
        bcrypt_salt = bcrypt.gensalt()
        # Hash password với salt
        hashed = bcrypt.hashpw(password_bytes, bcrypt_salt)
        # Chuyển đổi bytes thành string
        result = hashed.decode('utf-8')
        print(f"[DEBUG] Hashed result: {result}")
        return result
    except Exception as e:
        print(f"[DEBUG] Error hashing password: {str(e)}")
        raise

def generate_random_string(length=8):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(secrets.choice(characters) for i in range(length))
    return random_string
    
def get_salt()->str:
    salt= generate_random_string()
    return salt 