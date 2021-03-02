#include<iostream>
#include<cmath>
using namespace std;
int main()
{
int N,M,minbroilampi;
bool plan=1,osvetena=0;
cout<<"Vuvedete broi peiki i lampi"<<endl;
cin>>N>>M;
int** XYpeiki=new int*[N];
int** XYlampi=new int*[M];
for(int i=0;i<N;i++)
{
	XYpeiki[i]=new int[2];
}
for(int i=0;i<M;i++)
{
	XYlampi[i]=new int[3];
}
for(int i=0;i<N;i++)
{
	cout<<"Kordinati na "<<i+1<<" peika:"<<endl;
cin>>XYpeiki[i][0]>>XYpeiki[i][1];
cout<<endl;
}
for(int i=0;i<M;i++)
{
	cout<<"Kordinati na "<<i+1<<" lampa i nein radius:"<<endl;
cin>>XYlampi[i][0]>>XYlampi[i][1]>>XYlampi[i][2];
cout<<endl;
}
//
for(int i=0;i<N;i++)
{
	for(int j=0;j<M;j++)
	{
		if(sqrt((XYlampi[j][0]-XYpeiki[i][0])*(XYlampi[j][0]-XYpeiki[i][0])+(XYlampi[j][1]-XYpeiki[i][1])*(XYlampi[j][1]-XYpeiki[i][1]))<XYlampi[j][2])osvetena=1;
	}
	if(!osvetena)plan=0;
	osvetena=0;
}
if(plan)cout<<"plana e izpulnen"<<endl;
else cout<<"plana ne e izpulnen"<<endl;
//
if(plan)
{
	minbroilampi=M;
	int minR=XYlampi[0][2];
	for(int i=1;i<M;i++)
	{
		if(minR<XYlampi[i][2])minR=XYlampi[i][2];
	}
	for(int k=0;k<M;k++)
	{
	
	for(int i=0;i<N;i++)
{
	for(int j=0;j<k;j++)
	{
		if(sqrt((XYlampi[j][0]-XYpeiki[i][0])*(XYlampi[j][0]-XYpeiki[i][0])+(XYlampi[j][1]-XYpeiki[i][1])*(XYlampi[j][1]-XYpeiki[i][1]))<minR)osvetena=1;
	}
	if(!osvetena)plan=0;
	osvetena=0;
}
if(plan && k<minbroilampi)k=minbroilampi;
plan=1;
}
}
return 0;
}
