from app import Stage, App
import PyQt5
from ui import UI
import unittest
from unittest import mock

class TestApp(unittest.TestCase):

    def setUp(self):
        self.ui_class_patcher = mock.patch("app.UI", autospec=True)
        self.ui_class_patcher.start()
        self.app = App()

    def tearDown(self):
        self.ui_class_patcher.stop()

    def test_initial_stage_is_red(self):
        self.assertEqual(self.app.stage, Stage.RED)

    def test_advance_from_red_to_green(self):
        self.app.advance_stage()
        self.assertEqual(self.app.stage, Stage.GREEN)

    def test_advance_from_green_to_refactor(self):
        self.app.advance_stage()
        self.app.advance_stage()
        self.assertEqual(self.app.stage, Stage.REFACTOR)

    def test_advance_from_refactor_to_red(self):
        self.app.advance_stage()
        self.app.advance_stage()
        self.app.advance_stage()
        self.assertEqual(self.app.stage, Stage.RED)

    def test_app_has_ui(self):
        self.assertIsInstance(self.app.ui, UI)

    def test_run_ui(self):
        self.app.run()
        self.app.ui.run.assert_called_once();

class TestUI(unittest.TestCase):

    def setUp(self):
        self.qapplication_patcher = mock.patch(
            "ui.QApplication", autospec=True)
        self.qapplication_patcher.start()
        self.uic_patcher = mock.patch("ui.uic", autospec=True)
        self.uic_mock = self.uic_patcher.start()
        self.uic_mock.loadUi.return_value = mock.create_autospec(
            PyQt5.QtWidgets.QMainWindow)
        self.ui = UI()

    def tearDown(self):
        self.uic_patcher.stop()
        self.qapplication_patcher.stop()

    def test_has_qapplication(self):
        self.assertIsInstance(self.ui.app, PyQt5.QtWidgets.QApplication)

    def test_has_window(self):
        self.assertIsInstance(self.ui.window, PyQt5.QtWidgets.QMainWindow)

    def test_run_app_exec(self):
        self.ui.run()
        self.ui.app.exec_.assert_called_once()

    def test_create_tool_window(self):
        self.ui.window.setWindowFlag.assert_called_with(
            PyQt5.QtCore.Qt.Tool)
        self.ui.window.setAttribute.assert_called_with(
            PyQt5.QtCore.Qt.WA_QuitOnClose)

if __name__ == "__main__":
    unittest.main()
