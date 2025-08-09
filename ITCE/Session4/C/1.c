#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int count,type;
int sum = 0;
float avg;

void average(int number[],int count){
  for(int j=0;j<count;j++){
    sum += number[j];
  }
  avg = (float)sum/count;
  printf("\naverage of number = %.2f",avg);
}

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
    average(number,count);
  }
  else if(type==2){
    for(int i=0;i<count;i++){
      printf("enter number[%d] = ",i);
      scanf("%d",&number[i]);
    }
    average(number,count);
  }
  else printf("error");
}