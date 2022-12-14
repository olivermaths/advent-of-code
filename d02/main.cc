#include <fstream>
#include <iostream>
#include <string>


std::uint32_t getChoicePoint(char mn){
    if(mn == 'X') return 1;
    if(mn == 'Y') return 2;
    if(mn == 'Z') return 3;
    return 0;
}


std::uint32_t roundOneResult(char op, char mn){
    if(op=='A'){
        if(mn == 'X') return 3 + getChoicePoint(mn);
        if(mn == 'Y') return 6 + getChoicePoint(mn);
        if(mn == 'Z') return 0 + getChoicePoint(mn) ;
    }
    if(op=='B'){
        if(mn == 'X') return 0 + getChoicePoint(mn);
        if(mn == 'Y') return 3 + getChoicePoint(mn);
        if(mn == 'Z') return 6 + getChoicePoint(mn);
   
    }
    if(op=='C'){
        if(mn == 'X') return 6 + getChoicePoint(mn);
        if(mn == 'Y') return 0 + getChoicePoint(mn);
        if(mn == 'Z') return 3 + getChoicePoint(mn);
    }
    return 0;
}



std::uint32_t roundTwoResult(char op, char mn){
    if(op=='A'){
        if(mn == 'X') return 0 + getChoicePoint('Z');
        if(mn == 'Y') return 3 + getChoicePoint('X');
        if(mn == 'Z') return 6 + getChoicePoint('Y');
    }
    if(op=='B'){
        if(mn == 'X') return 0 + getChoicePoint('X');
        if(mn == 'Y') return 3 + getChoicePoint('Y');
        if(mn == 'Z') return 6 + getChoicePoint('Z');
    }
    if(op=='C'){
        if(mn == 'X') return 0 + getChoicePoint('Y');
        if(mn == 'Y') return 3 + getChoicePoint('Z');
        if(mn == 'Z') return 6 + getChoicePoint('X');
    }
    return 0;
}


int main() {

    std::ifstream file;
    std::uint32_t roundOneScore = 0, roundTwoScore = 0;

    file.open("d02/input", std::ifstream::in);
  
    

    for (std::string line; std::getline(file, line);) {
        char index = 0;
        char oponent, mine;
        for (char e : line) {
            if(!index++) oponent = e;
            if(index) mine = e;
        }
        index = 0;
        roundOneScore += roundOneResult(oponent, mine);
        roundTwoScore += roundTwoResult(oponent, mine);
    }

    std::cout << roundOneScore << "  " << roundTwoScore << '\n';

};