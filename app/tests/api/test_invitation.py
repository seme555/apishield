import pytest
from unittest import mock

from app.tests.utils.dummy import invitation_data


def test_invite_sends_email_successfully(client, mocker):
    """ When the invite API endpoint is called -
        Ensure that an invitation is created successfully
        Ensure that an invitation email is sent successfully with the correct data
    """

    # Mocking a token generation function
    _ = mocker.patch(
        'app.api.invitation.generate_invitation_token',
        return_value="unique_token_123"
    )

