StudentDict = { 'Amar': [0,23,44] , 'Nidhi': [0,25,46] ,'KJ':[0,50,14]}
Admin = { 'Python':999 , 'admin':123}

import statistics as s

class GradingSys:
    
    def login(uname,password):
        if uname =='Python' and passwrod === '999' Admin:
            GradingSys.option()
         
        else:
            print ('Invalid password,will detonate in 5 seconds!')
            uname = input('Username:')
            password = input('Password:')
            GradingSys.login(uname,password)
            
    def option():

            print ('Welcome to Grade Central'
                   '[1] - Enter Grades'
                   '[2] - Remove Student'
                   '[3] - Student Average Grades'
                   '[4] - Exit')
                   
            N = input('What would you like to do today? (Enter a number)')
            if N == '1':
                StudentName = input('For which student would you like to enter grades :')
                Grade = input('Enter Grades for '+ StudentName + ':')
                GradingSys.EnterGrade(StudentName,Grade);
                GradingSys.option();

            elif N == '2':
                StudentName = input('Which student do you want to remove :')              
                del StudentDict[StudentName]
                print(StudentDict)
                GradingSys.option();

            elif N == '3':
                StudentName = input('For which student you want average grade:')
                GradingSys.Mean(StudentName)
                
            elif N == '4':
                print('Thank You!!')
                print(StudentDict)
                
            else:
                print ('Not a valid option')
                
    def EnterGrade(StudentName ,Grade):
            
        if StudentName in StudentDict:
                
            StudentDict[StudentName].append(float(Grade))
            print(StudentDict[StudentName])
            print(StudentDict)
            GradingSys.option();
        else:
             print ("Student Name does not exist")
             
    def MeanGrade(StudentName):
            
        if StudentName in StudentDict:
            Mean = s.mean(StudentDict[StudentName])
            print('Mean for '+ StudentDict[StudentName] +'is' + Mean)
            print(StudentDict)
            
        else:
             print ("Student Name does not exist")            
            
            
uname = input('Username:')
password = input('Password:')
GradingSys.login(uname,password)



    
