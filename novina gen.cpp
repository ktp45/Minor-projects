#include<iostream>
#include<cstring>
#include <ctime>
#include <cstdlib>
using namespace std;
int main()
{
	int n,len=0;
	cout<<"Enter number of headings:";
	cin>>n;
char vuzkl[3][10]
{
	"Unikalno",
	"Skandal",
    "Naglost"
};
char subekt[3][10]
{
	"Baba",
	"Macka",
    "Bager"
};
char obekt[3][10]
{
	"Sklad",
	"Dom",
    "Rqpa"
};
char deistv[3][10]
{
	"Sgazi",
	"Zadiga",
    "Machka"
};
int temp=0;
srand (time(0));
for(int i=0;i<n;i++)
{
	int p=rand()%3; //vsqka novina ima kluch chislo koeto se obrazuva po sledniqt nachin
	temp+=p;
	len+=strlen(vuzkl[p]);
    p=rand()%3;
	temp+=p*10;
	len+=strlen(subekt[p]);
	p=rand()%3;									
	temp+=p*100;
	len+=strlen(deistv[p]);
	p=rand()%3;
	temp+=p*1000;
	len+=strlen(obekt[p]);
	p=rand()%8;
	temp+=p*10000;
	len+=p+3;
	char* novina=new char[len];
	strcpy(novina,vuzkl[temp%10]);
	if(temp/10000!=0)for(int i=0;i<temp/10000;i++)strcat(novina,"!");
	strcat(novina," ");
	strcat(novina,subekt[temp%100/10]);	
	strcat(novina," ");
	strcat(novina,deistv[temp%1000/100]);	
	strcat(novina," ");
	strcat(novina,obekt[temp%10000/1000]);
	cout<<novina<<" "<<endl;
	temp=0;len=0;	
	delete[]novina;
}
	return 0;
}

