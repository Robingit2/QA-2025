from page_objects.contact_page import ContactPage

def test_contact_empty_validation(driver):
    cp = ContactPage(driver)
    cp.load()
    cp.submit_form("", "", "")
    errors = cp.get_errors()
    assert "Name" in errors[0] and "Email" in errors[1]

def test_contact_valid_submission(driver):
    cp = ContactPage(driver)
    cp.load()
    cp.submit_form("Test User", "test@example.com", "Hello from pytest!")
    assert "Thank you" in cp.get_success()
