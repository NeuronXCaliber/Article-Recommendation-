# Article-Recommendation
Article Recommendation to the student based on students knowledge/learning capacity
![image](https://user-images.githubusercontent.com/78382164/176204008-955d31eb-6967-40b5-b556-4800369440fe.png)

Article will be recommended to the students based on his/her knowledge and learning capacity. 

Article recommendation can be classified into 5 categories :
1. If a student is very low in interest/knowledge/capacity, then very easy/simple article will be recommended to the student.
2. If a student has less interest/knowledge/capacity but seeking for learning, then a bit good article will be recommended to the student for learning.
3. If a student's interest/knowledge/capacity is moderate level, then moderate level artticle will be recommended to the student.
4. If the student's interest is high and has good amount of learning capacity/knowledge then a very good article will be recommended to the student.

Article can be classified into few steps: 
1. 1 star rated article for very low students.
2. 2 star rated article for low students.
3. 3 star article for moderate students.
4. 4-5 star rated article for high level students. 

Students capacity can be clustered through few steps: 
1. Mark a very low capacity student to 1.
2. Mark a low capacity student to 2.
3. Mark a moderate capacity student to 3.
4. Mark a high capacity student to 4.

Algorithms used : 
An optimized Suppport Vector Machine algorithm has been used to cluster the student and judge the capacity of student. 
![image](https://user-images.githubusercontent.com/78382164/176206665-7f7b8c51-e63f-40cc-93d4-d30de3a098ed.png)

Capacity od the student can be judged by best model accuracy by hyper parameter tuning of SVM model. 
![image](https://user-images.githubusercontent.com/78382164/176206985-d43b66e7-0cb3-4a5a-a4fc-cfc175392c43.png)


Recommendation of article has been done by using Recurrent Neural Network algorithm. 
![image](https://user-images.githubusercontent.com/78382164/176207264-9b916ed4-ff1f-441d-8a53-a3e4d2024fc0.png)

In this scenario, students choices are very higher than their expertise. They dont know whether they ill be able to learn that particular concept or not. 
![image](https://user-images.githubusercontent.com/78382164/176213340-edc7ef1a-32b6-4c76-89e2-dc4859cd502c.png)

By using this system students can be aware about their knowledge/capacity and a particular concept can be provided to the student based on his/her capacity. 
Step by step learning, growing and increasing knowledge will be helpful for the student. 

If a student is very poor in knowledge then he/she must be provided by a very easy article. So that he/she can learn that first then go for next one.

Combination of an optimized SVM model + Recurrent Neural Network model will help to overcome the problem and choose the best pathway to learn. 



