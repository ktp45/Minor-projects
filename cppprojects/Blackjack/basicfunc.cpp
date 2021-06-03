#include<iostream>
#include<vector>
#include<iterator>
#include <algorithm>
#include <cstdlib>
#include "Cards.h"
#include "Cards.cpp"
using namespace std;
ostream& operator<<(ostream& out, const Cards& c) // operator overloading: printed cards should have suit and name
{
	 if(c.GetSuit()==0)return out<< c.GetName()<<"-C"; // C for Clubs, D for Diamonds, H for Hearts and S for Spades 
 	 if(c.GetSuit()==1)return out<< c.GetName()<<"-D";
  	 if(c.GetSuit()==2)return out<< c.GetName()<<"-H";
   	 if(c.GetSuit()==3)return out<< c.GetName()<<"-S";
}
void MakeDeck(int num,vector<Cards> &deck) //deck generating function
{
	for(num;num>0;num--) // if the number stored in num,which is the total cards, is dividable by 52, that would make num/52 decks in one
	{
		Cards curr;
		switch(num%13) // method based on residue on division by 13
		{
			case 0:
				curr.SetName('K');
				break;
			case 1:
				curr.SetName('A');
				break;
			case 12:
				curr.SetName('Q');
				break;
			case 11:
				curr.SetName('J');
				break;
			case 10:
				curr.SetName('T');
				break;
			default:
				curr.SetName(char(num%13)+'0');
				break;
								
		}
		curr.SetPower(num%13);
		curr.SetSuit((num/13)%4);
		if(curr.GetPower()>10 || curr.GetPower()==0)curr.SetPower(10);
		deck.push_back(curr);
	}
}
void PrintDeck(vector<Cards> deck) // deck printing func for testing and for counting cards
{
	vector<Cards>::iterator it;
	short br=0;
	for(it=deck.end();it>deck.begin();--it)
	{
		cout<<" "<<*it;
		br++;
		if(br%20==0)cout<<endl;
	}
	cout<<endl;
}
void Shuffle(vector<Cards> &deck) // shuffle func
{
	random_shuffle(deck.begin(), deck.end()); // usage of implemented in cpp shuffle
}
short Calcscore(vector<Cards> hand) // function that calculates the Blackjack score of a hand
{
	short score=0,numaces=0;
	short len=hand.size();
	for(int i=0;i<len;i++)
	{
		if(hand[i].GetPower()!=1)score+=hand[i].GetPower(); // ace is 11 or 1 if the score is above 21
		else
		{
			numaces++;
			score+=11;
		}
	}
	while(numaces>0 && score>21) // score reductor if it is above 21
	{
		score-=10;
		numaces--;
	}
	return score;
}
void PrintHand(vector<Cards> hand) // hand and score of the hand printer
{
	short len=hand.size();
	for(int i=0;i<len;i++)cout<<hand[i]<<" ";
	cout<<endl;
	cout<<"Handscore is:"<<Calcscore(hand)<<endl;
}
bool IsPair(vector<Cards> hand) // binary check for pair in hand since the is a pair bet
{
	if(hand[0].GetName()==hand[1].GetName())return 1;
	else return 0;
}
void PrintStatement(vector<Cards> hand,vector<Cards> dhand) // interface statement print
{
	if(dhand[0].GetName()=='A') // if the dealer has ace players can bet on insurance 2 to 1
	{
		cout<<"Press 1-Hit ; 2-Stand ; 3-Double ; 4-Insurance"<<endl;
	}

	if(dhand[0].GetName()!='A') // otherwise they can surrender and get half of their money
	{
		cout<<"Press 1-Hit ; 2-Stand ; 3-Double ; 4-Surrender"<<endl;
	}	
}
void war(vector<Cards>your_hand,vector<Cards>dealer_hand,double &bet,double &warbet,double &money) // Blackjack war func
{
	PrintHand(dealer_hand);
	PrintHand(your_hand);
	if(Calcscore(your_hand)>Calcscore(dealer_hand)) // the war is won only if the first player card is bigger than the dealer
	{
		char temp; // the ace counts as 1
		cout<<"You win the war,press y to bet the profit,n to take it."<<endl;
		cin>>temp;
		if(temp=='y'|| temp=='Y') // player has choice between betting the profit or taking it
		{
			bet+=warbet;
			money+=warbet;
			warbet=0;
		}
		else
		{
			money+=warbet*2;
			warbet=0;
		}
	}
	else
	{
		cout<<"You lost the war!"<<endl;
		warbet=0;
	}
	system("pause");
	system("cls");
}


