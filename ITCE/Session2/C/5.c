#include <fullstd.h> //นำเข้าฟังก์ชันทั่วๆไปจาก Libraly

char Char; //กำหนดตัวแปร Char สำหรับเก็บค่า ตัวอักษร 1 ตัว
int main(){ //ฟังก์ชันหลักที่จะทำงานเมื่อเริ่มรันโปรแกรม
    printf("input a Character"); //ส่งออกข้อความ ให้ผู้ใช่กรอกตัวอักษร 1 ตัว
    scanf("%c",&Char); //รับค่าตัวอักษร ใส่ในตัวแปร Char
    switch(Char){ //นำตัวแปร Char ใส่ในฟังก์ชัน switch()
        case 'a' : printf("it is an a Vowel"); break; //ถ้าค่าในตัวแปรเป็น a ส่งออกข้อความว่า มันคือ สระ a
        case 'e' : printf("it is an e Vowel"); break; //ถ้าค่าในตัวแปรเป็น e ส่งออกข้อความว่า มันคือ สระ a
        case 'i' : printf("it is an i Vowel"); break; //ถ้าค่าในตัวแปรเป็น i ส่งออกข้อความว่า มันคือ สระ a
        case 'o' : printf("it is an o Vowel"); break; //ถ้าค่าในตัวแปรเป็น o ส่งออกข้อความว่า มันคือ สระ a
        case 'u' : printf("it is an u Vowel"); break; //ถ้าค่าในตัวแปรเป็น u ส่งออกข้อความว่า มันคือ สระ a
        case 'A' : printf("it is an A Vowel"); break; //ถ้าค่าในตัวแปรเป็น A ส่งออกข้อความว่า มันคือ สระ A
        case 'E' : printf("it is an E Vowel"); break; //ถ้าค่าในตัวแปรเป็น E ส่งออกข้อความว่า มันคือ สระ E
        case 'I' : printf("it is an I Vowel"); break; //ถ้าค่าในตัวแปรเป็น I ส่งออกข้อความว่า มันคือ สระ I
        case 'O' : printf("it is an O Vowel"); break; //ถ้าค่าในตัวแปรเป็น O ส่งออกข้อความว่า มันคือ สระ O
        case 'U' : printf("it is an U Vowel"); break; //ถ้าค่าในตัวแปรเป็น U ส่งออกข้อความว่า มันคือ สระ U
        default : printf("it isn't a Vowel"); //ถ้าค่าในตัวแปรเป็นตัวอื่น ส่งออกข้อความว่ามันไม่ใช่สระ
    }
}