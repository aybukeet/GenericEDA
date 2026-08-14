# GenericEDA

GenericEDA is a Python-based project developed to perform Exploratory Data Analysis (EDA), data quality checks, and data cleaning on datasets in different formats.

## 🚀 Project Features

- Reading CSV, Excel, and TXT files
- Displaying dataset row and column information
- Data type analysis
- Generating statistical summaries
- Missing value analysis
- Detecting and removing duplicate records
- Detecting infinite values
- Detecting constant and completely empty columns
- Outlier analysis using the IQR method
- Outlier analysis using the Z-Score method
- User-defined IQR multiplier
- Displaying outlier percentages
- Outlier cleaning: Remove Outliers, Mean, Median, Winsorize
- Data visualization
- Exporting the cleaned dataset

## 📊 EDA Workflow

Dataset → Loading → Summary → Quality Analysis → Missing Values → Outlier Analysis → Data Cleaning → Visualization → Export

## 📂 Supported File Formats

- `.csv`
- `.xlsx`
- `.xls`
- `.txt`

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- SciPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## 📁 Project Structure

```text
GenericEDA/
├── GenericEDA_updated.ipynb
├── README.md
├── utils/
│   ├── loader.py
│   ├── summary.py
│   ├── quality.py
│   ├── missing.py
│   ├── outlier.py
│   ├── cleaning.py
│   ├── visualization.py
│   └── export.py
├── data/
└── figures/
```

## 📈 Outlier Analysis

### IQR

The system first performs a preliminary analysis using the standard `1.5` IQR multiplier and displays the number and percentage of outliers for each column.

The user can review these results and determine an appropriate multiplier value.

- `1.5` → Standard / Balanced
- `2.0` → More Tolerant
- `2.5` → More Tolerant
- `3.0` → Very Tolerant

The final outlier report is generated using the selected multiplier.

### Z-Score

For the Z-Score method, the user can specify the threshold value.
The standard recommended threshold is `3`.

## 🧹 Data Cleaning

The goal is to improve data quality while minimizing data loss as much as possible.

### Missing Values

- Completely empty columns are removed.
- Rows containing a very high proportion of missing data are removed.
- Missing numeric values can be filled using the median.
- Missing categorical values can be filled using the mode.
- Mean, Median, and Mode methods are supported.

### Duplicate Records

Duplicate records are detected and can be removed during the cleaning process.

### Outliers

The following operations can be applied to outliers:

- Remove Outliers
- Replace with Mean
- Replace with Median
- Winsorize

## 📊 Visualization

Various plots are generated to help analyze and examine the dataset.
The generated plots are stored in the `figures/` directory.

## ▶️ Running the Project

After installing the required Python libraries, run:

```bash
jupyter notebook
```

or:

```bash
jupyter lab
```

Then open and run the `GenericEDA_updated.ipynb` file.

## 💾 Output

As a result of the analysis and cleaning processes, the following outputs can be generated:

- Dataset summary
- Data quality report
- Missing value report
- Outlier report
- Visualizations
- Cleaned dataset

Visualizations are stored in the `figures/` directory, while cleaned datasets can be saved through the export process.
