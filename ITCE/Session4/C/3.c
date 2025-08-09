#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void search(int number[],int count){
  int *max;
  for(int i=0;i<count;i++){
    if(number[i]>*max){
      max=&number[i];
    }
  }
  printf("\nmaximum number = %d",*max);

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
    search(number,count);
  }
  else if(type==2){
    for(int i=0;i<count;i++){
      printf("enter number[%d] = ",i);
      scanf("%d",&number[i]);
    }
    search(number,count);
  }
  else printf("error");
}