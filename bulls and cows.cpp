#include<iostream>
//#include "BullsAndCows.h"
using namespace std;
bool isValid(int a)
{
	if(a/1000==0 || a/1000>=10)return 0;
	if(a<0)return 0;
	int b=a/1000,c=a/100%10,d=a/10%10,e=a%10;
	if(b==c || b==d || b==e || c==d || c==e || d==e)return 0; 
	if(b==0 || c==0 || d==0 || e==0)return 0;
	return 1;
}
int compbulls(int x,int y) // sravnqva bikove na 2 chisla
{
	int b=x/1000,c=x/100%10,d=x/10%10,e=x%10;
	int b1=y/1000,c1=y/100%10,d1=y/10%10,e1=y%10;
	int bulls=0;
	if(b==b1)bulls++;
	if(c==c1)bulls++;
	if(d==d1)bulls++;
	if(e==e1)bulls++;
	return bulls;
}
int compcows(int x,int y)
{
	int b=x/1000,c=x/100%10,d=x/10%10,e=x%10;
	int b1=y/1000,c1=y/100%10,d1=y/10%10,e1=y%10;
	int cows=0;
    if(b==c1 || b==d1 || b==e1)cows++;
    if(c==b1 || c==d1 || c==e1)cows++;
    if(d==c1 || d==b1 || d==e1)cows++;
    if(e==c1 || e==d1 || e==b1)cows++;
	return cows;
}
//8523
const int* tryGuess(int x)
{
	int* answer = new int[2];
	cout<<"Neka da opitame "<<x<<endl;
	cout<<"Vuvedete broi bikove"<<endl;
	cin>>answer[0];
	cout<<"Vuvedete broi kravi"<<endl;
	cin>>answer[1];
	return answer;
}
void play()
{
	int count=0,br=0;
	for(int i=1000;i<10000;i++)
	{
		if(isValid(i))count++; // broika na vs validni chisla
	}
int* all=new int[count];
for(int i=1000;i<10000;i++)
{
	if(isValid(i))
	{
		all[br]=i;  // zapametqvane v masiv s vsichki tqh
		br++;
	}
}
bool* tried=new bool[count]; // masiv dali ne sa izklucheni
for(int i=0;i<count;i++)tried[i]=1;
while(br>1) // povtarqme dokato ne ostane samo 1 chislo koeto e tursenoto
{
	const int* temp;
	int tempnum;
	for(int i=0;i<count;i++)
	{
		if(tried[i])
		{
			temp=tryGuess(all[i]); // probvame porednoto chislo v narastvasht red i zapazvame broi bikove i kravi
			tempnum=all[i];
			break;
		}
	}
	for(int i=0;i<count;i++)
	{
		if((compcows(tempnum,all[i])!=temp[1] || compbulls(tempnum,all[i])!=temp[0])&& tried[i]) // sravnqvame s vsichki i izkl tezi koito nqma kak da sa
		{
			tried[i]=0;
			br--;
		}
	}
	delete[]temp;
}
for(int i=0;i<count;i++)
	{
		if(tried[i])
		{
			cout<<"Vasheto chislo e: "<<all[i]<<endl;
		}	
	}
	delete[]tried;
	delete[]all;
}
int main()
{
cout<<"Namislete 4 cifreno chislo s razlichni cifri bez 0, programata shte go poznae do 7 opita.\nPri vseki opit bik e chislo koeto si e na mqstoto i e vqrno, a krava, samo vqrno."<<endl;
play();
}
