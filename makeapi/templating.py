import typing, pathlib
import aiofiles


class TemplateLoader:
    """
    Asynchrounously load template files using aiofiles.
    """

    def __init__(self, directory: typing.Union[pathlib.Path, str]) -> None:
        self.dir = directory

    async def load(self, name: str, **kwargs):
        async with aiofiles.open(f"{self.dir}/{name}", "r+") as f:
            real_content = """"""
            for name in kwargs:
                async for line in f:
                    real_content += line.replace(name, kwargs[name])
        return real_content
