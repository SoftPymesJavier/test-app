# coding=utf-8
#########################################################
from app.models import Example


class ExampleController:

    @staticmethod
    def get_example():
        return 'Hello from Flask'
