# Student Performance in Portugal

## Overview


## Project Description


## Installation


## Usage


## Data
The data for this project focuses on student achievement in secondary education in two Portuguese schools. The dataset includes various attributes such as student grades, demographic information, social factors, and school-related features. The data for this project was downloaded from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/320/student+performance).

The following table provides a description of the attributes present in both the `student-mat.csv(Math course)` and `student-por.csv (Portuguese language course)` datasets:

| Attribute  | Attribute Description                                                                       | Attribute Type | Attribute Values                            |
|------------|-------------------------------------------------------------------------------------------|----------------|---------------------------------------------|
| school     | Student's school `('GP' - Gabriel Pereira or 'MS' - Mousinho da Silveira)`         | Binary         | 'GP', 'MS'                                  |
| sex        | Student's sex `('F' - female or 'M' - male)`                                        | Binary         | 'F', 'M'                                    |
| age        | Student's age `(from 15 to 22)`                                                   | Numeric        | 15 to 22                                    |
| address    | Student's home address type `('U' - urban or 'R' - rural)`                          | Binary         | 'U', 'R'                                    |
| famsize    | Family size `('LE3' - less or equal to 3 or 'GT3' - greater than 3)`                | Binary         | 'LE3', 'GT3'                                |
| Pstatus    | Parent's cohabitation status ('T' - living together or 'A' - apart)               | Binary         | 'T', 'A'                                    |
| Medu       | Mother's education (0 - none, 1 - primary education (4th grade), 2 - 5th to 9th grade, 3 - secondary education or 4 - higher education) | Numeric | 0, 1, 2, 3, 4                               |
| Fedu       | Father's education (0 - none, 1 - primary education (4th grade), 2 - 5th to 9th grade, 3 - secondary education or 4 - higher education) | Numeric | 0, 1, 2, 3, 4                               |
| Mjob       | Mother's job ('teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other') | Nominal | 'teacher', 'health', 'services', 'at_home', 'other' |
| Fjob       | Father's job ('teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other') | Nominal | 'teacher', 'health', 'services', 'at_home', 'other' |
| reason     | Reason to choose this school (close to 'home', school 'reputation', 'course' preference or 'other') | Nominal | 'home', 'reputation', 'course', 'other'      |
| guardian   | Student's guardian ('mother', 'father' or 'other')                               | Nominal        | 'mother', 'father', 'other'                  |
| traveltime | Home to school travel time ( 1 - <15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, or 4 - >1 hour) | Numeric | 1, 2, 3, 4                                  |
| studytime  | Weekly study time (1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours) | Numeric | 1, 2, 3, 4                                  |
| failures   | Number of past class failures (n if 1<=n<3, else 4)                              | Numeric        | 1 to 4                                      |
| schoolsup  | Extra educational support (binary: yes or no)                                             | Binary         | 'yes', 'no'                                |
| famsup     | Family educational support (yes or no)                                            | Binary         | 'yes', 'no'                                |
| paid       | Extra paid classes within the course subject (Math or Portuguese) (yes or no)     | Binary         | 'yes', 'no'                                |
| activities | Extra-curricular activities (yes or no)                                           | Binary         | 'yes', 'no'                                |
| nursery    | Attended nursery school (yes or no)                                               | Binary         | 'yes', 'no'                                |
| higher     | Wants to take higher education (yes or no)                                        | Binary         | 'yes', 'no'                                |
| internet   | Internet access at home (yes or no)                                               | Binary         | 'yes', 'no'                                |
| romantic   | With a romantic relationship (yes or no)                                          | Binary         | 'yes', 'no'                                |
| famrel     | Quality of family relationships (from 1 - very bad to 5 - excellent)             | Numeric        | 1, 2, 3, 4, 5                              |
| freetime   | Free time after school (from 1 - very low to 5 - very high)                      | Numeric        | 1, 2, 3, 4, 5                              |
| goout      | Going out with friends (from 1 - very low to 5 - very high)                      | Numeric        | 1, 2, 3, 4, 5                              |
| Dalc       | Workday alcohol consumption (from 1 - very low to 5 - very high)                 | Numeric        | 1, 2, 3, 4, 5                              |
| Walc       | Weekend alcohol consumption (from 1 - very low to 5 - very high)                | Numeric        | 1, 2, 3, 4, 5                              |
| health     | Current health status (from 1 - very bad to 5 - very good)                       | Numeric        | 1, 2, 3, 4, 5                              |
| absences   | Number of school absences (from 0 to 93)                                         | Numeric        | 0 to 93                                    |
| G1         | First period grade (from 0 to 20)                                                | Numeric        | 0 to 20                                    |
| G2         | Second period grade (from 0 to 20)                                               | Numeric        | 0 to 20                                    |
| G3         | Final grade (from 0 to 20, output target)                                        | Numeric        | 0 to 20                                    |



## Methods


## Results


## Contributing


## License

