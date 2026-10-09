import unittest

from profile_utils import AppConfig, health_response, normalize_identifier


class ProfileUtilsTest(unittest.TestCase):
    def test_configuration_is_normalized(self) -> None:
        config = AppConfig.from_mapping(
            {"service_name": " profile-api ", "log_level": "debug"}
        )
        self.assertEqual(config, AppConfig("profile-api", "DEBUG"))

    def test_identifier_is_normalized(self) -> None:
        self.assertEqual(normalize_identifier(" Customer 42 "), "customer-42")

    def test_health_response_reports_readiness(self) -> None:
        self.assertEqual(
            health_response("profile-api", ready=True),
            {"service": "profile-api", "status": "ready"},
        )


if __name__ == "__main__":
    unittest.main()
