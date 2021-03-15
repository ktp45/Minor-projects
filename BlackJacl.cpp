#include<iostream>
#include<vector>
#include<iterator>
#include <algorithm>
#include <cstdlib>
using namespace std;
class Cards 
{
	char name;
	short bjpower;
	short suit;
	public:
	Cards(){};
	Cards(char nam,int power)
	{
		name=nam;
		bjpower=power;
	}
	short GetPower()const
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
ostream& operator<<(ostream& out, const Cards& c)
{
	 if(c.GetSuit()==0)return out<< c.GetName()<<"-C";
 	 if(c.GetSuit()==1)return out<< c.GetName()<<"-D";
  	 if(c.GetSuit()==2)return out<< c.GetName()<<"-H";
   	 if(c.GetSuit()==3)return out<< c.GetName()<<"-S";
}
void MakeDeck(int num,vector<Cards> &deck) 
{
	for(num;num>0;num--)
	{
		Cards curr;
		switch(num%13)
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
void PrintDeck(vector<Cards> deck)
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
void Shuffle(vector<Cards> &deck)
{
	random_shuffle(deck.begin(), deck.end());
}
short Calcscore(vector<Cards> hand)
{
	short score=0,numaces=0;
	short len=hand.size();
	for(int i=0;i<len;i++)
	{
		if(hand[i].GetPower()!=1)score+=hand[i].GetPower();
		else
		{
			numaces++;
			score+=11;
		}
	}
	while(numaces>0 && score>21)
	{
		score-=10;
		numaces--;
	}
	return score;
}
void PrintHand(vector<Cards> hand)
{
	short len=hand.size();
	for(int i=0;i<len;i++)cout<<hand[i]<<" ";
	cout<<endl;
	cout<<"Handscore is:"<<Calcscore(hand)<<endl;
}
bool IsPair(vector<Cards> hand)
{
	if(hand[0].GetName()==hand[1].GetName())return 1;
	else return 0;
}
short PrintStatement(vector<Cards> hand,vector<Cards> dhand)
{
	if(dhand[0].GetName()=='A')
	{
		cout<<"Press 1-Hit ; 2-Stand ; 3-Double ; 4-Insurance"<<endl;
		return 4;
	}

	if(dhand[0].GetName()!='A')
	{
		cout<<"Press 1-Hit ; 2-Stand ; 3-Double ; 4-Surrender"<<endl;
		return 4;
	}	
}
void war(vector<Cards>your_hand,vector<Cards>dealer_hand,double &bet,double &warbet,double &money)
{
	PrintHand(dealer_hand);
	PrintHand(your_hand);
	if(Calcscore(your_hand)>Calcscore(dealer_hand))
	{
		char temp;
		cout<<"You win the war,press y to bet the profit,n to take it."<<endl;
		cin>>temp;
		if(temp=='y'|| temp=='Y')
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
void play(vector<Cards> &deck,vector<Cards>	&your_hand,vector<Cards> &dealer_hand,double &bet,double &money,short &temp,double &insbet,bool &surr)
{
	int templimit=PrintStatement(your_hand,dealer_hand);
	cin>>temp;
	while(temp<1 || temp>templimit)
	{
		cin>>temp;	
	}
	system("cls");
	switch(temp)
	{
		case 1:
			your_hand.push_back(deck.back());
			deck.pop_back();
			PrintHand(dealer_hand);
			PrintHand(your_hand);
			break;
		case 3:
			your_hand.push_back(deck.back());
			deck.pop_back();
			PrintHand(dealer_hand);
			PrintHand(your_hand);
			money-=bet;
			bet*=2;
			temp=2;
			break;
		case 4:
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
void wincond(vector<Cards>	&your_hand,vector<Cards> &dealer_hand,double &insbet,double &money,bool &winner,double &bet)
{
		if(Calcscore(dealer_hand)==21)
		{
			insbet*=2;
			money+=insbet;
		}
		if(Calcscore(dealer_hand)>21 || (Calcscore(dealer_hand)<Calcscore(your_hand) && Calcscore(dealer_hand)<21))
			{
				cout<<"You win!"<<endl;
				winner=1;
				bet*=2;
			}
		else if(Calcscore(dealer_hand)==Calcscore(your_hand))
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
void draw(short decknum,vector<Cards> &deck,double &bet,double &money,double &pairbet,double &warbet)
{
	vector<Cards>your_hand;
	vector<Cards>dealer_hand;
	short your_score=0,dealer_score=0;
	short temp=0;
	bool winner=0,surr=0;
	double insbet=0;	
	money-=bet;money-=pairbet;money-=warbet;
	while(!winner)
	{
		if(deck.empty())
		{
			MakeDeck(decknum*52,deck);
			Shuffle(deck);
		}
		if(bet==69 || bet==420)
		{
			cout<<"Cheat bet activated.Here is the deck!"<<endl;
			PrintDeck(deck);
			system("pause");
		} 
		your_hand.push_back(deck.back());
		deck.pop_back();
		dealer_hand.push_back(deck.back());
		deck.pop_back();
		if(warbet!=0)
		{
			war(your_hand,dealer_hand,bet,warbet,money);
		}
		your_hand.push_back(deck.back());
		deck.pop_back();
		PrintHand(dealer_hand);
		PrintHand(your_hand);
		if(pairbet!=0)
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
		if(Calcscore(your_hand)==21)
		{
			cout<<"Blackjack! You win!"<<endl;
			winner=1;
			bet*=2.5;
			break;
		}
		while(temp!=2)
		{
			play(deck,your_hand,dealer_hand,bet,money,temp,insbet,surr)	;
		}
		if(surr)
		{
			cout<<"You Surendered!"<<endl;
			surr=1;
			winner=1;
			bet=bet/2;
			break;
		}
		if(Calcscore(your_hand)>21)
		{
			cout<<"Bust! You lose!"<<endl;
			if(insbet!=0)
			{
				dealer_hand.push_back(deck.back());
				deck.pop_back();
				PrintHand(dealer_hand);
				if(Calcscore(dealer_hand)==21)
				{
					insbet*=2;
					money+=insbet;
				}
			}
			winner=1;
			bet=0;
			break;
		}
		while(Calcscore(dealer_hand)<=16)
		{
			system("cls");
			dealer_hand.push_back(deck.back());
			deck.pop_back();
			PrintHand(dealer_hand);
			PrintHand(your_hand);
		}
		wincond(your_hand,dealer_hand,insbet,money,winner,bet);
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
	short decknum=1;
	cout<<"How many decks you wanna play with?"<<endl;
	cin>>decknum;
	vector<Cards>deck;
	while(new_game)
	{
		while(decknum<=0)cin>>decknum;
		cout<<"Bet money for new game,0 to exit"<<endl;
		cout<<"Current money: "<<money<<endl;
		cin>>bet;
		if(bet==0)
		{
			new_game=0;
			break;
		}
		cout<<"Press y to bet for war,any key for no bet"<<endl;
		cin>>c;
		if(c=='y' || c=='Y')warbet=bet;
		cout<<"Press y to bet for pair,any key for no bet"<<endl;
		cin>>c;
		if(c=='y' || c=='Y')pairbet=bet;
		draw(decknum,deck,bet,money,pairbet,warbet);
	}
	return 0;
}
