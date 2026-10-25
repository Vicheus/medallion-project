![Python](https://img.shields.io/badge/any_text-3.11-blue?style=flat&label=Python%20versions)
![PySpark](https://img.shields.io/badge/any_text-3.5.3-blue?style=flat&label=PySpark)

# Parsetron
Parstron is a mini-application designed to transform raw data into the required format. 
I understand that this concept might not be entirely clear when explained in words. 
To provide a clearer understanding, the complete data processing cycle, along with examples, 
is illustrated in the graph below.

## Project architecture
The Parsetron project is structured to enable the seamless addition of new sections (field categories) while maintaining a clean and organized architecture. Each section resides within its own directory, containing essential components for functionality and validation.

### Creating a new section
To create a new section, several key files are required:

1. **UDFs (User-Defined Functions)**:  
   Defined in the `udfs.py` file, these functions are designed specifically for PySpark operations, ensuring efficient data processing and transformations for the section.

2. **Schema**:  
   The `schemas.py` file holds the schema definition, specifying the structure of all fields within the section. This ensures proper validation and consistency of the data.

3. **Validators**:  
   A list of validators for all fields in the section is contained in the `validators` directory. Each validator (e.g., `document.py`, `document_serial.py`) ensures that the data conforms to specific rules and requirements.

Additionally, each section can have its own custom settings defined in the `settings.py` file, allowing for further customization and flexibility as needed.

### Project structure
- **Global Settings**:  
  The global settings of the entire application are stored in the main `settings.py` file.

- **Utilities**:  
  Utility functions such as `ReadmeGenerator` and `JsonValidator` are located in the `utils` directory.

- **Main Module**:  
  The main entry point of the module is the `Parsetron.py` file.
```
parsetron
|-- sections                        # Contains all the sections of the application
|   |-- base
|   |-- document                    # Section (category of fields) name
|   |   |-- validators              # List of all section validators
|   |   |   |-- document.py
|   |   |   |-- document_serial.py
|   |   |-- schemas.py              # Schema of all fields in the section
|   |   |-- settings.py             # Specific section settings
|   |   |-- udfs.py                 # UDFs for pyspark
|   |-- ...
|-- utils                           # Utility functions (ReadmeGenerator, JsonValidator, etc)
|-- Parsetron.py                    # Main module file
|-- settings.py                     # Global settings of the application
```

## Supported formats
Below is a list of supported source file formats in Parsetron

| File format     | Support |
|-----------------|---------|
| <kbd>CSV</kbd>  | ✅       |
| <kbd>TXT</kbd>  | ✅       |
| <kbd>JSON</kbd> | ✅       |