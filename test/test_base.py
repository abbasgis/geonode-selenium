#!/usr/bin/env python3

from seleniumbase import BaseCase
import os

BASE = "http://127.0.0.1/"
GEOTIFF = os.path.abspath("data/UTM2GTIF.TIF")
USER = "super"
PASS = "duper"

class LayerUploadCheck(BaseCase):
    def click_button(self, label):
        selector = "//button[contains(., '%s')]" % label
        self.driver.find_element_by_xpath(selector).click()

    def superuser(func):
        def wrapper(self, *args, **kwargs):
            self.open(BASE+"/account/login/?next=/")
            self.update_text("#id_login", USER)
            self.update_text("#id_password", PASS)
            self.click_button("Sign In")
            func(self, *args, **kwargs)
            self.open(BASE+"/account/logout/?next=/")
            self.click_button("Log out")
        return wrapper

    @superuser
    def test_login(self):
        pass

    @superuser
    def test_upload(self):
        self.click_link("Layers")
        self.click_link("Upload Layers")
        self.execute_script("jQuery('#file-input').show()")
        self.update_text('#file-input', GEOTIFF)
        self.click_link("Upload files")
        self.click_link("Layer Info", timeout=60)