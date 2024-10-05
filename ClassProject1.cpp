/* Student record management system */

#include<iostream>
#include<string>
using namespace std;

struct Student
{
    int rollNumber;
    string name;
    string course;
    string DOB;
    int age;
    float marks;
};

void displayStudent(const Student& student) {
    cout<< "Roll Number :" << student.rollNumber<<endl;
    cout<< "Name of Student :" << student.name<<endl;
    cout<< "Course of Student:" << student.course<<endl;
    cout<< "Data Of Birth :" << student.DOB<<endl;
    cout<< "Age of student :" << student.age<<endl;
    cout<< "Total marks :" << student.marks<<endl;
    cout<< "-------------------------\n";

}
int main()
{
    int TotalStudents;
    cout<< "Enter the number of students: ";
    cin>>TotalStudents;

    //define a fixed size array to storing students records
    Student students[10]; 
    
    //ensuring total student does not exceed the array size
    if(TotalStudents>10){
        cout<<"Maximun number of student is 100"<<endl;
        TotalStudents=10;
    }
    
    for (int i =0;i<TotalStudents;++i)
    {
        Student student;
        cout<<"Enter details for Students"<< (i+1)<<":\n";
        cout<<"Roll Number :";
        cin>>student.rollNumber;

        cout<<"Name of Student:";
        cin.ignore();  //ignore the newline character left in the buffer
        getline(cin,student.name);

        cout <<"Course :";
        getline(cin, student.course);

        cout <<"date of birth :";
        getline(cin, student.DOB);


        cout <<"Age:";
        cin>> student.age;
        
        cout <<"Markes :";
        cin>> student.marks;
     
        students[i]=student;
        
    }

    cout<< "\nStudent Datails :\n";
    for(int i=0;i < TotalStudents;++i){
        displayStudent(students[i]);
    }
     
    return 0 ;}