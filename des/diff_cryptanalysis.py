from simpdes import encrypt, expander

key = '010011010'

message_a = '000111011011'
left_a1, right_a1 = message_a[0:6], message_a[6:12]

output_a = encrypt(message_a, key, 3)
left_a4, right_a4 = output_a[0:6], output_a[6:12]

print left_a1, right_a1
print left_a4, right_a4

print

message_b = '101110011011'
left_b1, right_b1 = message_b[0:6], message_b[6:12]

output_b = encrypt(message_b, key, 3)
left_b4, right_b4 = output_b[0:6], output_b[6:12]

print left_b1, right_b1
print left_b4, right_b4

print

left_x1 = "{0:06b}".format(int(left_a1, 2) ^ int(left_b1, 2))
right_x1 = "{0:06b}".format(int(right_a1, 2) ^ int(right_b1, 2))  # expected because right_a1 = right_b1
left_x4 = "{0:06b}".format(int(left_a4, 2) ^ int(left_b4, 2))
right_x4 = "{0:06b}".format(int(right_a4, 2) ^ int(right_b4, 2))
print left_x1, right_x1
print left_x4, right_x4

print

print expander(left_a4)
print expander(left_b4)

print

e_leftx4 = expander(left_x4)
print e_leftx4
print "{0:06b}".format(int(right_x4, 2) ^ int(left_x1, 2))

print
for i in range(16):
    print "{0:04b}".format(int(e_leftx4[-4:], 2) - i), "{0:04b}".format(i)
