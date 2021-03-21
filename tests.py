def solution(A):
    #def solution(A):
    A.sort()
    uni_list = list(set(A))


    missing_element = len(uni_list)+1

    for i,v in enumerate(uni_list):
        inc = (i-1) if v < 0 else (i+1)
        missing_element = missing_element ^ v ^ inc

    if missing_element == None or missing_element == 0:
        missing_element = max(uni_list) + 1

    return 1 if missing_element <= 0 else missing_element

def solution_1(A,K):
    #def solution(A):
    a = 0
    for i in range(K):
        a = A[len(A)-1]
        A.remove(a)
        A = [a] + A
    return A

def solution_2(A):
    #def solution(A):
    cnt = 0
    alter_side = 1 if A[0] == 1 else 0
    for i in range(len(A)):
        if A[i] > 1 or A[i] < -1:
            raise Exception
        if A[i] != alter_side:
            cnt += 1
        alter_side = 0 if alter_side == 1 else 1
    return cnt

def sol3(A):
    alternates = 0
    for i, v in enumerate(A):
        if v < 0 or v > 1:
            raise Exception
        alternates = ((v ^ i) & 1) + alternates
    return min(alternates, len(A)-alternates)


# Function to find out minimum steps 
def findMinSteps(mat, n, m, dp,vis): 
  
    # boundary edges reached 
    if (n == 0 or m == 0 or n == (r - 1) or m == (col - 1)): 
        return 0
      
   
    # already had a route through this 
    # point, hence no need to re-visit 
    if (dp[n][m] != -1): 
        return dp[n][m] 
   
    # visiting a position 
    vis[n][m] = True
   
    ans1, ans2, ans3, ans4=10**9,10**9,10**9,10**9
  
   
    # vertically up 
    if (mat[n - 1][m] == 0): 
        if (vis[n - 1][m]==False): 
            ans1 = 1 + findMinSteps(mat, n - 1, m, dp, vis) 
      
   
    # horizontally right 
    if (mat[n][m + 1] == 0): 
        if (vis[n][m + 1]==False): 
            ans2 = 1 + findMinSteps(mat, n, m + 1, dp, vis) 
      
   
    # horizontally left 
    if (mat[n][m - 1] == 0): 
        if (vis[n][m - 1]==False): 
            ans3 = 1 + findMinSteps(mat, n, m - 1, dp, vis) 
      
   
    # vertically down 
    if (mat[n + 1][m] == 0): 
        if (vis[n + 1][m]==False): 
            ans4 = 1 + findMinSteps(mat, n + 1, m, dp, vis) 
      
   
    # minimum of every path 
    dp[n][m] = min(ans1, min(ans2, min(ans3, ans4))) 
    return dp[n][m] 
  
   
# Function that returns the minimum steps 
def minimumSteps(mat, n, m): 
  
    # index to store the location at 
    # which you are standing 
    twox = -1
    twoy = -1
   
    # find '2' in the matrix 
    for i in range(n):  
        for j in range(m):  
            if (mat[i][j] == 2): 
                twox = i 
                twoy = j 
                break
              
          
        if (twox != -1): 
            break
      
   
    # Initialize dp matrix with -1 
    dp=[[-1 for i in range(col)] for i in range(r)] 
      
   
    # Initialize vis matrix with false 
    vis=[[False for i in range(col)] for i in range(r)] 
      
   
    # Call function to find out minimum steps 
    # using memoization and recursion 
    res = findMinSteps(mat, twox, twoy, dp, vis) 
   
    # if not possible 
    if (res >= 10**9): 
        return -1
    else: 
        return res 
  
   
# Driver Code 
  
  


if __name__ == "__main__":
    print(sol3([0, 1, 0, 1, 1]))
    mat= [ [0, 0, 0], [0, 0, 1], [1, 0, 0], [0, 0, 0] ] 
    r = 4
    col = 3
  
    print(minimumSteps(mat, r, col))