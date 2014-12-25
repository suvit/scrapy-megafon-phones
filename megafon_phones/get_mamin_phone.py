import sys

def is_mamin_phone(phone):
    #if phone[3] not in ['3', '4']:
    #    return False
    #if '92222' in phone:
    #    return True
    #else:
    #    return False

    main = int(phone[3])
    #print main, phone[5] == str(main * 2), phone[7:9] == str(main *4)
    #print phone[4], phone[6], phone[9]
    if not (phone[4] == phone[6] == phone[9]):
        return False
    #return True
    if (phone[5] == str(main * 2)
           and (phone[7:9] == str(main * 4).zfill(2) or phone[7:9] == str(main * 3).zfill(2))
           ):
        return True
    if (main + int(phone[7:9])) == int(phone[5]) * 2:
        return True
    return False

print 'mamin', is_mamin_phone('9043868128')

with open('megafon_phones_data.txt', 'r') as f:
    for phone in f.readlines():
        #print 'checking', phone
        if not phone.strip():
            continue

        if is_mamin_phone(phone):
            print phone

sys.exit(0)

phones = {}
with open('megafon_phones_data.txt', 'r') as f:
    for phone in f.readlines():
        #print 'checking', phone
        if not phone.strip():
            continue

        phones[phone] = phones.get(phone, 0) + 1


print len(phones)
