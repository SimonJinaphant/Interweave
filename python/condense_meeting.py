from __future__ import absolute_import
import unittest


def condense_meetings(time_slots):
    """
    Given a time slots of meetings, merge meetings which overlap to avoid scheduling more rooms.

    :param time_slots: List of 2D Integer tuples in the format (start_time, end_time)
    :return: List of 2D integer tuples
    """
    # Sort by their starting time to simplify the scheduling logic.
    time_slots.sort()

    time_stack = []
    time_stack.append(time_slots[0])

    for start_time, end_time in time_slots:
        if time_stack[-1][1] >= start_time:
            # The meeting overlaps with a previous meeting; combine them
            prev_start, prev_end = time_stack.pop()
            time_stack.append((prev_start, end_time))
        else:
            # The meetings don't overlap
            time_stack.append((start_time, end_time))

    return time_stack


class CondenseMeetingTest(unittest.TestCase):
    def test_normals(self):
        self.assertEquals(condense_meetings([(0,1), (3,5), (4,8), (10,12), (9,10)]), [(0,1),(3,8),(9,12)])


if __name__ == "__main__":
    unittest.main()