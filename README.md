# ECU Control Panel

## 📌 Project Overview

ECU Control Panel is a Qt/C++ based application for monitoring and processing ECU data.

The system receives raw ECU data, parses it according to parameter definitions, processes the resulting parameter values, and presents the data through a Qt/QML interface.

The project also includes a data cleaning layer to improve the reliability and quality of parsed ECU data before it is displayed.

## 🏗️ System Architecture

```text
                         ECU Data
                            │
                            ▼
                     RawDataReader
                            │
                            ▼
                     RawDataParser
                            ▲
                            │
                    Parameter Definitions
                            │
                     ┌──────┴──────┐
                     │ ExcelParser  │
                     └──────┬──────┘
                            │
                      ECU_Data.xlsx

                     Parsed Parameter Data
                            │
                            ▼
                       DataCleaner
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
       Missing          Duplicate          Infinite
          │                                   │
          └─────────────────┬─────────────────┘
                            │
                         Outlier
                            │
                            ▼
                       Cleaned Data
                            │
                            ▼
                        Qt / QML
                            │
                            ▼
                      Charts / UI
```

## 🔄 Data Processing Flow

1. `RawDataReader` receives or reads raw ECU data.
2. `ExcelParser` reads parameter definitions from the ECU configuration Excel file.
3. `RawDataParser` uses these definitions to convert raw ECU data into meaningful parameter values.
4. Parsed parameter values are passed to `DataCleaner`.
5. `DataCleaner` checks and processes data quality issues.
6. Cleaned values are passed to the Qt/QML interface.
7. Processed data can be displayed using parameter cards, tables, and charts.

## 📊 Data Cleaning

The cleaning layer is based on the data quality and outlier analysis work developed in the GenericEDA project.

### Missing Values

- Detect missing values.
- Reduce unnecessary row deletion.
- Remove completely empty columns.
- Fill numeric missing values using statistical methods.
- Fill categorical missing values using mode.

### Duplicate Records

Duplicate records can be detected and removed to prevent repeated measurements from affecting analysis.

### Infinite Values

Infinite and other non-finite numeric values are detected and handled before further analysis.

### Outlier Detection

Two methods are supported:

- **IQR**
- **Z-Score**

For IQR analysis, the standard multiplier is initially `1.5`.

The system can first show the detected outlier count and percentage, allowing the user to choose an appropriate IQR multiplier before the final analysis.

### Outlier Handling

Detected outliers can be handled using:

- Remove Outliers
- Replace with Mean
- Replace with Median
- Winsorization

## 📈 Visualization

Processed ECU parameters can be visualized through the Qt/QML interface.

Possible visualizations include:

- Live parameter values
- Parameter history
- Line charts
- Selected signal trends
- Data quality information
- Outlier/anomaly indicators

## 🧩 Main Components

### ExcelParser

Reads parameter definitions from the ECU Excel configuration.

These definitions can include:

- Parameter name
- RAM/address information
- Data type
- Data width
- Conversion information

### RawDataReader

Responsible for receiving or reading raw ECU data.

### RawDataParser

Converts raw ECU data into meaningful parameter values using the definitions provided by `ExcelParser`.

### DataCleaner

Processes parsed parameter data and handles data quality problems such as:

- Missing values
- Duplicate records
- Infinite values
- Outliers

### Qt/QML Interface

Displays processed ECU data and provides the visualization layer.

## 🛠️ Technologies

- C++
- Qt 6
- Qt Quick / QML
- Qt Widgets
- Excel-based parameter definitions
- Data processing and statistical analysis

## 📁 Project Structure

```text
ECUControlPanel/
│
├── backend/
│   ├── parser/
│   │   ├── ExcelParser.h
│   │   ├── ExcelParser.cpp
│   │   ├── RawDataParser.h
│   │   └── RawDataParser.cpp
│   │
│   ├── cleaner/
│   │   ├── DataCleaner.h
│   │   └── DataCleaner.cpp
│   │
│   ├── collector/
│   ├── dispatcher/
│   ├── manager/
│   └── simulator/
│
├── qml/
├── data/
└── README.md
```

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

## 🎯 Current Development Goal

The current development focus is integrating data cleaning functionality into the existing ECU data processing pipeline.

The target flow is:

```text
Raw ECU Data
     ↓
RawDataReader
     ↓
RawDataParser
     ↓
Parsed Parameter Data
     ↓
DataCleaner
     ↓
Cleaned Data
     ↓
Qt/QML
```

This integration aims to make the ECU Control Panel more robust by ensuring that parsed data is checked and cleaned before being presented to the user.

## 👥 Developers

Aybüke & Esra
