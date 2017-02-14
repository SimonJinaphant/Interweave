def ransom_note(message, magazine):
    if len(magazine) < len(message):
        return False

    scope_var = {"m_pos": 0}
    record = {}

    def search_until(letter):
        while scope_var["m_pos"] < len(magazine):
            m_letter = magazine[scope_var["m_pos"]]
            if m_letter == letter:
                return True
            else:
                if m_letter in record:
                    record[m_letter] += 1
                else:
                    record[m_letter] = 1
            scope_var["m_pos"] += 1
        return False

    for letter in message:
        if letter in record:
            record[letter] -= 1
            if record[letter] < 0:
                return False
        else:
            if not search_until(letter):
                return False

    return True

print ransom_note("hello", "theendisnearallofhere")
print ransom_note("hello", "teendisnearallofwere")