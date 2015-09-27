
import unittest
from ..app.persons import Person, Staff, Fellow


class GenericPersonTests(unittest.TestCase):

    def setUp(self):
        self.person = Person("AWILI UZO")


    def test_person_instance_must_have_name(self):
        with self.assertRaises(TypeError):
            Person()
        with self.assertRaises(AttributeError):
            self.person.name = None

    def test_person_raises_error_if_name_is_not_string(self):
        with self.assertRaises(TypeError):
            Person(234899)



class StaffTests(unittest.TestCase):

    def setUp(self):
        self.person = Staff("JANE DOE")

    def test_staff_role_property_is_readonly(self):
        with self.assertRaises(AttributeError):
            self.person.role = Person.FELLOW

    def test_staff_repr_returns_correct_values(self):
        self.assertEqual(str(self.person), "JANE DOE [STAFF]")



class FellowTests(unittest.TestCase):

    def setUp(self):
        Fellow.gender_aware = True
        self.person = Fellow("JANE DOE", **{
            "gender": "F",
            "wants_living_space": "Y",
        })

    def test_fellow_role_is_readonly(self):
        with self.assertRaises(AttributeError):
            self.person.role = 'FELLOW'

    def test_fellow_gender_is_readonly(self):
        with self.assertRaises(AttributeError):
            self.person.gender = 'M'

    def test_fellow_raises_error_if_gender_is_not_valid(self):
        with self.assertRaises(ValueError):
            Fellow("JOHN DOE", **{
                "gender": "binklmskl",
                "wants_living_space": "N",
            })

    def test_fellow_wants_living_space_is_readonly(self):
        with self.assertRaises(AttributeError):
            self.person.wants_living_space = 'N'

    def test_fellow_raises_error_if_wants_living_space_is_not_valid(self):
        with self.assertRaises(ValueError):
            Fellow("JOHN DOE", **{
                "gender": 'M',
                "wants_living_space": "gjhklms",
            })

    def test_fellow_repr_returns_correct_values(self):
        self.assertEqual(str(self.person), "JANE DOE [FELLOW F]")
        Fellow.gender_aware = False
        self.assertEqual(str(self.person), "JANE DOE [FELLOW]")



if __name__ == '__main__':
    unittest.main()
