from sportsagent.data import create_pandas_dataframe


def test_create_pandas_dataframe():
    df = create_pandas_dataframe()
    assert df.shape == (3, 2)
    assert df["a"].sum() == 6
    assert df["b"].sum() == 15