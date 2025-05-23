from enum import Enum


class AccessLevel(Enum):
    """
    PUBLIC - комната ожидания выключена, все пользователи смогут сразу присоединиться к встрече;

    ORGANIZATION — комната ожидания включена для внешних пользователей, к встрече сразу смогут присоединиться только пользователи с аккаунтами на домене организации;

    UNKNOWN — параметр для обеспечения обратной совместимости: все остальные значения поля обрабатываются как UNKNOWN.
    """
    PUBLIC = 'PUBLIC'
    ORGANIZATION = 'ORGANIZATION'
    UNKNOWN = 'UNKNOWN'
