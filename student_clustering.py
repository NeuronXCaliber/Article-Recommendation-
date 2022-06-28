# -*- coding: utf-8 -*-
"""Student Clustering

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pOaIAxnm_bLIPqafWCDx2JShHFSaxEcD
"""

import warnings
warnings.filterwarnings('ignore')
import sys
from mpl_toolkits.mplot3d import axes3d, Axes3D
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv("/content/Data_User_Modeling_Dataset - Training_Data.csv")
data.head()

dataset=data.drop(['Unnamed: 6','Unnamed: 7','Attribute Information:'],axis=1)
dataset.head()

x=data['Attribute Information:'].tolist()
for i in range(0,6):
  if(x[i]!='nan'):
    print(x[i])

dataset.isnull().sum()

x=dataset[' UNS'].tolist()
for i in range(len(x)):
  if(x[i]=='very_low'):
    x[i]=1
  elif(x[i]=='Low'):
    x[i]=2
  elif(x[i]=='Middle'):
    x[i]=3
  else:
    x[i]=4
print(x)

dataset[' UNS'].unique()

dataset['cluster_student']=x
dataset=dataset.drop([' UNS'],axis=1)
dataset.head()

pd.DataFrame(dataset).to_csv('student_cluster.csv',index=None)
pd.DataFrame(dataset['cluster_student']).to_csv('cluster_column.csv',index=None)

x=dataset.iloc[:,:-1]
y=dataset.iloc[:,-1]

x.head()

y.head()

from sklearn.model_selection import train_test_split
from sklearn import svm
X_train,X_val,y_train,y_val=train_test_split(x,y,test_size=0.4,shuffle=False)
X_val,X_test,y_val,y_test=train_test_split(X_val,y_val,test_size=0.5,shuffle=False)

def pso(n_particles, iterations, dimensions, inertia):

    # Range of SVR's hyperparameters (Particles' search space)
    # C, Epsilon and Gamma
    max_c = 1e4
    min_c = 1e-3
    max_e = 1e-1
    min_e = 1e-8
    max_g = 1e3
    min_g = 1e-3
    
    # Initializing particles' positions randomly, inside
    # the search space
    x = np.random.rand(n_particles, 1)*(max_c - min_c) + min_c
    y = np.random.rand(n_particles, 1)*(max_e - min_e) + min_e
    z = np.random.rand(n_particles, 1)*(max_g - min_g) + min_g

    c = np.concatenate((x,y,z), axis=1)

    # Initializing particles' parameters
    v = np.zeros((n_particles, dimensions))
    c1 = 2
    c2 = 2
    p_best = np.zeros((n_particles, dimensions))
    p_best_val = np.zeros(n_particles) + sys.maxsize  
    g_best = np.zeros(dimensions)
    g_best_val = sys.maxsize

    best_iter = np.zeros(iterations)

    # Initializing regression variables
    p_best_RGS = np.empty((n_particles), dtype = object);
    g_best_RGS = sys.maxsize

    

    # Displaying tridimensional search space
    plot(c)

    from sklearn.metrics import mean_squared_error
    
    for i in range(iterations):

        for j in range(n_particles):
          # Starting Regression
          rgs = svm.SVC(C = c[j][0], degree = c[j][1], gamma = c[j][2])

          # Fitting the curve
          rgs.fit(X_train, y_train)
          y_predict = rgs.predict(X_val)

          # Using Mean Squared Error to verify prediction accuracy
          mse = mean_squared_error(y_val, y_predict) 

          # If mse value for that search point, for that particle,
          # is less than its personal best point,
          # replace personal best
          if(mse < p_best_val[j]):   # mse < p_best_val[j]
              # The value below represents the current least Mean Squared Error
              p_best_val[j] = mse
              
              p_best_RGS[j] = rgs
                           

              # The value below represents the current search coordinates for
              # the particle's current least Mean Squared Error found
              p_best[j] = c[j].copy()
              
          # Using auxiliar variable to get the index of the
          # particle that found the configuration with the 
          # minimum MSE value
          aux = np.argmin(p_best_val)        
        
          if(p_best_val[aux] < g_best_val):
              # Assigning Particle's current best MSE to the Group's best    
              g_best_val = p_best_val[aux]

              # Assigning Particle's current best configuration to the Group's best
              g_best = p_best[aux].copy()

              # Group best regressor:
              # the combination of C, Epsilon and Gamma
              # that computes the best fitting curve
              g_best_RGS = p_best_RGS[aux]

        
          rand1 = np.random.random()
          rand2 = np.random.random()

          # The variable below influences directly the particle's velocity.
          # It can either make it smaller or bigger. 
          w = inertia

          # The equation below represents Particle's velocity, which is
          # the rate of change in its position
          v[j] = w*v[j] + c1*(p_best[j] - c[j])*rand1 + c2*(g_best - c[j])*rand2

          # Change in the Particle's position 
          c[j] = c[j] + v[j]

          # Below is a series of conditions that stop the particles from
          # leaving the search space
          if(c[j][2] < min_g):
            c[j][2] = min_g
          if(c[j][2] > max_g):
            c[j][2] = max_g
          if(c[j][1] < min_e):
            c[j][1] = min_e
          if(c[j][1] > max_e):
            c[j][1] = max_e
          if(c[j][0] < min_c):
            c[j][0] = min_c
          if(c[j][0] > max_c):
            c[j][0] = max_c
            
     
        # The variable below represents the least Mean Squared Error
        # of the current iteration
        best_iter[i] = g_best_val
                
        print('Best value iteration # %d = %f\n'%(i, g_best_val))

    # Coordinates found after all the iterations
    print('Group Best configuration found: ')
    print(g_best)
    print('\n')
    print('Best Classifier:\n')
    print(g_best_RGS)
    print('\n')
    # Displaying the MSE value variation throughout the iterations
    t = range(iterations)
    plt.plot(t, best_iter, label='Fitness Value')
    plt.legend()
    plt.show()

    # Displaying Particles' final configuration
    #plot(c)

    # Making the prediction with the best configuration of C, Epsilon and
    # Gamma found by the particles
    predict_test = g_best_RGS.predict(X_test)

    
    # Displaying actual values and predicted values for
    # Group's best configuration found overall
    #print(color.BOLD + 'Predictions with the Population Best Value found:\n' + color.END)
    evaluate(predict_test)

'''class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'''

# Function that displays tridimensional plot
'''def plot(some_list):
 
  ax = Axes3D(plt.figure())
  ax.scatter3D(some_list[:,0], some_list[:,1], some_list[:,2], color = 'r')
  ax.set_xlabel('$C$', fontsize = 20)
  ax.set_ylabel('$\epsilon$', fontsize = 25)
  ax.zaxis.set_rotate_label(False) 
  ax.set_zlabel('$\gamma$', fontsize=30, rotation = 0)
  ax.zaxis._axinfo['label']['space_factor'] = 1.0
  plt.show()

  print('\n')
  print('\n')'''

def evaluate(predictions):

    from sklearn.metrics import mean_squared_error,accuracy_score
    import statistics as st

    predict_test = predictions

    # To un-normalize the data:
    # Multiply the values by
    # data.to_numpy().max()

    plt.plot(range(len(y_test)), y_test, label='Real')
    plt.plot(range(len(predict_test)), predict_test, label='Predicted')
    plt.legend()
    plt.show()
    
    acc = accuracy_score(y_test, predict_test)
    print('\n')
    print('\n')
    print('Accuracy for the Test Set:\t %f' %acc)
    print('\n')
    print('\n')
    print('Predictions Average:\t %f' %((predict_test.sum()/len(predict_test))))
    print('\n')
    print('\n')
    print('Predictions Median:\t %f' %(st.median(predict_test)))
    print('\n')
    print('\n')

pso(120, 30, 3, 1)

svc=svm.SVC(C=5248.058208238585, degree=0.07638391163384857, gamma=0.001)
svc.fit(X_train,y_train)
pred=svc.predict(X_test)

from sklearn import metrics
accuracy=metrics.accuracy_score(y_test,pred)
accuracy*100

one=dataset['cluster_student']==1
cluster_1=dataset[one]

two=dataset['cluster_student']==2
cluster_2=dataset[two]

three=dataset['cluster_student']==3
cluster_3=dataset[three]

four=dataset['cluster_student']==4
cluster_4=dataset[four]

pd.DataFrame(cluster_1).to_csv('student_cluster_1.csv',index=None)
pd.DataFrame(cluster_2).to_csv('student_cluster_2.csv',index=None)
pd.DataFrame(cluster_3).to_csv('student_cluster_3.csv',index=None)
#pd.DataFrame(cluster_4).to_csv('student_cluster_4.csv',index=None)
pd.DataFrame(cluster_4).to_csv('student_cluster_4.csv',index=None)

