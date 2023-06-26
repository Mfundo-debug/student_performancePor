#use log_reg to predict the result of student performance and deploy it on the web
import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.title('Student Performance Prediction')
#st.write('This is a simple example of using a custom prediction model to interact with Streamlit.')
st.write('This app predicts the result of student performance based on the data of student.')
st.write('Please input the data of student and click the button to predict the result of student performance.')
#LOAD THE MODEL
model = joblib.load('log_reg.pkl')
#CREATE THE USER INPUT FIELDS
#st.sidebar.header('User Input Parameters')
#add features for the model from student performance dataset
sex = st.selectbox('sex', ['F', 'M'])
age = st.slider('age', 15, 22, 18)
address = st.selectbox('address', ['Urban', 'Rural'])
famsize = st.selectbox('famsize', ['Greater than 3', 'Less than 3'])
Pstatus = st.selectbox('Pstatus', ['Together', 'Apart'])
Medu = st.selectbox('Medu', ['None', 'Primary Education(4th grade)', '5th to 9th grade', 'secondary education',
                              'higher education'])
Fedu = st.selectbox('Fedu', ['None', 'Primary Education(4th grade)', 
                             '5th to 9th grade', 'secondary education'])
Mjob = st.selectbox('Mjob', ['teacher', 'health care', 'civil services', 'at_home', 'other'])
Fjob = st.selectbox('Fjob', ['teacher', 'health care', 'civil services', 'at_home', 'other'])
reason = st.selectbox('reason', ['home to school', 'reputation', 'course', 'other'])
guardian = st.selectbox('guardian', ['mother', 'father', 'other'])
traveltime = st.selectbox('traveltime', ['<15 min', '15 to 30 min', '30 min to 1 hour', '>1 hour'])
studytime = st.selectbox('studytime', ['<2 hours', '2 to 5 hours', '5 to 10 hours', '>10 hours'])
failures = st.selectbox('failures', ['0', '1', '2', '3'])
schoolsup = st.selectbox('schoolsup', ['yes', 'no'])
famsup = st.selectbox('famsup', ['yes', 'no'])
paid = st.selectbox('paid', ['yes', 'no'])
activities = st.selectbox('activities', ['yes', 'no'])
nursery = st.selectbox('nursery', ['yes', 'no'])
higher = st.selectbox('higher', ['yes', 'no'])
internet = st.selectbox('internet', ['yes', 'no'])
romantic = st.selectbox('romantic', ['yes', 'no'])
famrel = st.selectbox('famrel', ['1', '2', '3', '4', '5'])
freetime = st.selectbox('freetime', ['1', '2', '3', '4', '5'])
goout = st.selectbox('goout', ['1', '2', '3', '4', '5'])
Dalc = st.selectbox('Dalc', ['1', '2', '3', '4', '5'])
Walc = st.selectbox('Walc', ['1', '2', '3', '4', '5'])
health = st.selectbox('health', ['1', '2', '3', '4', '5'])
absences = st.slider('absences', 0, 93, 0)
#Preprocess user input
#sex
if sex == 'F':
    sex = 0
else:
    sex = 1
#address
if address == 'Urban':
    address = 0
else:
    address = 1
#paid
if paid == 'yes':
    paid = 0
else:
    paid = 1
#higher
if higher == 'yes':
    higher = 0
else:
    higher = 1
#internet
if internet == 'yes':
    internet = 0
else:
    internet = 1
#romantic
if romantic == 'yes':
    romantic = 0
else:
    romantic = 1
#schoolsup
if schoolsup == 'yes':
    schoolsup = 0
else:
    schoolsup = 1
#famsup
if famsup == 'yes':
    famsup = 0
else:
    famsup = 1
#activities
if activities == 'yes':
    activities = 0
else:
    activities = 1
#nursery
if nursery == 'yes':
    nursery = 0
else:
    nursery = 1
#guardian
if guardian == 'mother':
    guardian = 0
elif guardian == 'father':
    guardian = 1
else:
    guardian = 2
    #reason
if reason == 'home to school':
    reason = 0
elif reason == 'reputation':
    reason = 1
elif reason == 'course':
    reason = 2
else:
    reason = 3
#traveltime
if traveltime == '<15 min':
    traveltime = 0
elif traveltime == '15 to 30 min':
    traveltime = 1
elif traveltime == '30 min to 1 hour':
    traveltime = 2
else:
    traveltime = 3
#studytime
if studytime == '<2 hours':
    studytime = 0
elif studytime == '2 to 5 hours':
    studytime = 1
elif studytime == '5 to 10 hours':
    studytime = 2
else:
    studytime = 3
#failures
if failures == '0':
    failures = 0
elif failures == '1':
    failures = 1
elif failures == '2':
    failures = 2
else:
    failures = 3
#famrel
if famrel == '1':
    famrel = 0
elif famrel == '2':
    famrel = 1
elif famrel == '3':
    famrel = 2
elif famrel == '4':
    famrel = 3
else:
    famrel = 4
#freetime
if freetime == '1':
    freetime = 0
elif freetime == '2':
    freetime = 1
elif freetime == '3':
    freetime = 2
elif freetime == '4':
    freetime = 3
else:
    freetime = 4
#goout
if goout == '1':
    goout = 0
elif goout == '2':
    goout = 1
elif goout == '3':
    goout = 2
elif goout == '4':
    goout = 3
else:
    goout = 4
#Dalc
if Dalc == '1':
    Dalc = 0
elif Dalc == '2':
    Dalc = 1
elif Dalc == '3':
    Dalc = 2
elif Dalc == '4':
    Dalc = 3
else:
    Dalc = 4
#Walc
if Walc == '1':
    Walc = 0
elif Walc == '2':
    Walc = 1
elif Walc == '3':
    Walc = 2
elif Walc == '4':
    Walc = 3
else:
    Walc = 4
    #health
if health == '1':
    health = 0
elif health == '2':
    health = 1
elif health == '3':
    health = 2
elif health == '4':
    health = 3
else:
    health = 4
#absences
absences = absences
#Create a dictionary containing the features
features = pd.DataFrame({
    'sex': sex, 'age': age, 'address': address, 'famsize': famsize, 'Pstatus': Pstatus, 'Medu': Medu, 'Fedu': Fedu,
})
#Transform features using scalar
from sklearn.preprocessing import StandardScaler
scalar = StandardScaler()
features = scalar.transform(features)
#Make prediction using model loaded from disk as per the data.
prediction = model.predict(features)
#Take the first value of prediction
output = prediction[0]
#Display the result with probability
if output == 1:
    st.write('This student is likely to pass with probability of ', round(prediction[0][1]*100), '%')
else:
    st.write('This student is likely to fail with probability of ', round(prediction[0][0]*100), '%')
    







