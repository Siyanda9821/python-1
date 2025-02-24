message = "  Programming in Python is not only powerful but also fun! "

trim = message.strip()
print(trim)
new_message = (message[17:24]) + "-" + message[35:45]

print(new_message.upper())


# Task 2

flipped_message = "!nuf sseldnE dna seitinutroppo lufrewop htiw nohtyP"

c_message = flipped_message[::-1]
print(c_message)
new_c_message = (c_message[0:6]) + "🗡️ " + c_message[12:21] + "🌸"
print(new_c_message.lower())

# Task 3

message_3 = "    🚨🔍📱🔑secret_code✌️"
message_3 = message_3.strip()
print(message_3.find("🔑"))
message_3_cut = message_3[4:]
print(message_3_cut.upper())
