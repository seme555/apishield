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

    # Mocking the email sending function to prevent actual email dispatch
    mock_send_email = mocker.patch(
        'app.api.invitation.send_email_background',
        return_value=None
    )

    # Execute the api call
    response = client.post("api/invitation/invite", json=invitation_data)

    # Assertions
    assert response.status_code == 200
    assert response.json() == {'message': 'Invitation sent successfully'}

    # Verify the mock was called as expected
    mock_send_email.assert_called_once()
    mock_send_email.assert_called_with(
        background_tasks=mock.ANY,
        subject=f'Invitation to Join {invitation_data["organization"]}',
        email_to=invitation_data["email"],
        body={
            "full_name": invitation_data["full_name"],
            "email": invitation_data["email"],
            "organization": invitation_data["organization"],
            "created_by_name": "test user full name",
            "invitation_url": mock.ANY
        }
    )


@pytest.mark.parametrize("missing_field", [
    ("email"),
    ("organization"),
    ("organizational_role"),
    ("role")
])
def test_invite_missing_required_fields(client, missing_field):
