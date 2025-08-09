#include <stdio.h>

int deci;
int bi[64];
int i;

int main(){
    printf("input decimal = ");
    scanf("%d",&deci);
    do{
        bi[i]=deci%2;
        deci = deci/2;
        i++;
    }
    while(deci>0);
    for(int j=i-1;j>=0;j--){
        printf("%d",bi[j]);
    }
}