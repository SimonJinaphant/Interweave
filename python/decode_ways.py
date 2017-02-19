def decode_interpretation(message):
    _decode("", list(message))


def _decode(current_message, pending_digits):
    if len(pending_digits) == 0:
        print current_message
        return

    single_decode_message = current_message + chr( ord('a') + int(pending_digits[0]) - 1)
    single = pending_digits.pop(0)
    _decode(single_decode_message, pending_digits[:])

    if len(pending_digits) >= 1:
        double_decode_message = current_message + chr( ord('a') + int( single + pending_digits[0]) - 1)
        pending_digits.pop(0)
        _decode(double_decode_message, pending_digits[:])

print decode_interpretation("121")