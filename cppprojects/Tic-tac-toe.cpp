#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main()
{
	int size, board[10][10] = {0}, mode;
	for (int i = 0; i  <  10; i++)
	{
		for (int j = 0; j  <  10; j++)
		{
			board[i][j] = i * 10 + j + 6;  // fill the board with numbers at least 6
		}
	}

	cout << "Choose game mode (1 - PvP,  2 - PvC):" << endl;
	cin >> mode;
	cin.clear();
	fflush(stdin);  // clear the cin incase someone writen 3 3 or 4 4
	cout << "Enter grid size:" << endl;
	cin >> size;
	for (int i = 0; i < size; i++)
	{
		for (int j = 0; j < size; j++)
		{
			cout << "[ ]";  // draw board
		}
		cout << endl;
	}
	cin.clear();
	fflush(stdin);  // clear the cin incase someone writen 3 3 or 4 4
	int x, y;
	if (mode == 2)
	{
		bool winner = 0; int br = 0, br2 = 0, br3 = 0;
		time_t t;
		while (winner!= 1)
		{
			if (br%2 == 0)
				cout << "It is Player 1 turn:" << endl;
			else
				cout << "It is CPU turn:" << endl;
			while (x < 1 || x>size || y < 1 || y>size || board[x-1][y-1] == 1 || board[x-1][y-1] == 2 )
			{
				if (br%2 == 0)
					cin >> x >> y;
				else
				{
					srand (time(&t));
					x = rand()%size + 1;
					y = rand()%size + 1;
				}
			}
			if (br%2 == 0)
				board[x-1][y-1] = 1;  //fill board with X or O
			else
				board[x-1][y-1] = 2;
			br++;  //number of turns
	   	for (int i = 0; i < size; i++)
      {
			   for (int j = 0; j < size; j++)
			   {
				    if (board[i][j] == 1)
							cout << "[" << "X" << "]";
				   	else if (board[i][j] == 2)
							cout << "[" << "O" << "]";  // draw updated board
				    else
							cout << "[ ]";
			    }
			    cout << endl;
	    }
		for (int i = 0; i < size; i++)
			{
				for (int j = 0; j < size; j++)
				{
					if (board[i][j] == 1 && board[i][j+1] == 1)
						br2++;
					if (board[j][i] == 1 && board[j+1][i] == 1)
						br3++;  // check for  winner by rows and cols
					if (br2 == size-1 && !winner)
					{
						if (board[i][j] == 1)
							cout << "PLayer 1 won!" << endl;
						else
							cout << "CPU won!" << endl;
							winner = 1;
						}
							if (br3 == size-1 && !winner)
						{
						if (board[j][i] == 1)
							cout << "PLayer 1 won!" << endl;
						else
							cout << "CPU won!" << endl;
							winner = 1;
					}
				}
				br2 = 0; br3 = 0;
			}
			for (int i = 0; i < size; i++)
			{
				if (i == size-1 && !winner)
				{
						if (board[i][i] == 1)
							cout << "PLayer 1 won!" << endl;  // check for  winner by main diag
					else
						cout << "CPU won!" << endl;
					winner = 1;
				}
				if (board[i][i]!= board[i + 1][i + 1])
					break;
			}
			for (int i = 0; i < size; i++)
			{
				if (i == size-1 && !winner)
				{
					if (board[i][size-i-1] == 1)cout << "PLayer 1 won!" << endl;  // check for  winner by alt diag
					else cout << "CPU won!" << endl;
					winner = 1;
				}
				if (board[i][size-i-1]!= board[i + 1][size - i - 2])break;
			}
			if (br == size * size && !winner)
			{
				cout << "There is no winner!" << endl;  // check if  board is full and no winner
				break;
			}
			x = 0; y = 0;

		}
	}
	else if (mode == 1)
	{
		bool winner = 0; int br = 0, br2 = 0, br3 = 0;
		while (winner!= 1)
		{
			if (br%2 == 0)cout << "It is Player 1 turn:" << endl;
			else cout << "It is Player 2 turn:" << endl;
			while (x < 1 || x > size || y < 1 || y > size || board[x - 1][y - 1] == 1 || board[x - 1][y - 1] == 2 )
			{
				cin >> x >> y;
			}
			if (br%2 == 0)
				board[x - 1][y - 1] = 1;
			else
				board[x - 1][y - 1] = 2;
			br++;
	    for (int i = 0; i < size; i++)
      {
		    for (int j = 0; j < size; j++)
		    {
			     if (board[i][j] == 1)
					 	cout << "[" << "X" << "]";
			     else if (board[i][j] == 2)
					 	cout << "[" << "O" << "]";
			     else
					 	cout << "[ ]";
		    }
		    cout << endl;
	     }
			for (int i = 0; i < size; i++)
			{
				for (int j = 0; j < size; j++)
				{
					if (board[i][j] == 1 && board[i][j + 1] == 1)
					 	br2++;
					if (board[j][i] == 1 && board[j + 1][i] == 1)
						br3++;
					if (br2 == size-1 && !winner)
					{
						if (board[i][j] == 1)
							cout << "PLayer 1 won!" << endl;
						else
							cout << "Player 2 won!" << endl;
						winner = 1;
					}
						if (br3 == size - 1 && !winner)
					{
					if (board[j][i] == 1)
						cout << "PLayer 1 won!" << endl;
					else
						cout << "Player 2 won!" << endl;
					winner = 1;
					}
				}
				br2 = 0; br3 = 0;
			}
			for (int i = 0; i < size; i++)
			{
				if (i == size - 1 && !winner)
				{
					if (board[i][i] == 1)
						cout << "PLayer 1 won!" << endl;
					else
						cout << "Player 2 won!" << endl;
					winner = 1;
				}
				if (board[i][i]!= board[i + 1][i + 1])
					break;
			}
				for (int i = 0; i < size; i++)
			{
				if (i == size-1 && !winner)
				{
					if (board[i][i] == 1)
						cout << "PLayer 1 won!" << endl;
					else
						cout << "Player 2 won!" << endl;
					winner = 1;
				}
				if (board[i][size - i - 1]!= board[i + 1][size - i - 2])
					break;
			}
				if (br == size * size && !winner)
			{
				cout << "There is no winner!" << endl;  // check if  board is full and no winner
				break;
			}
			x = 0; y = 0;
		}
	}
}
