import random
import numpy as np
import os

def user(num, sts, filed, filed_list):
    filed[num-1] = sts
    filed_list.remove(num)
    
    print('', filed[0] ,' ' , filed[1],' ' , filed[2],'\n',
             filed[3],' ' , filed[4],' ' , filed[5],'\n',
             filed[6],' ' , filed[7],' ' , filed[8],'\n')
    return sts

def computer(num, filed, filed_list):
    filed[num-1] = 'X'
    filed_list.remove(num)
    
    print('', filed[0] ,' ' , filed[1],' ' , filed[2],'\n',
             filed[3],' ' , filed[4],' ' , filed[5],'\n',
             filed[6],' ' , filed[7],' ' , filed[8],'\n')
    return '+'

def win(filed, sts):
    if((filed[0] == sts and filed[1] == sts and filed[2] == sts ) |
       (filed[3] == sts and filed[4] == sts and filed[5] == sts ) |
       (filed[6] == sts and filed[7] == sts and filed[8] == sts ) |

       (filed[0] == sts and filed[3] == sts and filed[6] == sts ) |
       (filed[1] == sts and filed[4] == sts and filed[7] == sts ) |
       (filed[2] == sts and filed[5] == sts and filed[8] == sts ) |

       (filed[0] == sts and filed[4] == sts and filed[8] == sts ) |
       (filed[2] == sts and filed[4] == sts and filed[6] == sts )):
        
        return sts
    
def ttt(users):
    if(users==1):
        sts = "O"
    else:
        sts = "O"
        
    filed = np.array(range(1,10),dtype="O")
    filed_list = [1,2,3,4,5,6,7,8,9]
    start = True
    while(True):
        print("번호를 입해주세요")
        num = int(input())
        if win(filed, user(num,sts, filed,filed_list))==sts:
            print("플레이어 승리")
            break
        if not filed_list:
            print("FULL")
            break
            
            
        print("컴퓨터 입력")
        if win(filed,computer(random.choice(filed_list),filed, filed_list)) == "X":
            print("컴퓨터 승리")
            break
        if not filed_list:
            print("FULL")
            break
        #os.system('cls') #출력삭제   
if __name__ == "__main__":
    print("플레이어를 선택해주세요")
    print("1. 플레이\n2. 컴퓨터")
    input_user = input()
    num = int(input_user)

    ttt(num)
