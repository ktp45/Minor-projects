#pragma once
class Cards  // each card has name, suit and power on black jack
{
	char name;
	short bjpower;
	short suit;
	public:
	Cards();	//default constructor just in case
	Cards(char nam,int power);	// constuctor with parameters
	short GetPower()const;// setters and getters to keep the capsulation
	char GetName()const;
	void SetPower(short power);
	void SetName(char nam);
	short GetSuit()const;
	void SetSuit(short sui);
};
