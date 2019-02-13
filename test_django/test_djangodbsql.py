import pytest

@pytest.mark.django_db
def test_djangodbsql():
    import debugsql
    debugsql.init_django()
    res = dbsql.g("SELECT 1 AS foo")
    assert res == "+-----+\n"\
                  "| foo |\n" \
                  "+-----+\n" \
                  "|  1  |\n" \
                  "+-----+"

