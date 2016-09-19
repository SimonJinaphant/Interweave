def condense_meeting_time(meeting_time):
    meeting_slots = [None] * 16

    for current_index, meeting in enumerate(meeting_time):
        start = meeting[0]
        end = meeting[1]

        if meeting_slots[start] is not None:
            # There's a meeting already going on at this time!
            new_index = start
            end = meeting_time[new_index][1] = max(meeting_time[current_index][1], meeting_time[new_index][1])
            meeting_time[current_index] = None
            current_index = new_index

        replacing = None
        #Change to while loop until end is reached
        for i in xrange(start, end+1):
            current_meeting = meeting_slots[i]
            if current_meeting is not None:
                if current_meeting != current_index and replacing != current_meeting:
                    end = meeting_time[current_index][1] = max(meeting_time[current_meeting][1], meeting_time[current_index][1])
                    meeting_time[current_meeting] = None
                    replacing = current_meeting

            else:
                meeting_slots[i] = current_index

    return None