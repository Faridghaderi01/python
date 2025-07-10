import numpy as np
from math import  ceil 
from  colorama import Fore , Back , Style , init

init()

# Main_Matrix = np.array([[1.0,1.0,3.0] , [4.0,5.0,6.0] , [7.0,8.0,9.0]])
Main_Matrix = [[0.0 for Rows in range (0,3)] for Cols in range(0,3)] 

#  ----------------------------------------------------------
#   Fill main matrix using 2 for loops
#  ----------------------------------------------------------

def Fill_Matrix(L):
    for Rows in range(len(L)):
        for Cols in range(len(L[0])):
           print (Fore.GREEN + 'M=[',Rows,' ,' ,Cols,']: ', end='')
           L[Rows][Cols] = float (input()) 
    return L

#  ------------------------------------------------------------------
#   in this function we calculate 2*2 matrix elemnts for Kahad matrix
#  ------------------------------------------------------------------


def Calc_elem(mtx):
    result = mtx[0][0] * mtx[1][1] - mtx[1][0]*mtx[0][1]
    return result


#  ------------------------------------------------------------------
#     this function calculate Kahad matrix
#  ------------------------------------------------------------------

def Kahad ( L ):
    K_Mtx =np.array([[ 0.0 , 0.0 , 0.0 ],[ 0.0 , 0.0 , 0.0 ],[ 0.0 , 0.0 , 0.0 ]])
    L_tmp = L
    L_bak1 = []
    for Rows in range (len (L)):
        for Cols in range (len (L[0])):
            L_bak1 = np.delete( L_tmp, Rows, 0)   # for each elemnt i,j in matrix we should igonre that i'th  row and j'th col
            L_bak1 = np.delete( L_bak1, Cols, 1)  # to extract a 2*2 matrix then  calculate Matrix[i,j] value by Calc_elem() function
            K_Mtx[Rows][Cols] = Calc_elem(L_bak1) # برای محاسبه ماتریس کهاد برای هر عنصر باید سطر و ستون آن عنصر را حذف کرده  
    print (Fore.YELLOW + '    Kahad Matrix   ' )                 #و ماتریس 2*2 بدست آمده را به تابع خط 40 بفرستیم
    print (K_Mtx)        
    return K_Mtx

#  -----------------------------------------------------------------------------
#     this function calculate Coherence matrix
#     in Coherence matrix is a matrix that each matrix value [i,j] should 
#     multiplye in (-1) once in between ( باید یک در میان در یک منفی ضرب شود) 
#  -----------------------------------------------------------------------------

def Coherence ( L ):
    for Rows in range (len (L)):
        for Cols in range (len (L[0])): 
            L[Rows][Cols] = ((-1)**(Rows+Cols))*L[Rows][Cols]   
    Fore.RESET
    print (Fore.GREEN + '   Coherence Matrix    ') 
    print (L)
    return L


#  -----------------------------------------------------------------------------
#     this function calculate Additive matrix
#     in Change cols and rows of Coherence matrix 
#     در ماتریس الحاقی جای سطر و ستونها را عوض می کنیم 
#  -----------------------------------------------------------------------------


def Additive ( L ):
     L_tmp = np.array([[ 0.0 , 0.0 , 0.0 ],[ 0.0 , 0.0 , 0.0 ],[ 0.0 , 0.0 , 0.0 ]])
     for Rows in range (len(L)):
         for Cols in range (len(L[0])):
             L_tmp[Cols][Rows] = L[Rows][Cols]
     L=L_tmp  
     print ('   Additive Matrix    ') 
     print (L)     
     return L

#  -----------------------------------------------------------------------------
#     this function calculate determinant of Main matrix
#       محاسبه دترمینان ماتریس اصلی
#  -----------------------------------------------------------------------------

def Det (mtx):
    determinan = 0
    elm00 = mtx[0][0] * ( mtx[1][1] * mtx[2][2] - mtx[2][1] * mtx[1][2] )
    elm01 = mtx[0][1] * (mtx[1][0] * mtx[2][2] - mtx[2][0] * mtx[1][2]  )
    elm02 = mtx[0][2] * ( mtx[1][0] * mtx[2][1] - mtx[2][0] * mtx[1][1] )
    determinan = elm00 - elm01 + elm02
    print ('Determinant = ', determinan)
    return determinan

#  -----------------------------------------------------------------------------
#     this function calculate (1/determinant) * Additive matrix 
#     that results reverse matrix
#     این تابع ماتریس معکوس را بدست می اورد که فرمول آن عبارت است از (دترمینان /1  ضرب در ماترس الحاقی)
#  -----------------------------------------------------------------------------


def Rev_Mtx(L,det):
    
    R_mtx = np.array([[ 0.0 , 0.0 , 0.0 ],[ 0.0 , 0.0 , 0.0 ],[ 0.0 , 0.0 , 0.0 ]])
    
    for Rows in range(len(L)):
        for Cols in range(len(L[0])):
            R_mtx[Rows][Cols] = det * L[Rows][Cols]
    
    return R_mtx


#  -------------------------------------------------------------------------------------------------------------------------
#     this function test our algorithm 
#     by multiplying  (  Main_Matrix * Reversed_Matrix ) that result in Same Matrix
#     با این تابع صحت عملکرد الگوریتم خود را می سنجیم . با ضرب ماتریس اصلی در ماتریس معکوس ماتریس همانی بدست می آید
#  -------------------------------------------------------------------------------------------------------------------------

def Test_Func(L1,L2):
    Tmp_L = np.array([[ 0.0 , 0.0 , 0.0 ],[ 0.0 , 0.0 , 0.0 ],[ 0.0 , 0.0 , 0.0 ]])

    for Rows in range (len(L1)):
        for Cols in range (len(L1[0])):
            for elm in range (len(L1[0])):
                Tmp_L[Rows][Cols] += L1[Rows][elm]*L2[elm][Cols]

    for Rows in range (len(L1)):
        for Cols in range (len(L1[0])):
            Tmp_L[Rows][Cols] = round(Tmp_L[Rows][Cols])

    return Tmp_L

#  -------------------------------------------------------------------------------------------------------------------------
#
#                                               Main Program Starts Here
#
#  -------------------------------------------------------------------------------------------------------------------------



Fill_Matrix(Main_Matrix)

print ('---------------------------------------------------')
print (Main_Matrix)

determinants = Det(Main_Matrix) # calculate determinant
if ( determinants != 0 ):       # to avoid Divided by Zero جهت جلوگیری از خطای تقسیم بر صفر
    
    Reverse = Additive (Coherence(Kahad(Main_Matrix)))
    
    print ('-----------------------------------------------')
   
    Reverse = Rev_Mtx(Reverse , 1/Det(Main_Matrix))
   
    print ('------------------Reverse Main_Matrix ---------')
    print (Reverse)
   
    Test=[]
    Test = Test_Func(Reverse, Main_Matrix)
   
    print ('--------------- Test Algorithm -------------')
    print (Test)
else:
    print ('Main_Matrix has no determinan so Reverse Main_Matrix not exists!.')
    exit (0)
