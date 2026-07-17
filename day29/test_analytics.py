def test_dataframe_rows(sample_df):
    assert len(sample_df) == 5
def test_dataframe_columns(sample_df):
    assert "Score" in sample_df.columns
def test_intentional_failure(sample_df):
    assert len(sample_df) >= 6
