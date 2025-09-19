#include <fullstd.h> //นำเข้าฟังก์ชันนทั่วๆไปจากLibraly

int main() { //ฟังก์ชันหลักที่จะทำงานเมื่อเริ่มรันโปรแกรม
    int number; //ประกาศตัวแปร ชื่อ number เป็นจำนวนเต็ม
    printf("enter the number"); //ส่งออกข้อความว่า ให้ผู้ใช้ระบุ ตัวเลข
    scanf("%d",&number); //รับค่าตัวแปร number จาก input
    if(number%2==0) printf("Number is Even"); //เช็คค่า เมื่อ เศษเหลือจากการหาร number ด้วย 2 เป็น 0 (number เป็นเลขคู่) ให้ส่งออกข้อความว่า Number เป็นเลขคู่
    else printf("Number is Odd"); //ถ้าไม่เข้าสถานการณ์ด้านบน ส่งออกข้อความว่า Number เป็นเลขคี่
}