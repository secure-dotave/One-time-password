import hashlib
import datetime

def generate_hash():
    # Get current data and time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Generate SHA-256 hash of the date-time string
    hash_object = hashlib.sha256(current_time.encode())
    hex_dig = hash_object.hexdigest()
    # Store hash in a text file
    with open("hash_store.txt", "w") as file:
        file.write(hex_dig)
    return hex_dig

def generate_otp_from_hash(hex_dig):
    # Implementing function F to process the hash and generate the OTP
    otp = ''
    for i, char in enumerate(hex_dig):
        if char.isdigit():
            otp += char
        else:
            otp += str(ord(char) % 10) # Simple mapping from letters to numbers
        if len(otp) == 4:
            break
    return otp

def verify_otp(input_otp):
    with open("hash_store.txt", "r") as file:
        stored_hash = file.read().strip()
    generated_otp = generate_otp_from_hash(stored_hash)
    if input_otp == generated_otp:
        print("OTP Verification Successful")
        # Remove the hash from the file to prevent replay
        open("hash_store.txt", "w").close()
    else:
        print("OTP Verification Unsuccessful")

# Use case example
hex_dig = generate_hash()
OTP = generate_otp_from_hash(hex_dig)
print(f"One Time Password: {OTP}")
# OTP is sent to the user, and hex_dig is stored

# Verification for OTP that was sent to the user
verify_otp(OTP)
