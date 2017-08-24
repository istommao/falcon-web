"""falcon models."""


class User(object):
    """User model."""

    ROLE_ROOT = '2'
    ROLE_ADMIN = '1'

    def __init__(self, _id, name, cnname, email, phone, im, qq, role):
        self._id = _id
        self.name = name
        self.cnname = cnname
        self.email = email
        self.phone = phone
        self.im = im
        self.qq = qq
        self.role = role

    def is_root(self):
        """IS root user."""
        return str(self.role) == self.ROLE_ROOT

    def is_admin(self):
        """Is admin user."""
        return str(self.role) == self.ROLE_ADMIN
