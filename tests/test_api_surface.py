import importlib.util, pathlib, unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
MAIN_PATH = ROOT / "src" / "yapin" / "main.py"
EXPECTED = ("Bot", "Cog", "command", "listener", "button", "YapinError", "row", "btn", "link_button")


class ApiSurfaceTests(unittest.TestCase):
    def test_main_module_exposes_expected_symbols(self):
        spec = importlib.util.spec_from_file_location("yapin_main", MAIN_PATH)
        module = importlib.util.module_from_spec(spec)
        assert spec.loader is not None
        spec.loader.exec_module(module)

        for name in EXPECTED:
            self.assertTrue(hasattr(module, name), name)

    def test_package_exports_expected_symbols(self):
        import yapin

        for name in EXPECTED:
            self.assertTrue(hasattr(yapin, name), name)


if __name__ == "__main__":
    unittest.main()
