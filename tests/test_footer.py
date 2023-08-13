from pages.footer import Footer


def test_open_twitter(driver, logged_in):
    twitter = Footer(driver)
    result = twitter.is_twitter_open()

    assert result in "https://twitter.com/saucelabs"


def test_open_facebook(driver, logged_in):
    facebook = Footer(driver)
    result = facebook.is_facebook_open()

    assert result in "https://www.facebook.com/saucelabs"


def test_open_linkedin(driver, logged_in):
    linkedin = Footer(driver)
    result = linkedin.is_linkedin_open()

    assert result in "https://www.linkedin.com/company/sauce-labs/"
