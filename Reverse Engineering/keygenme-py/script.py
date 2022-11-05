import hashlib

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial

username_trial = b"FREEMAN"

potential_key = ""

pos = [4,5,3,6,2,7,1,8]

for i in pos:
    potential_key += hashlib.sha256(username_trial).hexdigest()[i]
    
key = key_part_static1_trial + potential_key + key_part_static2_trial

print(key)