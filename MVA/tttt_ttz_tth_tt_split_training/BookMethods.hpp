#ifndef BOOK_METHODS_HPP
#define BOOK_METHODS_HPP

//Changing to these include paths for compatibility with ROOT v5.34

#include "TMVA/Factory.h"

class map;

void SwitchTrainMethods();
void bookMethods(TMVA::Factory *factory, const std::map<std::string,bool>& Use);

#endif
