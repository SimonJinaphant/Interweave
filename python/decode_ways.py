def decode_ways(message):
    return _decode_ways("", list(message))

def _decode_ways(current, remaining):

    if len(remaining) == 0:
        print current
        return

    new_current = list(current)
    new_current.append(remaining.pop(0))

    _decode_ways(new_current[:], remaining[:])

    if len(remaining) > 1:
        new_current.append(remaining.pop(0))
        _decode_ways(new_current[:], remaining[:])

print decode_ways("121")