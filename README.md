# EDA_MARKETING
Project that demonstrates the skills using python to perform an exploratory analysis of a set of data and draw conclusions that add value to the business.


## Contents:
1. Aim of the project
2. Initial project documentation
3. Creation of the development environment for the version control centre.
4. Data processing
5. Data visualisation

## Aim of the project
The aim of this project is to draw decision-relevant conclusions about the results of a company's marketing campaigns. This requires the use of the knowledge acquired in the Python and Python data analysis block of the course. Specifically, the requirements are:
- Data transformation and data cleaning.
- Descriptive analysis of data.
- Data visualisation.
- Explanatory report of the analysis.
  
## Initial project documentation

To carry out the work we are presented with the following information:
- A word document called DataProject_Project_Project EDA with Python that has the context information of the project as well as statement and definition of the fields that are in the files.Also delivery instructions, tips and evaluation criteria.
- csv document ‘bank-additional’: this document contains the information about the records of the direct marketing campaigns.
- csv document ‘customer-details.xlsx’: this is an excel file with information about the bank's customers.

## Creation of the development environment for version control:

### Using the system console, the following actions are done:
- Creation of a folder called EDA_MAKETING on the desktop, cloned from the one already created in github.
- Add the folder venv that will store the different programs used in the environment and their version history.
- Activate the environment by calling Activate through the console
- A new available version of pip is installed
- Create the requiremens.txt document to document the version history
- Upload the environment to github:
(venv) C:\UsersmatisesDesktopAssembly>git add .

(venv) C:\UsersersmatismatisDesktopA_MARKETING> git commit -m ‘Creation of the folder system and environment’.
On branch main
Your branch is up to date with ‘origin/main’.

nothing to commit, working tree clean

(venv) C:\UsersersmatisktopEDA_MARKETING> git push
Everything up-to-date

(venv) C:\UsersersmatismatisDesktopAEMA_MARKETING> git push Everything up-to-date.

## Data processing

The analysis of the data provided needs to be transformed. In this way, information relevant to the objective of the project can be obtained. The following steps have been followed:

1. Preliminary data cleaning exercise
    The jupyter notebook eda_cleaning and the supporting document src sp_eda_cleaning are used to: import the data sources bank-additional and customer-details; initialise the columns with capital letters; convert the data to their int, float, specific format; delete columns with non-relevant data; change characters; merge the dataframes. 
2. Transformation of coordinates by geolocalisation
    The csv eda_mk_ok.csv is used to apply a geocoding function created in the src sp_geocode in the notebook geocode_bank.ipynb. As output the csv bankadditional_geocoded.csv is created.
3. Analysis of the categorical columns
    The values of the different categorical columns are studied and the values of the geocoded countries are transformed from their acronyms to full values.
    The nulls are filled in with unknown or with the mode depending on their volumetrics. For this, the csv vankadditional_geocoded.csv is imported and worked on in the notebook null_categories.ipynb. The src sp_categorias_nulos.py is created to create formulas to support the code and sp_vusualisation for the visualisation packages. As output the document df_gestion_nulos_ok is exported to csv.
4. Analysis of the numeric columns
    An analysis of the dataframe df_gestion_nulos_ok.csv is performed on the notebook columnas_numericas.ipynb. The src sp_columns_numerical_columns.py is used as support. The csv df_numerical_null_numbers_ok.csv is extracted as output.
5. Visualisation and analysis of the information
    An analysis of the dataframe df_nulos_numericos_ok.csv is performed in the notebook analisis_subscripciones.ipynb, conclusions are drawn and the sp_analisis_subscripciones is used to save the formulas. 
    During this working document the necessary information is extracted that will be used to report the conclusions.

The report on the results of the marketing campaign is presented in the PDF document Informe_EDA_Marketing_directo.v1. In this report you can get a clear view on the conclusions drawn during the analysis and the proposed strategies to bring future strategies closer to a higher number of sales.


