import typer

from portion.base import HandlerBase
from portion.commands import TemplateCommand


class TemplateHandler(HandlerBase):
    def __init__(self, app: typer.Typer) -> None:
        super().__init__(app, "template")

    def register_commands(self) -> None:
        template_command = TemplateCommand()

        @self.command.command(name="download")
        def download(link: str) -> None:
            template_command.download(link)

        @self.command.command(name="delete")
        def delete(template_name: str) -> None:
            template_command.delete(template_name)

        @self.command.command(name="list")
        def list() -> None:
            template_command.list()
