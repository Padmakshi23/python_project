# substring datatypes

data = "Hello fnwejfuwej world"

print(data[0])

print(data[0:3])

print(data[1:])

print(data[-1])

print(data[-7:])

print(data.index("world"))

print(data.replace("world", "princy"))

mail_id = "princy@123.gmail.com"

print(mail_id[0:7])

result = mail_id[0:mail_id.index('@')]
print(result)

res = mail_id.split("@")
print(res)
print(res[0])

res = (mail_id.split("@")[0])
print("new",res)