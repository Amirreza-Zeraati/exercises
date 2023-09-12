#include<iostream>
#include<time.h>
#include <stdlib.h>
using namespace std;

int main()
{
    int i=0, j=0, n=0;
    srand(time(0));
    while ((i != 0 || j != 9) && (i != 9 || j != 9))
	{
		int move;
		move = rand() % 4 + 1;
		if(move==1)                // Moving Up
			if (i != 0)
				i--;
		if(move==2)                // Moving Down
			if (i != 9)
				i++;
		if(move==3)                // Moving Left
		    if (j != 0)
				j--;
		if(move==4)                // Moving Right
		    if (j != 9)
				j++;
		n++;
	}
    
    if (i == 0 && j == 9)
		cout << "move number = " << n << "\nMouse is winner";
	if (i == 9 && j == 9)
		cout << "move number = " << n << "\nMouse is loser";

    return 0;
}