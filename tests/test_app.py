import pytest
import app as app

session = {}


@pytest.fixture(autouse=True)
def setup(monkeypatch):
    """
    This is used to initialize the session and to mock the render_template function before each tests.
    Before each test, the session will be reinitialized with a new one.
    """
    session.clear()
    monkeypatch.setattr(app, 'get_session', mocked_get_session)
    monkeypatch.setattr(app, 'render_template', mocked_render_template)


def test_index_should_set_session_key_user():
    """
    This is a test example, please delete this test before starting the TP.
    This is a test example, please delete this test before starting the TP.
    This is a test example, please delete this test before starting the TP.
    This is a test example, please delete this test before starting the TP.
    """
    # Call app.index() to fill the session
    app.index()
    # Assert that the session is well filled
    assert app.get_session()['dino'] == 'TREX'


def test_should_have_an_empty_session():
    """
    This is a test example, please delete this test before starting the TP.
    This is a test example, please delete this test before starting the TP.
    This is a test example, please delete this test before starting the TP.
    This is a test example, please delete this test before starting the TP.
    """
    assert len(app.get_session()) == 0


def mocked_render_template(template_name, **kwargs):
    """
    Used to mock the method 'render_template'
    This returns the template name rendered
    """
    return template_name


def mocked_get_session():
    """
    Used to mock the method 'get_session'
    This returns a simple dict which is reinitiated every test
    """
    return session
