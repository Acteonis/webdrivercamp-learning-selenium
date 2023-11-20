from components.base import Base

class LeftFilter(Base):
    LOCATOR = "//*"  # Class constant variable

    def __init__(self, driver):
        super().__init__(driver)

    def select_option(self, option, visible=False):
        print(Base.BASE_VAR)  # Access the BASE_VAR from the parent class
        print(self.LOCATOR)  # Access the LOCATOR from the current class
        print(option)
        print(visible)