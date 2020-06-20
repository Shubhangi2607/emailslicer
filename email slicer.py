import string

s=input("enter the email address")

index=s.find("@")

print("your username is",s[:index])


print("your domain name is",s[index+1:])



