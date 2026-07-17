import pytest
import pandas as pd

@pytest.fixture
def sample_df():
    """Provides a Sample DataFrame For Testing"""
    data = {
        "Username" : ["Sam", "Roy", "Michael", "Angilena", "Samantha"],
        "Score"    : [68   , 57   , 76       , 38        , 82        ],
        "Active"   : [True , False, True     , True      , False     ]
    }
    return pd.DataFrame(data)
