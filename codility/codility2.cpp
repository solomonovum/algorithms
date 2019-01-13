#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <unordered_map>

using std::string;

struct PhotoInfos {
	string Extention;
	string Place;
	int Year;
	int Month;
	int Day;
	int HH;
	int MM;
	int SS;
};

// compare two data and sort by ascendent order
bool compareTwo(PhotoInfos const & A, PhotoInfos const &  B)
{
	// year
	if (A.Year != B.Year)
		return  A.Year < B.Year;

	// month
	if (A.Month != B.Month)
		return  A.Month < B.Month;

	// day
	if (A.Day != B.Day)
		return  A.Day < B.Day;

	// HH
	if (A.HH != B.HH)
		return  A.HH < B.HH;
	// MM
	if (A.MM != B.MM)
		return  A.MM < B.MM;

	// SS
	return  A.SS < B.SS;
}

string solution(string &S) {
	std::string Result;

	if (S.empty()) {
		return Result;
	}

	// get raw string one by one
	using namespace std;

	vector<string> RawData;
	std::string GetString;
	stringstream Stream(S);
	
	while (getline(Stream, GetString, '\n')) {
		RawData.emplace_back(GetString);
	}

	// check photo size
	if (RawData.size() < 0 || RawData.size() > 100) {
		return Result;
	}

	// make photoinfo structure
	vector<PhotoInfos> PhotoData;
	unordered_map<string, int> PhotoNumberAtPlace;
	auto constexpr FirstPosition{ 0 };

	for (auto const Raw : RawData) {
		PhotoInfos PhotoInfo;

		// get extention
		auto DotPosition{ Raw.find(".") };
		auto Extension{ Raw.substr(DotPosition + 1, Raw.find(",") - DotPosition - 1) };
		PhotoInfo.Extention = Extension;
		auto Remainedstring{ Raw.substr(Raw.find(" ") + 1) };

		// get place
		auto Place{ Remainedstring.substr(FirstPosition, Remainedstring.find(",")) };
		PhotoInfo.Place = Place;
		PhotoNumberAtPlace.emplace(Place, 0);
		Remainedstring = Remainedstring.substr(Remainedstring.find(" "));

		// get year
		auto DashPosition{ Remainedstring.find("-") };
		auto Year{ Remainedstring.substr(FirstPosition, DashPosition) };
		PhotoInfo.Year = stoi(Year);
		Remainedstring = Remainedstring.substr(DashPosition + 1);

		// get month
		DashPosition = Remainedstring.find("-");
		auto Month{ Remainedstring.substr(FirstPosition, DashPosition) };
		PhotoInfo.Month = stoi(Month);
		Remainedstring = Remainedstring.substr(DashPosition + 1);

		// get day
		auto SpacePosition{ Remainedstring.find(" ") };
		auto Day{ Remainedstring.substr(FirstPosition, SpacePosition) };
		PhotoInfo.Day = stoi(Day);
		Remainedstring = Remainedstring.substr(SpacePosition + 1);

		// get HH
		auto ColonPosition{ Remainedstring.find(":") };
		auto HH{ Remainedstring.substr(FirstPosition, ColonPosition) };
		PhotoInfo.HH = stoi(HH);
		Remainedstring = Remainedstring.substr(ColonPosition + 1);

		// get MM
		ColonPosition =  Remainedstring.find(":");
		auto MM {Remainedstring.substr(FirstPosition, ColonPosition) };
		PhotoInfo.MM = stoi(MM);
		Remainedstring = Remainedstring.substr(ColonPosition + 1);

		// get SS
		auto SS{ Remainedstring.substr(FirstPosition, Remainedstring.find(":")) };
		PhotoInfo.SS = stoi(SS);

		PhotoData.emplace_back(PhotoInfo);
	}

	// sort by date
	sort(PhotoData.begin(), PhotoData.end(), compareTwo);

	// make result
	for (auto const PhotoInfo : PhotoData) {
		// place
		Result.append(PhotoInfo.Place);

		// number
		auto Number{ PhotoNumberAtPlace.find(PhotoInfo.Place) };

		if (Number != PhotoNumberAtPlace.end()) {
			Result.append(to_string(Number->second++));
		}

		// dot
		Result.append(".");

		// extension
		Result.append(PhotoInfo.Extention);

		// carrage return
		Result.append("\n");
	}

	return Result;
}
