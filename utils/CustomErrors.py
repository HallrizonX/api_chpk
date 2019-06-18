from abc import ABCMeta, abstractmethod
from string import Template


class AbstractMixinBaseException(metaclass=ABCMeta):
    """
    @head_message: str - Message middleware for adding text before main message
    @last_message: str - Message middleware for adding text after main message
    @message: str - Main error message
    @status: int - Status for handler response in API
    @full_message: list - Full message with all messages
    """
    head_message: str
    last_message: str
    message: str
    status: int

    full_message: list = []

    @abstractmethod
    def get_message(self) -> str:
        """ Get ready string for show in error message"""

    @abstractmethod
    def set_full_message(self) -> None:
        """ Adding for main message all of middleware"""


class MixinBaseException(AbstractMixinBaseException, BaseException):

    def __init__(self, head_message: str = "", last_message: str = ""):
        super().__init__()
        self.head_message = str(head_message) if head_message != "" else None
        self.last_message = str(last_message) if last_message != "" else None
        self.set_full_message()

    def set_full_message(self, *args):
        self.full_message.append(self.head_message) if self.head_message != None else ""
        self.full_message.append(self.message) if self.message != None else ""
        self.full_message.append(self.last_message) if self.last_message != None else ""

    @property
    def get_message(self) -> str:
        return ". ".join(Template(
            self.full_message
        ).template)

    def __str__(self) -> str:
        return self.get_message


class AccessError(MixinBaseException):
    message = "Trouble with access. Maybe user haven't unique token"
    status = 403
