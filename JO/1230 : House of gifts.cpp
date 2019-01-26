#include <iostream>

using namespace std;

// direction
int Dx[] = { 1, -1, 0, 0 };
int Dy[] = { 0, 0, -1, 1 };

int **Map;

int HouseLength;
int MaxGiftCount;
int HouseLengthBound;

void getGift(int X, int Y, int GiftCount) {
	// set entrance
	auto CurrentStatus = Map[X][Y];

	Map[X][Y] = 1;

	// exit when arrived at the end position
	if ((X == HouseLength) && (Y == HouseLength)) {
		Map[X][Y] = CurrentStatus;

		if (MaxGiftCount < GiftCount) {
			MaxGiftCount = GiftCount;
		}
		return;
	}

	// proceed, the EWSN, when except 1
	for (int i = 0; i < 4; i++) {
		auto Nx = X + Dx[i];
		auto Ny = Y + Dy[i];

		if (Map[Nx][Ny] != 1) {
			if (Map[Nx][Ny] == 2) {
				GiftCount++;
			}

			getGift(Nx, Ny, GiftCount);

			if (Map[Nx][Ny] == 2) {
				GiftCount--;
			}
		}
	}
	Map[X][Y] = CurrentStatus;
}

int main() {
	// get house length
	cin >> HouseLength;

  // house length check
	if (HouseLength > 10) {
		return 0;
	}

	// HouseLength with boundary
	auto WithBoundarySize = HouseLength + 2;

	// map init
	Map = new int*[WithBoundarySize];

	for (int i = 0; i < WithBoundarySize; ++i) {
		Map[i] = new int[WithBoundarySize];
	}

	// get map
	int X = 1, Y = 1;
	int count = 0;
	int InputChar;
	HouseLengthBound = HouseLength + 1;
	
	while(count < HouseLength) {
		cin >> InputChar;
		if (InputChar != 32 && InputChar != 10) {
			Map[X][Y++] = InputChar;

			if (Y == HouseLengthBound) {
				X++;
				Y = 1;
				count++;
			}
		}
	}

	// make boundary
	auto MaxBoundaryIndex = WithBoundarySize - 1;

	for (int i = 0; i < WithBoundarySize; ++i) {
		Map[0][i] = 1;
		Map[i][0] = 1;
		Map[MaxBoundaryIndex][i] = 1;
		Map[i][MaxBoundaryIndex] = 1;
	}

	// run
	auto GiftCount = 0;
	if (Map[1][1] == 2) {
		GiftCount++;
	}

	getGift(1, 1, GiftCount);

	cout << MaxGiftCount;

	// map free
	for (int i = 0; i < HouseLength; ++i) {
		delete[] Map[i];
	}
	delete[] Map;

	return 0;
}
