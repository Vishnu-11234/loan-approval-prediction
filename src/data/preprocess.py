
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer


def create_preprocessor(numerical_columns,categorical_columns):
    num_pipeline=Pipeline([
        ("imputer",SimpleImputer(strategy="mean"))
        
    ]

    )
    cat_pipeline=Pipeline(
        [
            ("imputer",SimpleImputer(strategy="most_frequent")),
            ("Encoder",OneHotEncoder(handle_unknown="ignore"))

        ]
    )
    preprocessor=ColumnTransformer(
        [
            ("num",num_pipeline,numerical_columns),
            ("cat",cat_pipeline,categorical_columns)
        ]
    )
    return preprocessor
