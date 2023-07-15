# Student Performance in Portugal

## Overview
The goal of this project is to conduct a comprehensive analysis to identify the factors that significantly impact student grades. By understanding the key drivers of academic performance, we aim to develop targeted interventions and support systems that can improve student outcomes and enhance their overall educational experience. The project will involve statistical modeling, correlation analysis, and feature importance determination to uncover the factors that have the most significant influence on student grades.

## Project Description


## Installation


## Usage


## Data
The data for this project focuses on student achievement in secondary education in two Portuguese schools. The dataset includes various attributes such as student grades, demographic information, social factors, and school-related features. The data for this project was downloaded from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/320/student+performance).

The following table provides a description of the attributes present in both the `student-mat.csv(Math course)` and `student-por.csv (Portuguese language course)` datasets:

| Attribute | Attribute Description                                            | Attribute Type | Attribute Values                                                    |
|-----------|-----------------------------------------------------------------|----------------|--------------------------------------------------------------------|
| school    | Student's school                                                | Binary         | 'GP' - Gabriel Pereira<br/>'MS' - Mousinho da Silveira              |
| sex       | Student's sex                                                   | Binary         | 'F' - female<br/>'M' - male                                        |
| age       | Student's age                                                   | Numeric        | From 15 to 22                                                      |
| address   | Student's home address type                                     | Binary         | 'U' - urban<br/>'R' - rural                                         |
| famsize   | Family size                                                     | Binary         | 'LE3' - less or equal to 3<br/>'GT3' - greater than 3               |
| Pstatus   | Parent's cohabitation status                                    | Binary         | 'T' - living together<br/>'A' - apart                               |
| Medu      | Mother's education                                              | Numeric        | 0 - none<br/>1 - primary education (4th grade)<br/>2 - 5th to 9th grade<br/>3 - secondary education<br/>4 - higher education |
| Fedu      | Father's education                                              | Numeric        | 0 - none<br/>1 - primary education (4th grade)<br/>2 - 5th to 9th grade<br/>3 - secondary education<br/>4 - higher education |
| Mjob      | Mother's job                                                    | Nominal        | 'teacher'<br/>'health' care related<br/>'services' (e.g. administrative or police)<br/>'at_home'<br/>'other'                    |
| Fjob      | Father's job                                                    | Nominal        | 'teacher'<br/>'health' care related<br/>'services' (e.g. administrative or police)<br/>'at_home'<br/>'other'                    |
| reason    | Reason to choose this school                                    | Nominal        | close to 'home'<br/>school 'reputation'<br/>'course' preference<br/>'other'                                                       |
| guardian  | Student's guardian                                              | Nominal        | 'mother'<br/>'father'<br/>'other'                                   |
| traveltime| Home to school travel time                                      | Numeric        | 1 - <15 min.<br/>2 - 15 to 30 min.<br/>3 - 30 min. to 1 hour<br/>4 - >1 hour                                                  |
| studytime | Weekly study time                                               | Numeric        | 1 - <2 hours<br/>2 - 2 to 5 hours<br/>3 - 5 to 10 hours<br/>4 - >10 hours                                                      |
| failures  | Number of past class failures                                   | Numeric        | n if 1<=n<3, else 4                                                |
| schoolsup | Extra educational support                                       | Binary         | 'yes' or 'no'                                                      |
| famsup    | Family educational support                                      | Binary         | 'yes' or 'no'                                                      |
| paid      | Extra paid classes within the course subject                    | Binary         | 'yes' or 'no'                                                      |
| activities| Extra-curricular activities                                     | Binary         | 'yes' or 'no'                                                      |
| nursery   | Attended nursery school                                         | Binary         | 'yes' or 'no'                                                      |
| higher    | Wants to take higher education                                  | Binary         | 'yes' or 'no'                                                      |
| internet  | Internet access at home                                         | Binary         | 'yes' or 'no'                                                      |
| romantic  | With a romantic relationship                                    | Binary         | 'yes' or 'no'                                                      |
| famrel    | Quality of family relationships                                 | Numeric        | From 1 - very bad to 5 - excellent                                 |
| freetime  | Free time after school                                          | Numeric        | From 1 - very low to 5 - very high                                 |
| goout     | Going out with friends                                          | Numeric        | From 1 - very low to 5 - very high                                 |
| Dalc      | Workday alcohol consumption                                     | Numeric        | From 1 - very low to 5 - very high                                 |
| Walc      | Weekend alcohol consumption                                     | Numeric        | From 1 - very low to 5 - very high                                 |
| health    | Current health status                                           | Numeric        | From 1 - very bad to 5 - very good                                 |
| absences  | Number of school absences                                       | Numeric        | From 0 to 93                                                       |
| G1        | First period grade (Math or Portuguese)                         | Numeric        | From 0 to 20                                                       |
| G2        | Second period grade (Math or Portuguese)                        | Numeric        | From 0 to 20                                                       |
| G3        | Final grade (Math or Portuguese)                                | Numeric        | From 0 to 20                                                       |

This table provides a summary of the attributes in the dataset, their descriptions, types, and possible values.


## Methods


## Results


## Contributing


## License

