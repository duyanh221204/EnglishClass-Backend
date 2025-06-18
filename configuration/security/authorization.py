from typing import Annotated

from fastapi import Depends, HTTPException
from starlette import status

from configuration.security.authentication import AuthenticationConfig
from dto.response.authentication import TokenDataResponse
from repository.user import UserRepository, get_user_repo


class HasRole:
    def __init__(self, role_name: str):
        self.role_name = role_name
        
    async def __call__(
            self,
            user: Annotated[TokenDataResponse, Depends(AuthenticationConfig.get_current_user)],
            user_repo: Annotated[UserRepository, Depends(get_user_repo)]
    ) -> None | HTTPException:
        user_db = await user_repo.find_by_id(user.id)
        user_roles = [role.name for role in user_db.roles]

        if self.role_name not in user_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission"
            )

        return None
