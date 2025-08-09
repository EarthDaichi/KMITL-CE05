#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void select(int number[],int count){
  int min,indx;
  for(int j=0;j<count;j++){
    min = number[j];
    indx = j;
    for(int k=j+1;k<count;k++){
      if(number[k]<min){
        min=number[k];
        indx=k;
      }
    }
    number[indx]=number[j];
    number[j]=min;
    for(int l=0;l<count;l++){
      printf("%d ",number[l]);
    }
    printf("\n");
  }
}

int count,type;
int main(){
  srand(time(NULL));
  printf("enter count of number\n");
  scanf("%d",&count);
  int number[count];
  printf("select number type:\n 1.Random\n 2.enter\n");
  scanf("%d",&type);
  if(type==1){
    for(int i=0;i<count;i++){
      number[i]= rand() %100+1;
      printf("number[%d] = %d\n",i,number[i]);
    }
    select(number,count);
  }
  else if(type==2){
    for(int i=0;i<count;i++){
      printf("enter number[%d] = ",i);
      scanf("%d",&number[i]);
    }
    select(number,count);
  }
  else printf("error");
}