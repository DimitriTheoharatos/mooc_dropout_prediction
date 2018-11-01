# MOOC Dropout Prediction Rate


In this project, I use data compiled by HarvardX and MITx on their first year of EdX Massive Open Online Courses (MOOC) in 
order to predict whether or not a student is likely to explore a course (i.e. the student looks at > 50% of the course).

In addition, I deployed one of the Logistic Regression models with a Flask App to integrate user interaction.

### Install

This project requires **Python** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [matplotlib](http://matplotlib.org/)
- [plotly](http://plot.ly/python/)
- [Flask](http://flask.pocoo.org/)

You will also need to have software installed to run and execute a [Jupyter Notebook](http://ipython.org/notebook.html)


### Files

`data_cleaning.ipynb` --> notebook to quickly clean through some of the data.  

`EDA.ipynb` --> Covers exploratory analysis of our features of interest. Includes interactive viz with Plotly. 

`modeling.ipynb` --> Contains the bulk of the modeling and algorithmic analysis. 

`HMXPC13_DI_v2_5-14-14.csv` --> Original uncleaned data. 

`visualize.csv` --> Used in conjunction with theEDA notebook. 

`modeling_data.csv` --> Used in conjunction with the modeling notebook. 


### Run

In a terminal or command window, navigate to the top-level project directory and run the following command:


```bash
jupyter notebook
```

This will open the Jupyter Notebook software and project file in your browser.


### Executing the Flask App:

In a terminal or command window, navigate to the flask directory and run the following command:

```bash
python app.py
```

Then, on your local machine, go to the following link: http://127.0.0.1:5000/id 

#### Data:

  
**Important Features**
- `ages`: the binned age of the student. 
- `education`: the highest level of education attained by the student. 
- `subject`: the subject of the course. 
- `final_cc_cname`: the country of origin of the student. 
- `gender`: the gender of the participant. 
- `course`: the actual name of the course. 


**Target Variable**
- `explored/certified` Whether the student explored or was certified in the course.  
