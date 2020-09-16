from widget import Stage, Widget
import unittest

class TestWidget(unittest.TestCase):

    def setUp(self):
        self.widget = Widget()

    def test_widget_is_visible(self):
        self.assertTrue(self.widget.is_visible())

    def test_initial_stage_is_red(self):
        self.assertEqual(self.widget.stage, Stage.RED)

    def test_advance_from_red_to_green(self):
        self.widget.advance_stage()
        self.assertEqual(self.widget.stage, Stage.GREEN)

    def test_advance_from_green_to_refactor(self):
        self.widget.advance_stage()
        self.widget.advance_stage()
        self.assertEqual(self.widget.stage, Stage.REFACTOR)

    def test_advance_from_refactor_to_red(self):
        self.widget.advance_stage()
        self.widget.advance_stage()
        self.widget.advance_stage()
        self.assertEqual(self.widget.stage, Stage.RED)

if __name__ == "__main__":
    unittest.main()
