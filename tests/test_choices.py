import pytest
from easy_choices import Choices
from easy_choices.exceptions import (
    ChoicesIsEmpty,
    InvalidChoicesElements,
    MixedChoicesElements,
)


def test_choices_empty():
    with pytest.raises(ChoicesIsEmpty) as exc:
        Choices()

    assert "choices_tuples is empty" == str(exc.value)


@pytest.mark.parametrize(
    "some_tuple_with_choices",
    [
        ("order_amount",),
        ("value", "attribute_name", "Some description", "This is an error"),
    ],
)
def test_choices_with_more_than_three_items(some_tuple_with_choices):
    with pytest.raises(InvalidChoicesElements) as exc:
        Choices(some_tuple_with_choices)

    assert f"choices_tuples must have 2 or 3 items only" == str(exc.value)


def test_choices_with_mixed_tuples_quantities():
    with pytest.raises(MixedChoicesElements) as exc:
        Choices(
            ("order_amount",),
            ("order_amount", "Order amount"),
            ("value", "attribute_name", "Some description"),
            ("value", "attribute_name", "Some description", "This is an error"),
        )

    assert f"choices_tuples tuples has mixed items size" == str(exc.value)


def test_choices_attributes_with_two_items_on_tuple():
    choices = Choices(
        ("order_amount", "Order amount"), ("attribute_name", "Some description")
    )

    assert choices.order_amount == "order_amount"
    assert choices.attribute_name == "attribute_name"


def test_choices_attributes_with_three_items_on_tuple():
    choices = Choices(
        ("order_amount", "order_amount", "Order amount"),
        ("value", "attribute_name", "Some description"),
        (0, "inactive", "Status inactive"),
        (True, "active", "Status active"),
    )

    assert choices.order_amount == "order_amount"
    assert choices.attribute_name == "value"
    assert choices.inactive == 0
    assert choices.active is True


def test_choices_to_django_choices_with_two_items_on_tuple():
    choices = Choices(
        ("order_amount", "Order amount"), ("attribute_name", "Some description")
    )

    django_choices = choices.to_django_choices()
    assert django_choices == (
        ("order_amount", "Order amount"),
        ("attribute_name", "Some description"),
    )


def test_choices_to_django_choices_with_three_items_on_tuple():
    choices = Choices(
        ("order_amount", "order_amount", "Order amount"),
        ("value", "attribute_name", "Some description"),
    )

    django_choices = choices.to_django_choices()
    assert django_choices == (
        ("order_amount", "Order amount"),
        ("value", "Some description"),
    )


@pytest.mark.parametrize(
    "choices, expected_list",
    [
        ([("value1", "Value1"), ("value2", "Value2")], ["value1", "value2"]),
        ([(0, "value1", "Value1"), (1, "value2", "Value2")], [0, 1]),
    ],
)
def test_choices_values_list(choices, expected_list):
    choices = Choices(*choices)
    assert choices.values == expected_list
