from easy_choices.exceptions import (
    ChoicesIsEmpty,
    InvalidChoicesElements,
    MixedChoicesElements,
)


class Choices:
    def __init__(self, *choices_tuples):
        self._choices = []
        self.choices_tuples = choices_tuples
        self.values = []

        self.validate()

        for choices in self.choices_tuples:
            if len(choices) == 2:
                choices = choices[0], choices[0], choices[1]

            value, attribute_name, description = choices
            setattr(self, attribute_name, value)
            self._choices.append((value, description))
            self.values.append(value)

    def validate(self):
        if not self.choices_tuples:
            raise ChoicesIsEmpty("choices_tuples is empty")

        quantities_of_tuples = {len(choices) for choices in self.choices_tuples}
        is_valid_quantity_of_tuples = any(
            [2 in quantities_of_tuples, 3 in quantities_of_tuples]
        )

        if len(quantities_of_tuples) != 1:
            raise MixedChoicesElements("choices_tuples tuples has mixed items size")

        if not is_valid_quantity_of_tuples:
            raise InvalidChoicesElements("choices_tuples must have 2 or 3 items only")

    def to_django_choices(self):
        return tuple(self._choices)
