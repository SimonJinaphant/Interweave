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


def merge_meetings(time_slots):
    """
    Given a time slots of meetings, merge meetings which overlap to avoid scheduling more rooms.

    :param time_slots: List of 2D Integer tuples in the format (start_time, end_time)
    :return: List of 2D integer tuples
    """
    # Sort by their starting time
    time_slots.sort()

    time_stack = []
    time_stack.append(time_slots[0])

    for start_time, end_time in time_slots:

        # This meeting overlaps!
        if time_stack[-1][1] >= start_time:
            prev_start, prev_end = time_stack.pop()
            time_stack.append((min(prev_start, start_time), max(prev_end, end_time)))
        else:
            time_stack.append((start_time, end_time))

    return time_stack

print merge_meetings([(0,1), (3,5), (4,8), (10,12), (9,10)])
