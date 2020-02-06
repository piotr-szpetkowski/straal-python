import pytest

from straal.filters import Filter, FilterInstance, Op, SimpleFilter


class EmptyOpsFilter(Filter):
    ops = []


@pytest.fixture(scope="module")
def foo_filter():
    return SimpleFilter("foo")


@pytest.fixture(scope="module")
def no_ops_filter():
    return EmptyOpsFilter("nope")


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


@pytest.mark.parametrize("operation", [f for f in Op])
def test_empty_ops_filter_supports_no_ops(operation, no_ops_filter):
    op_method = f"__{operation.value}__"
    with pytest.raises(NotImplementedError):
        getattr(no_ops_filter, op_method)(123)
