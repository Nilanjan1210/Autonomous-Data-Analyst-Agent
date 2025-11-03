import pandas as pd
import tempfile
import csv

def preprocess_and_save(file_path): 
    """
    Load and preprocess a CSV/XLSX file.
    Returns: DataFrame, columns list, HTML table, and error message (if any).
    """
    try:
        global df
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path, encoding='utf-8', na_values=['NA', 'N/A', 'missing'])
        elif file_path.endswith('.xlsx'):
            df = pd.read_excel(file_path, na_values=['NA', 'N/A', 'missing'])
        else:
            return None, None, None, "Unsupported file format."

        # Clean text columns
        for col in df.select_dtypes(include=['object']):
            df[col] = df[col].astype(str).replace({r'"': '""'}, regex=True)

        # Convert dates and numerics
        for col in df.columns:
            if 'date' in col.lower():
                df[col] = pd.to_datetime(df[col], errors='coerce')
            elif df[col].dtype == 'object':
                try:
                    df[col] = pd.to_numeric(df[col])
                except:
                    pass

        # Save cleaned version
        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv", mode='w', newline='', encoding='utf-8') as temp_file:
            df.to_csv(temp_file.name, index=False, quoting=csv.QUOTE_ALL)
            return df, df.columns.tolist(), df.to_html(classes='table-auto w-full'), None

    except Exception as e:
        return None, None, None, str(e)
