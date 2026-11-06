"""Модели предметной области."""


class User:
    """Пользователь приложения."""

    def __init__(self, username: str, email: str) -> None:
        self.username = username
        self.email = email

    def info(self) -> str:
        return f"{self.username} <{self.email}>"


class Currency:
    """Валюта из справочника ЦБ РФ."""

    def __init__(self, code: str, name: str) -> None:
        # TODO: сохраните code и name в атрибуты экземпляра
        self.code = code
        self.name = name

    def info(self) -> str:
        # TODO: верните строку вида "USD — Доллар США"
        return f"{self.code} — {self.name}"
