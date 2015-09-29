
import unittest
from ..app.persons import Staff, Fellow
from ..app.spaces import Room, OfficeSpace, LivingSpace


class RoomTests(unittest.TestCase):

    def setUp(self):
        self.room = Room("Carat")

    def test_instance_must_have_name(self):
        with self.assertRaises(TypeError):
            Room()
        with self.assertRaises(AttributeError):
            self.room.name = None

    def test_raises_error_if_name_is_not_string(self):
        with self.assertRaises(TypeError):
            Room(234899)



class OfficeSpaceTests(unittest.TestCase):

    def setUp(self):
        self.room = OfficeSpace("CRUCIBLE")
        self.persons = [
            Fellow("JANE DOE", "Y", gender="F"),
            Fellow("JOHN DOE", "N", gender="M"),
            Fellow("JEN DOE", "Y", gender="F"),
            Fellow("JIM DOE", "N", gender="M"),
            Staff("LAGBAJA"),
            Staff("OSADEBE"),
            Staff("AWILO UZO"),
        ]

    def test_purpose_is_readonly(self):
        with self.assertRaises(AttributeError):
            self.room.purpose = 'LIVING'

    def test_occupant_role_is_readonly(self):
        with self.assertRaises(AttributeError):
            self.room.occupant_role = 'FELLOW'

    def test_raises_error_if_occupant_role_is_not_valid(self):
        with self.assertRaises(ValueError):
            OfficeSpace("JOHN DOE", occupant_role="binklmskl")

    def test_add_occupant_adds_to_occupants_list(self):
        room = OfficeSpace("CRUCIBLE")
        room.add_occupant(Staff("LAGBAJA"))
        self.assertEqual(len(room.occupants), 1)

    def test_added_occupants_never_exceeds_max_occpants(self):
        for person in self.persons:
            self.room.add_occupant(person)
        self.assertEqual(len(self.room.occupants), 6)

    def test_add_occupant_adds_only_person_instances(self):
        room = OfficeSpace("CRUCIBLE")
        self.assertFalse(room.add_occupant("invalid value"))

    def test_add_occupant_accepts_only_lists_of_persons(self):
        room = OfficeSpace("CRUCIBLE")
        self.assertFalse(room.add_occupants(65789))

    def test_add_occupant_uses_occupant_role_if_specified(self):
        room = OfficeSpace("CRUCIBLE", occupant_role='STAFF')
        self.assertFalse(room.add_occupant(Fellow("JIM DOE", "N", gender="M")))

    def test_repr_returns_correct_values(self):
        self.room = OfficeSpace("CRUCIBLE")
        self.assertEqual(str(self.room), "CRUCIBLE (OFFICE)")
        # test again with occupant_role specified:
        self.room = OfficeSpace("CRUCIBLE", occupant_role="STAFF")
        self.assertEqual(str(self.room), "CRUCIBLE (OFFICE STAFF)")



class LivingSpaceTests(unittest.TestCase):

    def setUp(self):
        self.room = LivingSpace("SAPELE")
        self.persons = [
            Fellow("JANE DOE", "Y", gender="F"),
            Fellow("JOHN DOE", "Y", gender="M"),
            Fellow("JEN DOE", "Y", gender="F"),
            Fellow("JIM DOE", "Y", gender="M"),
            Fellow("JOE DOE", "Y", gender="M"),
            Staff("OSADEBE"),
            Staff("AWILO UZO"),
        ]

    def test_purpose_is_readonly(self):
        with self.assertRaises(AttributeError):
            self.room.purpose = 'OFFICE'

    def test_occupant_gender_is_readonly(self):
        with self.assertRaises(AttributeError):
            self.room.occupant_gender = 'M'

    def test_raises_error_if_occupant_gender_is_not_valid(self):
        with self.assertRaises(ValueError):
            LivingSpace("SAPELE", occupant_gender="dljskn")

    def test_add_occupant_adds_to_occupants_list(self):
        room = LivingSpace("SAPELE")
        room.add_occupant(Fellow("LAGBAJA", "Y"))
        self.assertEqual(len(room.occupants), 1)

    def test_added_occupants_never_exceeds_max_occpants(self):
        for person in self.persons:
            self.room.add_occupant(person)
        self.assertEqual(len(self.room.occupants), 4)

    def test_add_occupant_adds_only_fellow_instances(self):
        room = LivingSpace("SAPELE")
        self.assertFalse(room.add_occupant(Staff("OSADEBE")))

    def test_add_occupants_accepts_only_lists_of_persons(self):
        room = OfficeSpace("CRUCIBLE")
        self.assertFalse(room.add_occupants(65789))

    def test_add_occupant_adds_only_fellows_with_want_living_yes(self):
        room = LivingSpace("SAPELE")
        self.assertFalse(room.add_occupant(Fellow("OSADEBE", "N")))

    def test_add_occupant_uses_occupant_gender_if_specified(self):
        room = LivingSpace("SAPELE", occupant_gender='F')
        self.assertFalse(room.add_occupant(Fellow("JIM DOE", "N", gender="M")))

    def test_repr_returns_correct_values(self):
        self.room = LivingSpace("SAPELE")
        self.assertEqual(str(self.room), "SAPELE (LIVING)")
        
        # test again with occupant_role specified:
        self.room = LivingSpace("SAPELE", occupant_gender="F")
        self.assertEqual(str(self.room), "SAPELE (LIVING F)")