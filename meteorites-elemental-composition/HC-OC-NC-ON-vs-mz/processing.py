import pandas as pd


def process_data(csv_file_path):
    data = []
    max_extra_columns = 0
    fixed_columns = ["Average Noise", "Exp. m/z", "Recal m/z", "Theor. Mass", "Error",
                     "Rel. Abundance", "Signal2Noise", "DBE", "H/C", "O/C", "Molecular Formula"]

    with open(csv_file_path, 'r') as file:
        for _ in range(2):
            next(file)

        for line in file:
            row = line.strip().split(',')
            fixed_part = row[:len(fixed_columns)]
            extra_part = row[len(fixed_columns):]
            max_extra_columns = max(max_extra_columns, len(extra_part))
            data.append(fixed_part + extra_part)

    extra_columns = [f'Extra Col {i+1}' for i in range(max_extra_columns)]
    all_columns = fixed_columns + extra_columns

    df = pd.DataFrame(data, columns=all_columns)

    return df


def preprocess_data(csv_file_path):
    df = process_data(csv_file_path)
    start_idx = df.columns.get_loc("Molecular Formula")
    cols_to_merge = df.columns[start_idx:]
    df['Molecular Formula'] = df[cols_to_merge].apply(
        lambda x: ' '.join(x.dropna().astype(str)), axis=1)
    df = df.drop(columns=cols_to_merge.difference(['Molecular Formula']))
    df = df.dropna()

    return df


def extract_element_count(formula, element):
    elements = formula.split()
    count = 0
    for i in range(0, len(elements), 2):
        if elements[i] == element:
            count = int(elements[i+1])
            break
    return count


def further_ratios(df):
    df['N/C'] = df['Molecular Formula'].apply(lambda x: extract_element_count(
        x, 'N') / extract_element_count(x, 'C') if extract_element_count(x, 'C') != 0 else 0)
    df['O/N'] = df['Molecular Formula'].apply(lambda x: extract_element_count(
        x, 'O') / extract_element_count(x, 'N') if extract_element_count(x, 'N') != 0 else 0)

    return df
