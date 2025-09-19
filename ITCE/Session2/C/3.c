#include <fullsdt.h> //นำเข้าฟังก์ชันทั่วๆไปจาก Libraly

char Character; //กำหนดตัวแปร Character สำหรับรับค่าตัวอักษร 1 ตัว
int main(){ //ฟังก์ชันหลักที่จะทำงานเมื่อเริ่มรันโปรแกรม
    printf("enter a Character"); //ส่งออกข้อความ ให้ผู้ใช่กรอกตัวอักษร 1 ตัว
    scanf("%c",&Character); //รับค่าตัวอักษร ใส่ในตัวแปร Character 
    if ((Character >= 'a' && Character <= 'z') || (Character >= 'A' && Character <= 'Z')) //เปรียบเทียบค่า ascii ของข้อมูลใน Character ถ้าอยู่ระหว่าง a-z หรือ A-Z
    {printf("%c is an Alphabet",Character);} //ส่งออกข้อความว่าตัวอักษรนั้นเป็น Alphabet 
    else {printf("%c isn't an Alphabet",Character);} //ส่งออกข้อความว่าตัวอักษรนั้นไม่เป็น Alphabet
}