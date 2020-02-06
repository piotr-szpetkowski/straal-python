from straal.filters import Op, SimpleFilter, FilterInstance
import pytest


@pytest.fixture(scope="module")
def foo_filter():
    return SimpleFilter("foo")


@pytest.mark.parametrize("operation", [f for f in Op])
def test_simple_filter_supports_op(operation, foo_filter):
    op_method = f"__{operation.value}__"
    filter_instance = getattr(foo_filter, op_method)(123)

    assert isinstance(filter_instance, FilterInstance)
    assert filter_instance.name == foo_filter._name
    assert filter_instance._op == operation
    assert filter_instance._value == 123

    api_param = filter_instance.build_api_param()
    assert api_param == {f"{foo_filter._name}__{operation.value}": 123}
