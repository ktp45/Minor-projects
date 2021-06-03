#include<iostream>
#include<vector>
#include<iterator>
#include <algorithm>
#include <cstdlib>
#include "Cards.h"
	Cards::Cards(){}
	Cards::Cards(char nam,int power)	// constuctor with parameters
	{
		name=nam;
		bjpower=power;
	}
	short Cards::GetPower()const// setters and getters to keep the capsulation
	{
		return bjpower;
	}
	char Cards::GetName()const
	{
		return name;
	}
	void Cards::SetPower(short power)
	{
		bjpower=power;
	}
	void Cards::SetName(char nam)
	{
		name=nam;
	}
	short Cards::GetSuit()const
	{
		return suit;
	}
	void Cards::SetSuit(short sui)
	{
		suit=sui;
	}
