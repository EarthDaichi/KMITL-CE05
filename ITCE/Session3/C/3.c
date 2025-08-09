#include <stdio.h> //นำเข้าฟังก์ชั่นทั่วไปจากLibraly

int number;
int r=0;
int main(){ //ฟังก์ชั่นพื้นฐาน
    printf("input number"); //ส่งออกข้อความขอค่าตัวเลขจากผู้ใช้
    scanf("%d",&number); //รับค่าตัวเลข

    while(number>0){ //ระหว่างที่ตัวเลขมากกว่า 0
        printf("%d %d\n",number,r); //ส่งออกค่าตัวเลข และ จำนวนรอบ
        r++; //จำนวนรอบ +1
        number = number/10; //ค่าตัวเลขใหม่ เท่ากับค่าตัวเลขเก่า หารด้วย 10 
    }
    printf("number of digits = %d\n",r); //ส่งออกค่า จำนวนรอบ เป็นจำนวนหลักของตัวเลข
}