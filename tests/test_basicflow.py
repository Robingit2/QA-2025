from page_objects.basic_flow import BasicFlow

def test_basic_flow(driver):
    basic_flow = BasicFlow(driver)
    basic_flow.load()
    basic_flow.basic_flow()
