#include<iostream>
#include<vector>
#include<iterator>
#include <algorithm>
#include <cstdlib>
#include "Cards.h"
#include "basicfunc.cpp"
void choice(vector<Cards> &deck,vector<Cards> &your_hand,vector<Cards> &dealer_hand,double &bet,double &money,short &temp,double &insbet,bool &surr)
{
	PrintStatement(your_hand,dealer_hand); // function doing things depending on player's choices
	cin>>temp;
	while(temp<1 || temp>4) // validation
	{
		cin>>temp;	
	}
	system("cls");
	switch(temp)
	{
		case 1: // if the player hits he takes cards
			your_hand.push_back(deck.back());
			deck.pop_back();
			PrintHand(dealer_hand);
			PrintHand(your_hand);
			break;
		case 3: // if the player doubles, he hits once with doubled bet
			your_hand.push_back(deck.back());
			deck.pop_back();
			PrintHand(dealer_hand);
			PrintHand(your_hand);
			money-=bet;
			bet*=2;
			temp=2;
			break;
		case 4: // if the player wants an Insurance, he bets money on it
			PrintHand(dealer_hand);
			PrintHand(your_hand);
			if(dealer_hand[0].GetName()=='A')
			{
				insbet=bet;
				money-=insbet;
			}
			else
			{
				surr=1;
				temp=2;				
			}
			break;				
	}
	if(Calcscore(your_hand)>21)
	{
	temp=2;
	}		
}
void wincond(vector<Cards>	&your_hand,vector<Cards> &dealer_hand,double &insbet,double &money,bool &winner,double &bet) //calculates winnings 
{
		if(Calcscore(dealer_hand)==21) // Insurance pays 2 to 1
		{
			insbet*=2;
			money+=insbet;
		}
		if(Calcscore(dealer_hand)>21 || (Calcscore(dealer_hand)<Calcscore(your_hand) && Calcscore(dealer_hand)<21)) 
			{  // player wins if the dealer busts or he has more points than the dealer
				cout<<"You win!"<<endl;
				winner=1;
				bet*=2;
			}
		else if(Calcscore(dealer_hand)==Calcscore(your_hand) && Calcscore(your_hand)<=21) // if the points are even there is a tie
			{
				cout<<"Tie!"<<endl;
				winner=1;
			}
		else
			{
				cout<<"You Lose!"<<endl;
				winner=1;
				bet=0;
			}
}
void play(short decknum,vector<Cards> &deck,double &bet,double &money,double &pairbet,double &warbet) // function which leads the game
{
	vector<Cards>your_hand;
	vector<Cards>dealer_hand;
	short your_score=0,dealer_score=0;
	short temp=0;
	bool winner=0,surr=0;
	double insbet=0;	
	money-=bet;money-=pairbet;money-=warbet; // we put the bets on the table
	while(!winner) // we play till there is a winner
	{
		if(deck.empty() || deck.size()<=38) // if there is a deck made by 38 aces player will have 21 and the dealer 17, both players can use more than that number of cards
		{
			MakeDeck(decknum*52,deck); // generates the selected from user number of decks
			Shuffle(deck);
		}
		if(bet==69 || bet==420) // secret bets which see the deck
		{
			cout<<"Cheat bet activated.Here is the deck!"<<endl;
			PrintDeck(deck);
			system("pause");
		} 
		your_hand.push_back(deck.back()); // each player takes card and the deck loses one
		deck.pop_back();
		dealer_hand.push_back(deck.back());
		deck.pop_back();
		if(warbet!=0) // if the user has bet on war there is war
		{
			war(your_hand,dealer_hand,bet,warbet,money);
		}
		your_hand.push_back(deck.back());
		deck.pop_back();
		PrintHand(dealer_hand);
		PrintHand(your_hand);
		if(pairbet!=0) // same as warbet
		{
			if(IsPair(your_hand))
			{
				cout<<"You have a pair! You win!"<<endl;
				if(your_hand[0].GetSuit()==your_hand[1].GetSuit())pairbet*=30;
				else pairbet*=7;
				money+=pairbet;
				pairbet=0;
			}
			else cout<<"You lost your pair bet!"<<endl;
		}
		if(Calcscore(your_hand)==21 && dealer_hand[0].GetPower()!=1 && dealer_hand[0].GetPower()!=10) // if the player has 21 and dealer has no chance of having 21 in 2 cards there is a Blackjack
		{
			cout<<"Blackjack! You win!"<<endl;
			winner=1;
			bet*=2.5;
			break;
		}
		while(temp!=2)
		{
			choice(deck,your_hand,dealer_hand,bet,money,temp,insbet,surr);
		}
		if(surr) // surrender option
		{
			cout<<"You Surrendered!"<<endl;
			surr=1;
			winner=1;
			bet=bet/2;
			break;
		}
		if(Calcscore(your_hand)>21) // if above 21 player loses
		{
			cout<<"Bust! You lose!"<<endl;
			if(insbet!=0)
			{
				dealer_hand.push_back(deck.back());
				deck.pop_back();
				PrintHand(dealer_hand);
				if(Calcscore(dealer_hand)==21) // bet even in that case his insurance bet still exist
				{
					insbet*=2;
					money+=insbet;
					insbet=0;
				}
			}
			winner=1;
			bet=0;
			break;
		}
		while(Calcscore(dealer_hand)<=16) // The dealer must hit on 16 or below and stand on 17 or above
		{
			system("cls");
			dealer_hand.push_back(deck.back());
			deck.pop_back();
			PrintHand(dealer_hand);
			PrintHand(your_hand);
		}
		wincond(your_hand,dealer_hand,insbet,money,winner,bet); // check who wins
		insbet=0;
		temp=0;
	}
	money+=bet;
}
