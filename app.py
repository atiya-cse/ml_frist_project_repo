import gradio as gr 
import pandas as pd 
import numpy as np

import pickle 

with open("student_rf_pipeline.pkl", "rb") as file:
    model = pickle.load(file)





#main logic 
def predict_gpa(gender, age, address, famsize, Pstatus,M_Edu, F_Edu,
                M_Job, F_Job, relationship, smoker, tuition_fee,  
                 time_friends, ssc_result):
    input_df = pd.DataFrame([[
        gender, age, address, famsize, Pstatus, M_Edu,
        F_Edu, M_Job, F_Job, relationship,smoker,
        tuition_fee, time_friends, ssc_result
    ]],
    columns= [
        'gender', 'age', 'address', 'famsize', 'Pstatus', 'M_Edu',
        'F_Edu', 'M_Job', 'F_Job', 'relationship','smoker',
        'tuition_fee', 'time_friends', 'ssc_result'
    ]
    )

     #prediction 
    prediction = model.predict(input_df)[0]

    #clipping

    return f"Predicted HSC Result: {np.clip(prediction, 0, 5):.2f}"


# pack inputs into a DtaFrame 
    input_df = pd.DataFrame([[
        gender, age, address, famsize, pstatus,M_edu, F_edu,
                M_job, F_job, relationship, smoker, tuition_fee,  
                 time_friends, ssc_result
    ]], columns= [
        'gender', 'age', 'address', 'famsize', 'pstatus','M_edu', 'F_edu',
                'M_job', 'F_job', 'relationship', 'smoker', 'tuition_fee',  
                 'time_friends', 'ssc_result'
    ]
    )

# prediction 
    prediction = model.predict(input_df)
    return f"Predicted HSC Result: {np.clip(prediction, 0, 5)} "

inputs = [
    gr.Radio( ["M", "F"], label="Gender"),
    gr.Number(label = "Age", value = 18),
    gr.Radio( ["Urban", "Rural"], label="Address"),

    gr.Radio(["GT3", "LE3"], label="Family"),
    gr.Radio( [ "Together", "Apart"], label= "parent Status"),
    gr.Slider(0, 4, step=1, label="Mother's Edu"),
    gr.Slider(0, 4, step=1, label= "Father's Edu"),
    gr.Dropdown( [ "At_home", "Health", "Other", "services", "Teacher"], label="Mother's Job"),
    gr.Dropdown( [ "Teacher", "Other", "services", "Health", "Buisness", "Farmar"], label="Father's Job"),
    gr.Radio( [ "Yes", "No"], label="Relationship"),
    gr.Radio( [ "Yes", "No"], label="Smoker"),
    gr.Number(label="Tuition Fee"),
    gr.Slider(1, 5, step=1, label= "Time with Friends"),
    gr.Number(label="SSC Result (GPA) ")


]




#interface 

app = gr.Interface(
    fn=predict_gpa,
    inputs=inputs,
    outputs="text",
    title="HSC prediction"
)

#launch 

app.launch(share=True)