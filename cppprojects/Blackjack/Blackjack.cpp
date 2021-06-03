#include<iostream>
#include<vector>
#include<iterator>
#include <algorithm>
#include <cstdlib>
#include "Cards.h"
#include "playfunc.cpp"
using namespace std;
int main()
{
	bool new_game=1;
	char c;
	double bet=0,pairbet=0,warbet=0;
	double money=1000;
	short decknum;
	cout<<"How many decks you wanna play with?"<<endl; // the player choices how many cards are there
	cin>>decknum;
	vector<Cards>deck;
	while(new_game)
	{
		while(decknum<=0)cin>>decknum;
		cout<<"Bet money for new game,0 to exit"<<endl;
		cout<<"Current money: "<<money<<endl;
		cin>>bet;
		if(bet==0 || bet >=money)
		{
			new_game=0;
			break;
		}
		cout<<"Press y to bet for war,any key for no bet"<<endl; // the pair bet and the war bet are the same as the main one
		cin>>c;
		if(c=='y' || c=='Y')warbet=bet;
		cout<<"Press y to bet for pair,any key for no bet"<<endl;
		cin>>c;
		if(c=='y' || c=='Y')pairbet=bet;
		play(decknum,deck,bet,money,pairbet,warbet);
	}
	return 0;
}



