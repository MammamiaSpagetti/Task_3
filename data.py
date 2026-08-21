from uuid import uuid4


REQUEST_TIMEOUT = 20
UI_TIMEOUT = 25


def generate_user_data():
    unique_id = uuid4().hex
    return {
        'email': f'stellar_ui_{unique_id}@example.com',
        'password': f'Password_{unique_id}',
        'name': f'User_{unique_id[:8]}',
    }


def generate_email():
    return f'recovery_{uuid4().hex}@example.com'
