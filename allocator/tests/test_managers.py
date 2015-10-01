import unittest
import __builtin__ as builtins
from StringIO import StringIO
from mock import patch, MagicMock

from ..app import settings
from ..app.spaces import OfficeSpace, LivingSpace
from ..app.persons import Fellow, Staff
from ..app.managers import FacilityManager


class FaciltyManagerLoadTest(unittest.TestCase):

    def setUp(self):

        self.manager =  FacilityManager()

        self.mock_file_obj_1 = MagicMock()
        self.mock_file_obj_1.readlines = MagicMock(return_value=[
            "SANAA LATHER            FELLOW      Y       F",
            "KAMY BIN               STAFF",
            "KOBE BRYSNT            FELLOW      Y       M",
            "KIRTDAE O'CONNOR        STAFF",
            "PHPIYANU LOMRSE         FELLOW      Y       F",
            "WUXIX KILO                 STAFF",
        ])
        self.mock_file_obj_2 = MagicMock()
        self.mock_file_obj_2.readlines = MagicMock(return_value=[
            "GILD            OFFICE        FELLOW",
            "IROKO           LIVING                        F",
            "CEDAR           LIVING                        M",
        ])

        
    @patch.object(builtins, 'open')
    def test_loads_team_data_correctly(self, mock_open):
        
        mock_open.return_value = self.mock_file_obj_1
        self.manager.load(target="team", filepath="./data/input_persons_ext.txt", mode=settings.OVERWRITE)
        self.assertEquals(len(self.manager.teamdir), 6)
        self.assertEquals(self.manager.teamdir[3].name, "KIRTDAE O'CONNOR")

    
    @patch.object(builtins, 'open')
    def test_loads_rooms_data_correctly(self, mock_open):
        
        mock_open.return_value = self.mock_file_obj_2
        self.manager.load(target="rooms", filepath="./data/input_rooms_ext.txt", mode=settings.OVERWRITE)
        self.assertEquals(len(self.manager.roomsdir), 3)
        self.assertEquals(self.manager.roomsdir[1].name, "IROKO")



class FaciltyManagerInputTest(unittest.TestCase):

    def setUp(self):

        self.manager =  FacilityManager()

        self.team_input_lines = "SANAA LATHER  FELLOW  Y  F, KAMY BIN STAFF, WUXIX KILO STAFF"
        self.room_input_lines = "GILD OFFICE  FELLOW, IROKO  LIVING  F, CEDAR   LIVING   M"


    def test_inputs_team_data_correctly(self):
        
        self.manager.input("team", self.team_input_lines, mode=settings.OVERWRITE)
        self.assertEquals(len(self.manager.teamdir), 3)
        self.assertEquals(self.manager.teamdir[1].name, "KAMY BIN")

        self.manager.input("team", self.team_input_lines, mode=settings.APPEND)
        self.assertEquals(len(self.manager.teamdir), 6)
        self.assertEquals(self.manager.teamdir[4].name, "KAMY BIN")

    
    def test_inputs_rooms_data_correctly(self):
        
        self.manager.input("rooms", self.room_input_lines, mode=settings.OVERWRITE)
        self.assertEquals(len(self.manager.roomsdir), 3)
        self.assertEquals(self.manager.roomsdir[1].name, "IROKO")

        self.manager.input("rooms", self.room_input_lines, mode=settings.APPEND)
        self.assertEquals(len(self.manager.roomsdir), 6)
        self.assertEquals(self.manager.roomsdir[4].name, "IROKO")



class FaciltyManagerAllocateTest(unittest.TestCase):

    def setUp(self):

        self.manager =  FacilityManager()
        self.manager.teamdir = [
            Fellow("JANE DOE", "Y", gender="F"),
            Fellow("JOHN DOE", "Y", gender="M"),
            Fellow("JEN DOE", "N", gender="F"),
            Fellow("JIM DOE", "Y", gender="M"),
            Fellow("JOE DOE", "N", gender="M"),
            Staff("OSADEBE"),
            Staff("AWILO UZO"),
        ]
        self.manager.roomsdir = [
            OfficeSpace("CARAT"),
            OfficeSpace("CRUCIBLE"),
            OfficeSpace("ANVIL"),
            OfficeSpace("FORGE"),
            LivingSpace("OBECHE"),
            LivingSpace("SAPELE"),
            LivingSpace("BALSAM"),
        ]

    @patch.object(builtins, 'open')
    def test_allocates_correctly(self, mock_open):

        self.manager.allocate(gender_constraint=settings.DEFAULT_GENDER_CONSTRAINT, role_constraint=settings.DEFAULT_ROLE_CONSTRAINT)
        self.assertIsInstance(self.manager.teamdir[0].office_space, OfficeSpace)
        self.assertIsInstance(self.manager.teamdir[0].living_space, LivingSpace)



class FaciltyManagerPrintTest(unittest.TestCase):

    def setUp(self):

        self.manager =  FacilityManager()
        self.manager.teamdir = [
            Fellow("JANE DOE", "Y", gender="F"),
            Fellow("JOHN DOE", "Y", gender="M"),
            Fellow("JEN DOE", "N", gender="F"),
            Fellow("JIM DOE", "Y", gender="M"),
            Fellow("JOE DOE", "N", gender="M"),
            Staff("OSADEBE"),
            Staff("AWILO UZO"),
        ]
        self.manager.roomsdir = [
            OfficeSpace("CARAT"),
            OfficeSpace("CRUCIBLE"),
            OfficeSpace("ANVIL"),
            OfficeSpace("FORGE"),
            LivingSpace("OBECHE"),
            LivingSpace("SAPELE"),
            LivingSpace("BALSAM"),
        ]
        self.manager.allocate()

    @patch('sys.stdout', new_callable=StringIO)
    def test_prints_team_output_without_filters_correctly(self, mock_stdout):
        
        self.manager.print_to_console("team", filters=None)
        output_str = mock_stdout.getvalue()
        self.assertIn("JANE DOE (FELLOW F)", output_str)


    @patch('sys.stdout', new_callable=StringIO)
    def test_prints_team_output_correctly_1(self, mock_stdout):
        
        self.manager.print_to_console("team", filters="fw fm w+")
        output_str = mock_stdout.getvalue()
        self.assertIn("JANE DOE (FELLOW F)", output_str)

    @patch('sys.stdout', new_callable=StringIO)
    def test_prints_team_output_correctly_2(self, mock_stdout):
        
        self.manager.print_to_console("team", filters="fw fm w-")
        output_str = mock_stdout.getvalue()
        self.assertIn("JEN DOE (FELLOW F)", output_str)

    @patch('sys.stdout', new_callable=StringIO)
    def test_prints_team_output_correctly_1(self, mock_stdout):
        
        self.manager.print_to_console("team", filters="fw l+")
        output_str = mock_stdout.getvalue()
        self.assertIn("JANE DOE (FELLOW F)", output_str)


    @patch('sys.stdout', new_callable=StringIO)
    def test_prints_rooms_output_without_filters_correctly(self, mock_stdout):
        
        self.manager.print_to_console("rooms", filters=None)
        output_str = mock_stdout.getvalue()
        self.assertIn("CRUCIBLE (OFFICE)", output_str)


    @patch('sys.stdout', new_callable=StringIO)
    def test_prints_rooms_output_correctly_1(self, mock_stdout):
        
        self.manager.print_to_console("rooms", filters="os st cf-")
        output_str = mock_stdout.getvalue()
        self.assertIn("CRUCIBLE (OFFICE)", output_str)


    @patch('sys.stdout', new_callable=StringIO)
    def test_prints_rooms_output_correctly_2(self, mock_stdout):
        
        self.manager.print_to_console("rooms", filters="ls fw fm cf-")
        output_str = mock_stdout.getvalue()
        self.assertIn("SAPELE (LIVING)", output_str)


    @patch('sys.stdout', new_callable=StringIO)
    def test_prints_rooms_output_correctly_3(self, mock_stdout):
        
        self.manager.print_to_console("rooms", filters="ls ml")
        output_str = mock_stdout.getvalue()
        self.assertIn("SAPELE (LIVING)", output_str)



class FaciltyManagerSaveTest(unittest.TestCase):

    def setUp(self):

        self.manager =  FacilityManager()
        self.manager.teamdir = [
            Fellow("JANE DOE", "Y", gender="F"),
            Fellow("JOHN DOE", "Y", gender="M"),
            Fellow("JEN DOE", "N", gender="F"),
            Fellow("JIM DOE", "Y", gender="M"),
            Fellow("JOE DOE", "N", gender="M"),
            Staff("OSADEBE"),
            Staff("AWILO UZO"),
        ]
        self.manager.roomsdir = [
            OfficeSpace("CARAT"),
            OfficeSpace("CRUCIBLE"),
            OfficeSpace("ANVIL"),
            OfficeSpace("FORGE"),
            LivingSpace("OBECHE"),
            LivingSpace("SAPELE"),
            LivingSpace("BALSAM"),
        ]
        self.manager.allocate()
        self.mock_file_obj = MagicMock()

    @patch.object(builtins, 'open')
    def test_saves_team_output_correctly(self, mock_open):

        mock_open.return_value = self.mock_file_obj
        self.manager.save_to_file("team", filters="fw fm w+", filepath="./data/input_persons_ext.txt", mode=settings.OVERWRITE)
        self.assertTrue(self.mock_file_obj.write.called)


    @patch.object(builtins, 'open')
    def test_saves_rooms_output_correctly(self, mock_open):

        mock_open.return_value = self.mock_file_obj
        self.manager.save_to_file("rooms", filters="os st oc-", filepath="./data/input_persons_ext.txt", mode=settings.OVERWRITE)
        self.assertTrue(self.mock_file_obj.write.called)