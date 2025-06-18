from contextlib import asynccontextmanager
from datetime import datetime

from fastapi import FastAPI

from configuration.database import AsyncSessionLocal
from configuration.security.hashing import Hashing
from enums.role import RoleEnum
from model import Role, User
from repository.role import RoleRepository
from repository.user import UserRepository
from util.constant import Constant


@asynccontextmanager
async def lifespan(_: FastAPI):
    async with AsyncSessionLocal() as db:
        user_repo = UserRepository(db)
        role_repo = RoleRepository(db)

        roles_list = await role_repo.find_all()
        if not roles_list:
            admin_role = Role(name=RoleEnum.ADMIN.value)
            teacher_role = Role(name=RoleEnum.TEACHER.value)
            student_role = Role(name=RoleEnum.STUDENT.value)

            await role_repo.save_all([admin_role, teacher_role, student_role])

            admin = User(
                first_name=Constant.ADMIN_FIRST_NAME,
                last_name=Constant.ADMIN_LAST_NAME,
                email=Constant.ADMIN_EMAIL,
                phone=Constant.ADMIN_PHONE,
                dob=datetime.strptime(Constant.ADMIN_DOB, "%d/%m/%Y").date(),
                username=Constant.ADMIN_USERNAME,
                password=Hashing.hash_password(Constant.ADMIN_PASSWORD),
            )

            admin.roles = [admin_role, teacher_role]
            await user_repo.save(admin)
    yield
