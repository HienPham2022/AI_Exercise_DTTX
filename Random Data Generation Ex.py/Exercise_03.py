#Tạo OTP bảo mật ngẩu nhiên 6 chữ sô
import secrets

secretsGenerator = secrets.SystemRandom()
print("Generating 6 digit random OTP")
otp = secretsGenerator.randrange(100000,999999)
print("Secure random OTP is",otp)