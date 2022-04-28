
Libraries needed:
* PyPDF
* PyPDF2
* Camelot
* Tabula
* Pandas
* Numpy
* Matplotlib
* Seaborn
* Os
* Tabulate


-----------------------------------------------------------------------------------------

Steps to execute project:
   1. Extract group34-project.zip in your local system
   2. Steps to execute the preprocessing part:
      Note: The Preprocessing part will take some time (around half an hour) please be patient.
         1. Goto folder named "Preprocessing"
         2. Goto Preprocessing1 or Preprocessing2
         3. Open your command line Terminal in the same folder and run the following commands
         ./preprocessing1.sh or ./preprocessing2.sh to run either preprocessing parts.
   3. Steps to execute the analysis part:
         1. Goto folder named "Analysis" 
         2. Open your command line Terminal in the same folder and run the following commands
         ./analysis.sh

-----------------------------------------------------------------------------------------

NOTE:
1. Outputs are generated in folder named ‘Outputs’
2. ‘Figures’ folder contains all images
3. "Preprocessing" folder contains all our pre-processing code that we used to generate suitable CSV files
4. We have used Python 3.8.10 to compile all our Python scripts

-----------------------------------------------------------------------------------------

Questions Description (corresponding CSVs, sh file names):


1. Which program in each of the top(5) institutes has the highest/lowest female to male ratio?
* Output CSV’s:
   * “Top institutes with highest female-male ratio.csv”. 
* Executable bash file: q1.sh


2. For all the institutes find the ratio of socially challenged (SC/ST, OBC etc) to a total number of children as well as economically backward people?
* Output CSV’s:  
   * “Top institutes with highest economically backward-total ratio.csv”, 
   * “Top institutes with highest socially backward-total ratio.csv”. 
* Executable bash file: q2.sh


3. Which institute offers the maximum number of people a full waiver in the fee?
* Output CSV’s:  
   * “Top programs and colleges which provide reimbursement to maximum number of students.csv”. 
* Executable bash file: q3.sh


4. Which institute has the percentage of people who do not belong to its state (foreign as well as different states)? show the diversity present among the students of each course(ratio of instate to outside students)
* Output CSV’s: 
   * “Top institutes with highest number of migrants.csv”. 
* Executable bash file: q4.sh


5. Which are the colleges that have the highest overfill/underfill per cent?
* Output CSV’s:  
   * “Top institutes with highest overfill percent.csv”, 
   * “Top institutes with highest number of vacancies.csv”. 
* Executable bash file: q5.sh


6. Which institutes have lifts/ramps in less than 80% of the buildings?
* Program name: q6.py
* Executable File:  q6.sh 
* Output CSV: 
   * Lift Facilities.csv


7. Which institutes don't allow inter-building movements? Also report the overall percentage of such institutes.
* Program name: q7.py
* Executable File:  q7.sh 
* Output CSV: 
   * Movement Facilities.csv


8. What all instis. don't have special(differently abled people) toilets in at least 80% buildings? 
* Program name: q8.py
* Executable File:  q8.sh 
* Output CSV: 
   * Toilet Facilities.csv


9. Find the top 5 and bottom 5 institute names, ratio which have the highest #student/#faculty ratio?
* Program name: q9.py
* Executable File:  q9.sh 
* Output CSV’s: 
   * Top 5 student to faculty ratio.csv, 
   * Worst 5 student to faculty ratio.csv


10. Find the top 5 institutes which received the highest annual earnings over the period of the last three years, 2017-18 to 2019-20(sum).
* Program name: q10.py
* Executable File:  q10.sh 
* Output CSV’s: 
   * 2017-18 EDP Earnings.csv, 
   * 2018-19 EDP Earnings.csv, 
   * 2019-20 EDP Earnings.csv, 
   * Total EDP Earnings.csv


11. Which college has the highest benefit from Executive Development Programme #Amount of Annual earnings / #Total students.
* Program name: q11.py
* Executable File:  q11.sh 
* Output CSV’s: 
   * EDP to Strength ratio 2018.csv,
   * EDP to Strength ratio 2019.csv,
   * EDP to Strength ratio 2020.csv, 
   * EDP to Strength ratio Total.csv


12 Find the colleges with the highest percentage of students going for higher studies.
* Output CSV’s:  
   * “higher_studies.csv”. 
* Executable bash file: q12.sh


13. Find the colleges with a minimum percentage of unplaced students. (year-wise)
* Output CSV’s: 
   * “unplaced.csv”. 
* Executable bash file: q13.sh


14. Find the course per college (over all the years: sum) that provides the highest package?
* Output CSV’s: 
   * “best_program.csv”. 
* Executable bash file: q14.sh


15. For each college, find the average number of students doing a PhD over the last 3 years, full time as well as part-time? 
* Output CSV’s:  
   * “phd.csv”. 
* Executable bash file: q15.sh


16. Find the top 5 and bottom 5 institutes which received the highest fundings from the consultancy projects for the last three years.
* Executable File: q16.sh (uses q16.py)
* Output Files:
   *  top5-consultancy-funding-{year}.csv
   *  bottom5-consultancy-funding-{year}.csv


17. Find the Top 5 institutes with the highest number of projects for each of the years.
*  Executable File: q17.sh (uses q17.py)
*  Output File:
   *  consultancy_projects_top5.csv


18. For each institute, find the year in which the ratio between the Number of client Projects and the Number of Client organisations was the highest.
*  Executable File: q18.sh (uses q18.py)
*  Output File:
   *  Maximum-project-to-client-ratio-year.csv
                
19.  Find the percentage of sponsored research projects and consultancy projects for each institute for 3 years.
*  Executable File:  q19.sh (uses q19.py)
*  Output File:
   *  Sponsored Research projects and consultancy projects.csv
20.  Which program per institute had the highest as well as the lowest intake for the last 2-3 years?
* Program name: q20.py
* Executable File:  q20.sh 
* Output file: 
   * min_max_program.csv


21.  Find the year in which every institute had the highest ratio for # projects/#agency among the above mentioned three years?
* Program name: q21.py
* Executable File:  q21.sh 
* Output file: 
   * max_project_year.csv


22.  Find the top 5 (in decreasing order) institute which received the highest amount over the period across the last three years, 2017-18 to 2019-20.
* Program name: q22.py
* Executable File:  q22.sh 
* Output file: 
   * highest_sponsorship.csv


23. Find the total intake of every insti. And the top 5 and bottom 5 institutes.
* Program name: q23.py
* Executable File:  q23.sh 
* Output file: 
   * 2019-20_intake.csv,
   * 2018-19_intake.csv,
   * 2017-18_intake.csv,
   * 2016-17_intake.csv,
   * 2015-16_intake.csv,
   * 2014-15_intake.csv and
   * overall_intake.csv


24.   Report colleges having rare courses (PG 1 year).
* Program name: q24.py
* Executable File:  q24.sh 
* Output file: 
   * rare_program.csv

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
