class User:
    def __init__(self, name: str, u_id: str, level: int):
        self.name = name
        self.id = u_id
        self.level = level

    def __eq__(self, other):
        if isinstance(other, User):
            if self.name == other.name and self.id == other.id and self.level == other.level:
                return True
            else:
                return False

    def __str__(self):
        return f'{self.name} ({self.d}): Уровень доступа {self.level}'

    def __repr__(self):
        return f'{self.name} ({self.id}): Уровень доступа {self.level}'
