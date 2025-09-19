#include <fullstd.h> //นำเข้าฟังก์ชันทั่วๆไปจาก Libraly

int main() { //ฟังก์ชันหลักที่จะทำงานเมื่อเริ่มรันโปรแกรม
    int Count; //กำหนดตัวแปร Count เป็นประเภท จำนวนเต็ม
    printf("enter count of number to compare\n"); //ส่งออกข้อความ ให้ผู้ใช้ระบุ จำนวนตัวแปรที่จะนำมาเปรียบเทียบ
    scanf("%d",&Count); //รับค่าตัวแปร Count
    int Number[Count]; //กำหนดตัวแปรอาร์เรย์ชื่อNumber ประเภทจำนวนเต็ม โดยมีขนาดเท่ากับ ข้อมูลที่เก็บในตัวแปร Count 
        for(int i=0;i<Count;i++){ //for loop ทำงานโดย กำหนดตัวแปร i ที่มีค่า เป็นจำนวนเต็ม 0 กำหนดให้ for loop ทำงานเมื่อ i น้อยกว่า Count 
            printf("enter number %d of %d = ",i+1,Count); //ส่งออกข้อความให้ผู้ใช้กรอกตัวเลขที่จะนำมาเปรียบเทียบ 
            scanf("%d",&Number[i]); //รับค่าตัวเลข ใส่ในอาร์เรย์ Number ช่องที่ i
        }
    if(Count<2){ //นำตัวแปร Count มาเปรียบเทียบกับ เลข 2
        printf("Error Count of number to compare is less than 2\n"); //ถ้าน้อยกว่า 2 ส่งออกข้อความว่า จำนวนของตัวเลขที่จะนำมาเปรียบเทียบ น้อยกว่า 2
    }
    else if(Count == 2){ //ถ้า Count เท่ากับ 2
        if(Number[0]==Number[1]){ // ถ้าจำนวนที่ 1 และ 2 มีค่าเท่ากัน
            printf("Both Number is Equal and it is %d",Number[0]); //ส่งออกข้อความว่า ตัวเลขทั้งสองมีค่าเท่ากัน และบอกตัวเลข
        }
        else if(Number[0]>Number[1]){ // หรือถ้า เลขตัวที่ 1 มีค่ามากกว่า เลขตัวที่ 2
            printf("The biggest number is %d",Number[0]); //ส่งออกข้อความว่า เลขที่มีค่ามากที่สุดคือ เลขตัวที่ 1
        }
        else{
            printf("The biggest number is %d",Number[1]);//ส่งออกข้อความว่า เลขที่มีค่ามากที่สุดคือ เลขตัวที่ 2
        }
    }
    else{ //ถ้านอกเหนือกว่าตัวเปรียบเทียบข้างบน
        int Max = INT_MIN; //กำหนดตัวแปร Max สำหรับเก็บค่าสูงสุดจากการเปรียบเทียบ โดยกำหนดค่าไว้เป็นค่าต่ำสุด
        for(int i=0;i<Count;i++){ //for loop ทำงานโดย กำหนดตัวแปร i ที่มีค่า เป็นจำนวนเต็ม 0 กำหนดให้ for loop ทำงานเมื่อ i น้อยกว่า Count
            if(Number[i]>Max){ //ถ้า ค่าใน Number[i] มากกว่า Max
                Max = Number[i]; //ค่า Max = Number[i]
            }
        }

        if(Max==INT_MIN){ //ถ้า Max มีค่าเท่ากับ ค่าต่ำสุดของจำนวนเต็ม หรือค่าที่กำหนดไว้ตอนแรก
            printf("Error"); //ส่งออกข้อความ Error
        }
        else{ //นอกเหนือจาก if ข้างบน
            printf("The biggest number is %d",Max); //ส่งออกข้อความว่า ค่าที่ใหญ่ที่สุดคือ ข้อมูลในตัวแปร Max
        }
    }
}