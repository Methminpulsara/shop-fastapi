from datetime import datetime
from typing import Dict, Optional, List

from models import UserResponse, UserCreate


class UserRepository:
    def __init__(self):
        self.__data: Dict[int, UserResponse] = {}
        self.__count: int = 0

    def create_user(self, user_data: UserCreate) -> UserResponse:
        user_id = self.__count
        new_user = UserResponse(
            id=user_id,
            name=user_data.name,
            email=user_data.email,
            age=user_data.age,
            role=user_data.role,
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat(),
        )
        self.__data[user_id] = new_user
        self.__count += 1
        return new_user


    def get_user_by_id(self, user_id: int) -> Optional[UserResponse]:
         if user_id in self.__data.keys():
           return self.__data[user_id]

         return None

    def get_user_by_name(self, user_name: str) -> Optional[UserResponse]:
        for user in self.__data.values():
            if user.name == user_name:
                return user
        return None

    def get_user_by_email(self, email: str) -> Optional[UserResponse]:
        for user in self.__data.values():
            if user.email == email:
                return user
        return None

    def get_all_users(self, limit:int, offset:int) -> List[UserResponse]:
        users =  list(self.__data.values())
        return users[offset: offset + limit]

    def replace_user(self, user_id:int, user_update) -> UserResponse:

        replaced_user = UserResponse(
            id=user_id,
            name=user_update.name,
            email=user_update.email,
            age=user_update.age,
            role=user_update.role,
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat(),
        )
        self.__data[user_id] = replaced_user
        return replaced_user

    def patch_user(self, user_id, user_patch):
        updated_data = user_patch.model_dump(exclude_unset=True)
        updated_user = self.user_repository.patch_user(user_id, updated_data)
        updated_user.updated_at = datetime.now().isoformat()
        return updated_user
