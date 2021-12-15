#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

const char* getFileContext (const char* path) {
  ifstream file;
  file.exceptions(ifstream::failbit | ifstream::badbit);
  try {
    file.open(path);
    stringstream strstream;
    strstream << file.rdbuf();
    
    string str = strstream.str();
    return str.c_str();
  } catch (ifstream::failure e) {
    cout << "ERROR::READ::FAILYRE" << endl;
    return NULL;
  }
}

int main(int argc, char *argv[])
{
  cout << "1231" << endl;
	cout << getFileContext("D:/document/workplace/Repo/backend/c/test/src/1.t") << endl;
}

const char* test (const char* path) {
  ifstream file;
  file.exceptions(ifstream::failbit | ifstream::badbit);
  try {
    stringstream ss;
    file.open(path);
    ss << file.rdBuf();
    string ss.str();
    return ss.c_str();
  } catch (ifstream::failure e) {} 
} 