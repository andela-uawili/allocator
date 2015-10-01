
import unittest

from ..app import settings
from ..app.persons import Staff, Fellow
from ..app.spaces import Room, OfficeSpace, LivingSpace


class RoomTests(unittest.TestCase):

    def setUp(self):
        self.persons = [
            Fellow("JANE DOE", "Y", gender="F"),
            Fellow("JOHN DOE", "Y", gender="M"),
            Fellow("JEN DOE", "Y", gender="F"),
            Fellow("JIM DOE", "Y", gender="M"),
            Fellow("JOE DOE", "Y", gender="M"),
            Staff("OSADEBE"),
            Staff("AWILO UZO"),
        ]

    def test_instance_must_have_name(self):
        with self.assertRaises(TypeError):
            Room()

    def test_raises_error_if_name_is_not_string(self):
        with self.assertRaises(TypeError):
            Room(234899)

    def test_add_occupant_adds_to_occupants_list(self):
        room = Room("SAPELE")
        room.add_occupant(Fellow("LAGBAJA", "Y"))
        self.assertEqual(len(room.occupants), 1)

    def test_added_occupant_never_exceeds_max_occpants(self):
        room = LivingSpace("SAPELE")
        for person in self.persons:
            room.add_occupant(person)
        self.assertEqual(len(room.occupants), 4)

    def test_add_occupant_adds_only_person_instances(self):
        room = Room("SAPELE")
        self.assertFalse(room.add_occupant(None))

    def test_add_occupants_accepts_only_lists(self):
        room = Room("CRUCIBLE")
        self.assertFalse(room.add_occupants({}))



class OfficeSpaceTests(unittest.TestCase):

    def setUp(self):
        self.room = OfficeSpace("CRUCIBLE")

    def test_raises_error_if_occupant_role_is_not_valid(self):
        with self.assertRaises(ValueError):
            OfficeSpace("JOHN DOE", occupant_role="binklmskl")

    def test_repr_returns_correct_values(self):
        self.room = OfficeSpace("CRUCIBLE")
        self.assertEqual(str(self.room), "CRUCIBLE (OFFICE)")
        # test again with occupant_role specified:
        self.room = OfficeSpace("CRUCIBLE", occupant_role="STAFF")
        self.assertEqual(str(self.room), "CRUCIBLE (OFFICE ST)")



class LivingSpaceTests(unittest.TestCase):

    def setUp(self):
        self.room = LivingSpace("SAPELE")

    def test_raises_error_if_occupant_gender_is_not_valid(self):
        with self.assertRaises(ValueError):
            LivingSpace("SAPELE", occupant_gender="dljskn")

    def test_repr_returns_correct_values(self):
        self.room = LivingSpace("SAPELE")
        self.assertEqual(str(self.room), "SAPELE (LIVING)")
        
        # test again with occupant_role specified:
        self.room = LivingSpace("SAPELE", occupant_gender="F")
        self.assertEqual(str(self.room), "SAPELE (LIVING F)")