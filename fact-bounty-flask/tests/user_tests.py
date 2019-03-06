# -*- coding: utf-8 -*-
"""Functional tests using WebTest.
"""
from flask import url_for

from ..api.models.user import User


class TestLoggingIn:
    """Login."""

    def test_can_log_in_returns_200(self, testapp):
        """Login successful."""
        response = testapp.post('/spi/users/login',data=dict(username='username',password='password'), follow_redirects=True)
        assert response.status_code == '200'