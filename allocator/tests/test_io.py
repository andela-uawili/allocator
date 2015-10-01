import unittest
from mock import patch, MagicMock
import __builtin__ as builtins
import os.path

from ..app import settings
from ..app import io
from ..app.persons import Person, Staff, Fellow
from ..app.spaces import Room, OfficeSpace, LivingSpace


class CommandArgsParsingTest(unittest.TestCase):

    def test_load_command_parses_correctly(self):
        cmd_args = io.parse_cmd_args("rooms './data/input.txt' :a", io.load_cmd_pattern)
        self.assertNotEqual(cmd_args, None)
        self.assertEqual(cmd_args.get('target'), 'rooms')
        self.assertEqual(cmd_args.get('filepath'), './data/input.txt')
        self.assertEqual(cmd_args.get('mode'), 'a')

    def test_load_command_parses_correctly_without_args(self):
        cmd_args = io.parse_cmd_args("", io.load_cmd_pattern)
        self.assertNotEqual(cmd_args, None)
        self.assertEqual(cmd_args.get('target'), None)
        self.assertEqual(cmd_args.get('filepath'), None)
        self.assertEqual(cmd_args.get('mode'), None)

    def test_input_command_parses_correctly(self):
        cmd_args = io.parse_cmd_args("team 'AWILI UZO  FELLOW Y M, TOSIN ADE  STAFF' :o", io.input_cmd_pattern)
        self.assertNotEqual(cmd_args, None)
        self.assertEqual(cmd_args.get('target'), 'team')
        self.assertEqual(cmd_args.get('cslist'), 'AWILI UZO  FELLOW Y M, TOSIN ADE  STAFF')
        self.assertEqual(cmd_args.get('mode'), 'o')

    def test_allocate_command_parses_correctly_without_args(self):
        cmd_args = io.parse_cmd_args("", io.allocate_cmd_pattern)
        self.assertNotEqual(cmd_args, None)
        self.assertEqual(cmd_args.get('gender_constraint'), None)
        self.assertEqual(cmd_args.get('role_constraint'), None)

    def test_allocate_command_parses_correctly(self):
        cmd_args = io.parse_cmd_args("r- g+", io.allocate_cmd_pattern)
        self.assertNotEqual(cmd_args, None)
        self.assertEqual(cmd_args.get('gender_constraint'), 'g+')
        self.assertEqual(cmd_args.get('role_constraint'), 'r-')

    def test_print_command_parses_correctly(self):
        cmd_args = io.parse_cmd_args("rooms os fw cf-", io.output_cmd_pattern)
        self.assertNotEqual(cmd_args, None)
        self.assertEqual(cmd_args.get('target'), 'rooms')
        self.assertEqual(cmd_args.get('filters'), 'os fw cf-')

    def test_save_command_parses_correctly(self):
        cmd_args = io.parse_cmd_args("team fw fm   w+ l- './data/output.txt' :o", io.output_cmd_pattern)
        self.assertNotEqual(cmd_args, None)
        self.assertEqual(cmd_args.get('target'), 'team')
        self.assertEqual(cmd_args.get('filters'), 'fw fm   w+ l-')
        self.assertEqual(cmd_args.get('filepath'), './data/output.txt')
        self.assertEqual(cmd_args.get('mode'), 'o')



class ParsePersonInputTest(unittest.TestCase):

    def setUp(self):
        self.input_batch = [
            "ANDREW PHILLIPS         FELLOW      Y       ",
            "       MATTHEW O'CONNOR        STAFF",
            "JOHN ADEWALE            FELLOW      N       M   ",
            "   IYANU ALIMI             FELLOW      Y       F ",
            " AHMED AKUBE             STAFF",
        ]

    def test_person_input_processes_correctly(self):
        person_list = io.process_person_input_batch(self.input_batch)
        self.assertNotIn(None, person_list)
        self.assertEqual(person_list[2].name, 'JOHN ADEWALE')
        self.assertEqual(person_list[2].role, 'FELLOW')
        self.assertEqual(person_list[2].wants_living, 'N')
        self.assertEqual(person_list[2].gender, 'M')



class ParseRoomInputTest(unittest.TestCase):

    def setUp(self):
        self.input_batch = [
            "   CARAT           OFFICE        FELLOW   ",
            "TONGS           OFFICE        FELLOW",
            "   FURNACE         OFFICE        STAFF",
            "   HAMMER          OFFICE        STAFF",
            "SAPELE          LIVING             F",
            "   MAPLE           LIVING      F",
            "CEDAR           LIVING       M",
            "   MAHOGHANY       LIVING                    M    ",
        ]

    def test_person_input_processes_correctly(self):
        room_list = io.process_room_input_batch(self.input_batch)
        self.assertNotIn(None, room_list)
        self.assertEqual(room_list[2].name, 'FURNACE')
        self.assertEqual(room_list[5].purpose, 'LIVING')
        self.assertEqual(room_list[0].occupant_role, 'FELLOW')
        self.assertEqual(room_list[4].occupant_role, None)
        self.assertEqual(room_list[7].occupant_gender, 'M')
        self.assertEqual(room_list[1].occupant_gender, None)



class FormatRoomOutputTest(unittest.TestCase):

    def setUp(self):

        room_1 = LivingSpace('CARAT')
        room_2 = OfficeSpace("CRUCIBLE")

        occupants_1 = [
            Fellow("JANE DOE", "Y"),
            Fellow("JOHN DOE", "N"),
            Fellow("JEN DOE", "Y"),
        ]
        occupants_2 = [
            Staff("LAGBAJA"),
            Staff("OSADEBE"),
            Staff("AWILO UZO"),
        ]

        for occupant in occupants_1:
            room_1.add_occupant(occupant)

        for occupant in occupants_2:
            room_2.add_occupant(occupant)

        self.output_batch = [room_1, room_2]


    def test_room_output_formats_correctly(self):
        output_str = io.format_room_output_batch(self.output_batch, "Test Output")
        self.assertIn("Test Output", output_str)
        self.assertIn("CRUCIBLE (OFFICE)", output_str)
        self.assertIn("CARAT (LIVING)", output_str)
        self.assertIn("LAGBAJA", output_str)
        self.assertIn("JANE DOE", output_str)
    


class FormatPersonOutputTest(unittest.TestCase):
    
    def setUp(self):
        self.output_batch = [
            Staff("NNADI NADAYAR"),
            Staff("ENEGESI CHIDI"),
            Fellow("SULE OLUWA-FEMI", 'N', 'M'),
            Fellow("TOM 'N' JERRY", 'Y'),
        ]

    def test_person_output_formats_correctly(self):
        output_str = io.format_person_output_batch(self.output_batch, "Test Output")
        self.assertIn("Test Output", output_str)
        self.assertIn("NNADI NADAYAR (STAFF)", output_str)
        self.assertIn("TOM 'N' JERRY (FELLOW)", output_str)



class ReadFileInputTest(unittest.TestCase):

    def setUp(self):
        self.mock_file_object = MagicMock()
        self.mock_file_object.readlines = MagicMock(return_value=["   ","NNADI NADAYAR STAFF", "TOM 'N' JERRY FELLOW"])
        # self.mock_file_object.close = MagicMock()
        
    @patch.object(builtins, 'open')
    def test_target_file_is_opened_correctly(self, mock_open):
        
        mock_open.return_value = self.mock_file_object
        lines = io.read_input_lines_from_file("./data/input_persons.txt")
        mock_open.assert_called_with(os.path.abspath("./data/input_persons.txt"), 'r')


    @patch.object(builtins, 'open')
    def test_file_input_is_read_correctly(self, mock_open):
        
        mock_open.return_value = self.mock_file_object
        lines = io.read_input_lines_from_file("./data/input_persons.txt")
        self.mock_file_object.readlines.assert_any_call()
        self.assertEqual(len(lines), 2)



class WriteFileOutputTest(unittest.TestCase):

    def setUp(self):
        self.mock_file_object = MagicMock()
        self.mock_file_object.write = MagicMock()

    @patch.object(builtins, 'open')
    def test_target_file_is_opened_correctly(self, mock_open):
        
        mock_open.return_value = self.mock_file_object
        io.write_output_to_file("Test Output", "./data/output.txt", True)
        mock_open.assert_called_with(os.path.abspath("./data/output.txt"), 'a')


    @patch.object(builtins, 'open')
    def test_file_output_is_written_to_correctly(self, mock_open):
        
        mock_open.return_value = self.mock_file_object
        io.write_output_to_file("Test Output", "./data/output.txt", True)
        self.mock_file_object.write.assert_called_with("Test Output")
