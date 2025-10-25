from typing import Optional

from models import UserCreate, UserResponse
from repositories import UserRepository


class UserServiceException(Exception):
    pass


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, user_data: UserCreate) -> UserResponse:

        if self.user_repository.get_user_by_name(user_data.name) is not None:
            raise UserServiceException("User name already exist")

        if self.user_repository.get_user_by_email(user_data.email) is not None:
            raise UserServiceException("Email already exist")

        return self.user_repository.create_user(user_data)

    def get_user(self, id: int) -> Optional[UserResponse]:
        return self.user_repository.get_user_by_id(id)

    def get_all_users(self, limit: int = 10, offset: int = 0):
        return self.user_repository.get_all_users(limit, offset)

    def replace_user(self, user_id, user_update) -> UserResponse:

        if self.user_repository.get_user_by_id(user_id) is not None:
            raise UserServiceException("User Id do not exists")

        return self.user_repository.replace_user(user_id, user_update)

    def patch_user(self, user_id, user_patch) -> UserResponse:

        # Check if user exists
        existing_user = self.user_repository.get_user_by_id(user_id)
        if existing_user is None:
            raise UserServiceException("User does not exist")

        # Check if name already exists (ignore same user)
        if user_patch.name and self.user_repository.get_user_by_name(user_patch.name):
            raise UserServiceException("User name already exists")

        # Check if email already exists (ignore same user)
        if user_patch.email and self.user_repository.get_user_by_email(user_patch.email):
            raise UserServiceException("Email already exists")

        return self.user_repository.patch_user(user_patch)
