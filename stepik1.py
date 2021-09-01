import sweetviz as sv
import pandas as pd

df = pd.read_csv(r'C:\Users\User\Desktop\Back_end_dev\git_course\202107_процент по линиям.csv')
my_report = sv.analyze([df, 'Процент по линиям'])
my_report.show_html()
