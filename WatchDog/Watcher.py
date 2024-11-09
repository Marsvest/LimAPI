import os
from asyncio import sleep as async_sleep
from typing import List


class Watcher:
    stored_files: List[int] = []

    @classmethod
    def make_hash(cls, array: list) -> str:
        return str(sum(array))

    @classmethod
    def update_files(cls) -> None:
        """Рекусивно получает все рабочие файлы и добавляет их размеры в массив"""
        cls.stored_files = []
        for root, _, files in os.walk(os.getcwd()):
            for file in files:
                filepath = os.path.join(root, file)
                file_size = os.path.getsize(filepath)
                cls.stored_files.append(file_size)

    @classmethod
    async def watch(cls) -> None:
        cls.update_files()
        old_hash: str = cls.make_hash(cls.stored_files)
        await async_sleep(0.5)
        cls.update_files()
        new_hash: str = cls.make_hash(cls.stored_files)

        if old_hash == new_hash:
            await cls.watch()
        else:
            print("server.reload")
            await cls.watch()
