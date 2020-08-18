from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')


class InputeAllExceptAColumn(BaseEstimator, TransformerMixin):
    def __init__(self, simple_imputer):
        print('hey')
        self.simple_imputer = simple_imputer

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primero copiamos el dataframe de datos de entrada 'X'
        data = X.copy()

        profile_column = data['PROFILE']
        data.drop(['PROFILE'], axis=1, inplace=True)
        # Devolvemos un nuevo dataframe de datos sin las columnas no deseadas

        # Aplicamos el SimpleImputer ``si`` al conjunto de datos df_data_2 (resultado de la primera transformación)
        self.simple_imputer.fit(X=data)

        # Reconstrucción de un nuevo DataFrame de Pandas con el conjunto imputado (df_data_3)
        df_data_3 = pd.DataFrame.from_records(
            data=si.transform(
                X=data
            ),  # el resultado SimpleImputer.transform (<< pandas dataframe >>) es lista lista
            columns=data.columns  # las columnas originales deben conservarse en esta transformación
        )

        df_data_3['PROFILE'] = profile_column

        return df_data_3