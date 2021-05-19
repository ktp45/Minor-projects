#include<iostream>
#include<vector>
#include<iterator>
#include <algorithm>
#include <cstdlib>
using namespace std;
class Cards  // each card has name, suit and power on black jack
{
	char name;
	short bjpower;
	short suit;
	public:
	Cards(){};	//default constructor just in case
	Cards(char nam,int power)	// constuctor with parameters
	{
		name=nam;
		bjpower=power;
	}
	short GetPower()const// setters and getters to keep the capsulation
	{
		return bjpower;
	}
	char GetName()const
	{
		return name;
	}
	void SetPower(short power)
	{
		bjpower=power;
	}
	void SetName(char nam)
	{
		name=nam;
	}
	short GetSuit()const
	{
		return suit;
	}
	void SetSuit(short sui)
	{
		suit=sui;
	}
};
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
	while(!winner) // the bool var winner is a replace for the break word
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
		if(Calcscore(your_hand)>21) // if abovev 21 player loses
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
