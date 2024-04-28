from string_utils import StringUtils
import pytest

string_ut = StringUtils()

@pytest.mark.positive_test
@pytest.mark.parametrize('string, result', [("hello", "Hello"), ("HELLO", "Hello")])
def test_capitilize_pos(string, result):
    string_ut = StringUtils()
    res = string_ut.capitilize(string)
    assert res == result


@pytest.mark.negative_test
@pytest.mark.parametrize('string, result', [("Word", "word"), ("HELLO", "HELLO")])
def test_capitilize_neg(string, result):
    string_ut = StringUtils()
    res = string_ut.capitilize(string)
    assert res != result


@pytest.mark.positive_test
def test_trim_pos():
    string_ut = StringUtils()
    res = string_ut.trim("    we are here")
    assert res == "we are here"


@pytest.mark.negative_test
def test_trim_neg():
    string_ut = StringUtils()
    res = string_ut.trim("    ")
    assert res != "    "


@pytest.mark.positive_test
def test_to_list_pos():
    string_ut = StringUtils()
    res = string_ut.to_list("one,two,three,four")
    assert res == ["one", "two", "three", "four"]


@pytest.mark.negative_test
def test_to_list_neg():
    string_ut = StringUtils()
    res = string_ut.to_list("one,two,three,four", None)
    assert res != ["one", "two", "three", "four"]


@pytest.mark.positive_test
def test_contains_pos():
    string_ut = StringUtils()
    res = string_ut.contains("Hello darkness my old friend", "1")
    assert not res


@pytest.mark.negative_test
def test_contains_neg():
    string_ut = StringUtils()
    with pytest.raises(AttributeError):
        string_ut.contains(None, None)


@pytest.mark.positive_test
def test_delete_symbol_pos():
    string_ut = StringUtils()
    res = string_ut.delete_symbol("Hello darkness my old friend", "darkness ")
    assert res == "Hello my old friend"


@pytest.mark.negative_test
def test_delete_symbol_neg():
    string_ut = StringUtils()
    res = string_ut.delete_symbol("", "")
    assert res == ""


@pytest.mark.positive_test
def test_starts_with_pos():
    string_ut = StringUtils()
    res = string_ut.starts_with("Word", "W")
    assert res


@pytest.mark.negative_test
def test_starts_with_neg():
    string_ut = StringUtils()
    with pytest.raises(AttributeError):
        string_ut.starts_with(None, None)


@pytest.mark.positive_test
def test_end_with_pos():
    string_ut = StringUtils()
    res = string_ut.end_with("Weird", "M")
    assert not res


@pytest.mark.negative_test
def test_end_with_neg():
    string_ut = StringUtils()
    with pytest.raises(AttributeError):
        string_ut.end_with(None, None)


@pytest.mark.positive_test
def test_is_empty_pos():
    string_ut = StringUtils()
    res = string_ut.is_empty("      ")
    assert res

@pytest.mark.negative_test
def test_is_empty_neg():
    string_ut = StringUtils()
    with pytest.raises(AttributeError):
        string_ut.is_empty(None)



@pytest.mark.positive_test
def test_list_to_string_pos():
    string_ut = StringUtils()
    res = string_ut.list_to_string(["we","are","the","champions"], "-")
    assert res == ("we-are-the-champions")


@pytest.mark.negative_test
def test_list_to_string_neg():
    string_ut = StringUtils()
    res = string_ut.list_to_string([""," ","  ","    "], "-")
    assert res == ("- -  -    ")
