def ransom_note(message, magazine):
    """
    Given a magazine containing cut-outs of invidual words, determine if a message can be constructed

    :param message: The message to construct (no whitespaces)
    :param magazine: The collection of letters we have (no whitespaces)

    :return: True is the message can be made from the magazine
    """
    if len(magazine) < len(message):
        # Impossible to construct message; this only works if there's no whitespace involved
        # otherwise a message of "abc__" and a magazine of "abc" will be overlooked
        return False

    # This is a python 2.7 hack to get immutable outer function variables to be accessible
    # from within nested functions
    scope_var = {"m_pos": 0}

    # We keep a count record of how many letters we've seen/used
    # If an entry is positive it means the magazine has that many cut-out letters available
    record = {}

    def search_until(letter):
        """
        Iterate the magazine, recording letters we find along the way until
        we hit the letter we're looking for

        :param letter: The letter to look for
        :return: False if we reach the end of the magazine
        """
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

            if record[letter] == 0:
                # Remove the record for this letter, forcing the search in the magazine
                del record[letter]
        else:
            # There's no such letter in our record, we'll search the magazine for more letters

            if not search_until(letter):
                # We'd reach the end of the magazine,
                # the message cannot be completed because of the missing letter
                return False

    return True

print ransom_note("hello", "theendisnearallofhere")
print ransom_note("hello", "teendisnearallofwere")