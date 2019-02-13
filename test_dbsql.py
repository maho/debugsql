import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



@pytest.yield_fixture
def sess():
    engine = create_engine("sqlite:///:memory", echo=True)
    sess = sessionmaker(bind=engine)()
    yield sess
    sess.close()



def test_dbsql(sess):
    import debugsql
    debugsql.init(sess)
    res = dbsql.g("SELECT 1 AS foo")
    assert res == "+-----+\n"\
                  "| foo |\n" \
                  "+-----+\n" \
                  "|  1  |\n" \
                  "+-----+"

