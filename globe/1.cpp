#include<stdio.h>
int main()
{
    int i,j,tmp,count,flag;
    int num[20];
    count=0;
    for(i=1000;i<1999;i++)
    {   
        for(j=0;j<10;j++)  num[j]=0;
        tmp=i;
        while(tmp)
        {
            num[tmp%10]++;
            tmp/=10;
        }
        flag=0;
        for(j=0;j<10;j++) 
        { 
            if (num[j]==2) flag++;
        }
        if (flag==1)    { printf("%d\n",i );  count++;}

    }
 
    return 0;
}
